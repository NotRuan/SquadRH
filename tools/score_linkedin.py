"""Núcleo determinístico do score de LinkedIn (/linkedin).

Calcula os blocos Busca e Completude e soma com Abertura e Prova, que são
julgamento do modelo e chegam prontos. Existe pelo mesmo motivo do mercado.py:
contar em que seção cada termo aparece é trabalho que um script faz certo e um
LLM faz de forma instável — e o revisor-linkedin precisa chegar ao mesmo
número. stdlib apenas.
"""

import argparse
import re
import sys
import unicodedata

import mercado

PESOS_SECAO = {"headline": 2.0, "competencias": 1.5, "sobre": 1.0, "experiencia": 1.0}
ITENS_CONFIG = ["foto", "banner", "url personalizada", "open to work", "localidade",
                "top 5 competencias fixadas"]
ITENS_FATO = ["em destaque", "formacao", "certificacoes", "idiomas"]
PONTOS_ITEM = 1.5
MAX_ABERTURA = 20
MAX_PROVA = 15

_SECAO = re.compile(r"^## (.+)$", flags=re.M)
_TITULOS = re.compile(r"^- \*\*Títulos:\*\*\s*(.+)$", flags=re.M)
_ITEM = re.compile(r"^- \[([ xX])\]\s*(.+?)\s*$", flags=re.M)


def _norm(texto):
    texto = unicodedata.normalize("NFKD", texto.lower())
    return "".join(c for c in texto if not unicodedata.combining(c)).strip()


def _secoes(md):
    partes = _SECAO.split(md)
    return {_norm(partes[i]): partes[i + 1] for i in range(1, len(partes) - 1, 2)}


def titulos(vertente_md):
    m = _TITULOS.search(vertente_md)
    if not m:
        return []
    return [_norm(t) for t in m.group(1).split(",") if t.strip()]


def termos_recorrentes(vertente_md):
    n, contagem = mercado.parse_snapshot(_secoes(vertente_md).get("anuncios", ""))
    recorrentes = {_norm(t) for t, c in contagem.items() if n and 2 * c >= n}
    return sorted(recorrentes | set(titulos(vertente_md)))


def parse_perfil(perfil_md):
    secoes = _secoes(perfil_md)
    completude = {_norm(item): marca.lower() == "x"
                  for marca, item in _ITEM.findall(secoes.get("completude", ""))}
    perfil = {chave: _norm(secoes.get(chave, "")) for chave in PESOS_SECAO}
    perfil["completude"] = completude
    return perfil


def _contem(texto, termo):
    return re.search(r"(?<!\w)" + re.escape(termo) + r"(?!\w)", texto) is not None


def peso_termo(termo, perfil):
    t = _norm(termo)
    return max((peso for secao, peso in PESOS_SECAO.items() if _contem(perfil[secao], t)),
               default=0.0)


def _escala(soma, n):
    return round(soma / (2 * n) * 50, 2) if n else 0.0


def score_busca(termos, perfil):
    return _escala(sum(peso_termo(t, perfil) for t in termos), len(termos))


def score_completude(completude):
    marcados = sum(1 for item in ITENS_CONFIG + ITENS_FATO if completude.get(item))
    return round(marcados * PONTOS_ITEM, 2)


def busca_teto(termos, titulos_, lastro, perfil):
    """Melhor Busca possível com os fatos existentes.

    Todo termo com lastro pode ir para a headline (peso 2) — título ocupado ou
    competência com fato. Limitar competência a 1,5 fazia a proposta passar do
    teto (falha L2 do ensaio de 16/10/2026). `titulos_` e `perfil` ficam na
    assinatura porque o lastro de título é decidido por quem chama: só entra
    em `lastro` o título que o candidato ocupou.
    """
    lastro = {_norm(x) for x in lastro}
    soma = sum(PESOS_SECAO["headline"] for t in termos if t in lastro)
    return _escala(soma, len(termos))


def completude_teto(itens_fato_com_lastro, completude):
    possiveis = {_norm(x) for x in itens_fato_com_lastro}
    possiveis |= {i for i in ITENS_FATO if completude.get(i)}
    n = len(ITENS_CONFIG) + sum(1 for i in ITENS_FATO if i in possiveis)
    return round(n * PONTOS_ITEM, 2)


def total(busca, abertura, prova, completude):
    if not 0 <= abertura <= MAX_ABERTURA:
        raise ValueError(f"abertura fora de 0–{MAX_ABERTURA}: {abertura}")
    if not 0 <= prova <= MAX_PROVA:
        raise ValueError(f"prova fora de 0–{MAX_PROVA}: {prova}")
    return round(busca + abertura + prova + completude, 2)


def _br(x):
    return f"{x:.2f}".replace(".", ",")


_ROTULO = {2.0: "headline (2)", 1.5: "competências (1,5)", 1.0: "sobre/experiência (1)",
           0.0: "ausente (0)"}


def _imprime(termos, perfil, busca, abertura, prova, completude, n_itens):
    print(f"termos da vertente: {len(termos)}")
    for t in termos:
        print(f"  {t:<28} {_ROTULO[peso_termo(t, perfil)]}")
    print(f"busca       {_br(busca)} / 50")
    print(f"abertura    {_br(abertura)} / 20  (julgamento)")
    print(f"prova       {_br(prova)} / 15  (julgamento)")
    print(f"completude  {_br(completude)} / 15  ({n_itens}/10 itens)")
    print(f"total       {_br(total(busca, abertura, prova, completude))} / 100")


def _ler(caminho):
    with open(caminho, encoding="utf-8") as f:
        return f.read()


def _cmd_score(args):
    vertente = _ler(args.vertente)
    perfil = parse_perfil(_ler(args.perfil))
    termos = termos_recorrentes(vertente)
    completude = score_completude(perfil["completude"])
    _imprime(termos, perfil, score_busca(termos, perfil), args.abertura, args.prova,
             completude, int(completude / PONTOS_ITEM))


def _cmd_teto(args):
    vertente = _ler(args.vertente)
    perfil = parse_perfil(_ler(args.perfil))
    termos = termos_recorrentes(vertente)
    lastro = [x for x in args.lastro.split(",") if x.strip()]
    itens = [x for x in args.itens.split(",") if x.strip()]
    busca = busca_teto(termos, titulos(vertente), lastro, perfil)
    completude = completude_teto(itens, perfil["completude"])
    print("TETO — melhor score possível com os fatos que já existem")
    _imprime(termos, perfil, busca, args.abertura, args.prova, completude,
             int(completude / PONTOS_ITEM))


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description="Score de LinkedIn para a vertente")
    sub = p.add_subparsers(dest="cmd", required=True)
    for nome, func in (("score", _cmd_score), ("teto", _cmd_teto)):
        s = sub.add_parser(nome)
        s.add_argument("--vertente", required=True)
        s.add_argument("--perfil", required=True)
        s.add_argument("--abertura", type=float, required=True)
        s.add_argument("--prova", type=float, required=True)
        if nome == "teto":
            s.add_argument("--lastro", required=True, help="termos com fato, separados por vírgula")
            s.add_argument("--itens", default="", help="itens de completude com fato, separados por vírgula")
        s.set_defaults(func=func)
    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
