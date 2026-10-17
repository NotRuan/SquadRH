"""Núcleo determinístico do agente de mercado.

Existe porque contar termos por rodada e comparar frações entre rodadas é
trabalho que um script faz certo e um LLM faz de forma instável — e é isso que
torna a memória temporal (fatos-mercado.md) confiável e o /ensaio comparável.
Só faz a parte determinística; extrair os termos de cada vaga é trabalho do
coletor, que os escreve no snapshot. stdlib apenas.
"""

import argparse
import re

_PADRAO_BLOCO = re.compile(r"^### ", flags=re.M)
_PADRAO_TERMOS = re.compile(r"^- Termos:\s*(.+)$", flags=re.M)
_LIMIAR_ESTAVEL = 0.03  # variação de proporção abaixo disso é "estável"


def parse_snapshot(texto):
    """Devolve (n_vagas, {termo: n_blocos_que_citam}). Termo normalizado."""
    blocos = _PADRAO_BLOCO.split(texto)[1:]  # descarta o preâmbulo antes do 1º ###
    n = len(blocos)
    contagem = {}
    for bloco in blocos:
        m = _PADRAO_TERMOS.search(bloco)
        if not m:
            continue
        termos = {t.strip().lower() for t in m.group(1).split(",") if t.strip()}
        for t in termos:
            contagem[t] = contagem.get(t, 0) + 1
    return n, contagem


def formata_fracao(contagem, n):
    return f"{contagem}/{n}"


def _proporcao(fracao):
    a, b = fracao.split("/")
    b = int(b)
    return int(a) / b if b else 0.0


def tendencia(anterior, atual):
    if atual is None:
        return ""
    if anterior is None:
        return "novo"
    d = _proporcao(atual) - _proporcao(anterior)
    if d > _LIMIAR_ESTAVEL:
        return "↑"
    if d < -_LIMIAR_ESTAVEL:
        return "↓"
    return "estável"


def _le_tabela(fatos_md):
    """Devolve (colunas_rodada, linhas) onde linha = {termo, categoria, {coluna: fracao}}."""
    linhas_md = [l for l in fatos_md.splitlines() if l.strip().startswith("|")]
    if len(linhas_md) < 2:
        return [], []
    header = [c.strip() for c in linhas_md[0].strip("|").split("|")]
    # header: termo | categoria | <rodadas...> | tendência
    colunas_rodada = header[2:-1]
    linhas = []
    for l in linhas_md[2:]:  # pula header e separador
        celulas = [c.strip() for c in l.strip("|").split("|")]
        if len(celulas) != len(header):
            continue
        termo, categoria = celulas[0], celulas[1]
        fracoes = dict(zip(colunas_rodada, celulas[2:-1]))
        linhas.append({"termo": termo, "categoria": categoria, "fracoes": fracoes})
    return colunas_rodada, linhas


def _emite_tabela(colunas_rodada, linhas):
    header = ["termo", "categoria"] + colunas_rodada + ["tendência"]
    sep = ["-" * max(3, len(c)) for c in header]
    out = ["| " + " | ".join(header) + " |", "|" + "|".join(sep) + "|"]
    ultimas = colunas_rodada[-2:]
    for ln in linhas:
        ant = ln["fracoes"].get(ultimas[0]) if len(ultimas) == 2 else None
        atual = ln["fracoes"].get(colunas_rodada[-1]) if colunas_rodada else None
        tend = tendencia(ant, atual)
        celulas = [ln["termo"], ln["categoria"]]
        celulas += [ln["fracoes"].get(c, "—") for c in colunas_rodada]
        celulas.append(tend)
        out.append("| " + " | ".join(celulas) + " |")
    return "\n".join(out) + "\n"


def atualiza_fatos(fatos_md, contagem, n, coluna):
    colunas_rodada, linhas = _le_tabela(fatos_md)
    if coluna not in colunas_rodada:
        colunas_rodada = colunas_rodada + [coluna]
    por_termo = {ln["termo"]: ln for ln in linhas}
    # termos já conhecidos
    for termo, ln in por_termo.items():
        c = contagem.get(termo, 0)
        ln["fracoes"][coluna] = formata_fracao(c, n)
    # termos novos nesta rodada
    for termo, c in sorted(contagem.items()):
        if termo not in por_termo:
            ln = {"termo": termo, "categoria": "?", "fracoes": {coluna: formata_fracao(c, n)}}
            linhas.append(ln)
    return _emite_tabela(colunas_rodada, linhas)


def _cmd_atualizar(args):
    with open(args.snapshot, encoding="utf-8") as f:
        n, contagem = parse_snapshot(f.read())
    with open(args.fatos, encoding="utf-8") as f:
        fatos_md = f.read()
    conhecidos = {ln["termo"] for ln in _le_tabela(fatos_md)[1]}
    novos = sum(1 for t in contagem if t not in conhecidos)
    saida = atualiza_fatos(fatos_md, contagem, n, args.coluna)
    with open(args.fatos, "w", encoding="utf-8") as f:
        f.write(saida)
    print(f"{n} vagas, {len(contagem)} termos, {novos} novos")


def main():
    p = argparse.ArgumentParser(description="Núcleo do agente de mercado")
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("atualizar", help="funde um snapshot em fatos-mercado.md")
    a.add_argument("--snapshot", required=True)
    a.add_argument("--fatos", required=True)
    a.add_argument("--coluna", required=True, help="rótulo da rodada, ex. 2026-S36")
    a.set_defaults(func=_cmd_atualizar)
    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
