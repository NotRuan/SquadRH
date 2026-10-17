"""Recepção do squad: detecta o estado e monta o contexto do início da sessão.

Roda no gancho SessionStart (matcher startup). Não conversa com ninguém — diz
à sessão quem chegou e o que pede ação, para a primeira resposta abrir com as
boas-vindas certas. Nunca falha: um gancho que quebra derruba a recepção
inteira, e um contexto mínimo é melhor que nenhum. stdlib apenas.
"""

import argparse
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

_CAMPO = re.compile(r"^- \*\*(.+?):\*\*[ \t]*(.*)$", flags=re.M)
_DATA = re.compile(r"(\d{4}-\d{2}-\d{2})")
DIAS_AGUARDANDO = 30
DIAS_LINKEDIN = 90


def ler_campos(texto):
    return {k.strip(): v.strip() for k, v in _CAMPO.findall(texto)}


def _ler(caminho):
    return caminho.read_text(encoding="utf-8") if caminho.exists() else ""


def estado(raiz):
    raiz = Path(raiz)
    if not (raiz / "perfil" / "candidato.md").exists():
        return "novo"
    if "confirmado por" not in _ler(raiz / "perfil" / "perfil-mestre.md").lower():
        return "construcao"
    return "pronto"


def _data(valor):
    m = _DATA.search(valor or "")
    return datetime.strptime(m.group(1), "%Y-%m-%d").date() if m else None


def _em_aberto(resultado):
    r = resultado.strip().strip("`").lower()
    return r == "" or r.startswith("aguardando") or "a preencher" in r or "a confirmar" in r


def _linha_candidaturas(raiz, hoje):
    abertas = atrasadas = 0
    for st in sorted((raiz / "vagas").glob("*/status.md")):
        campos = ler_campos(_ler(st))
        if not _em_aberto(campos.get("Resultado", "")):
            continue
        abertas += 1
        d = _data(campos.get("Data da candidatura", ""))
        if d and (hoje - d).days > DIAS_AGUARDANDO:
            atrasadas += 1
    if not abertas:
        return None
    return (f"{abertas} candidatura(s) com retorno em aberto, {atrasadas} há mais de "
            f"{DIAS_AGUARDANDO} dias — registre com /resultado")


def _linha_linkedin(raiz, hoje):
    pub = raiz / "linkedin" / "publicado.md"
    if not pub.exists():
        return "LinkedIn ainda não modelado pelo squad — /linkedin"
    d = _data(ler_campos(_ler(pub)).get("Publicado em", ""))
    if d and (hoje - d).days > DIAS_LINKEDIN:
        return f"LinkedIn publicado há {(hoje - d).days} dias — vale revisar com /linkedin"
    return None


def _linha_estudos(raiz):
    campos = ler_campos(_ler(raiz / "perfil" / "candidato.md"))
    pasta = campos.get("Pasta de estudos (opcional)", "")
    if campos.get("/sync-pos", "").lower() != "ligado" or not pasta or not Path(pasta).exists():
        return None
    try:
        import ler_pos
        cache = ler_pos.carregar_cache(raiz / "perfil" / "pos-fiap-cache.json")
        novos, mudados = ler_pos.diff_contra_cache(pasta, cache)
    except Exception:
        return None
    n = len(novos) + len(mudados)
    return f"{n} arquivo(s) novo(s) ou mudado(s) na pasta de estudos — /sync-pos" if n else None


def situacao(raiz, hoje):
    raiz = Path(raiz)
    linhas = [_linha_candidaturas(raiz, hoje), _linha_linkedin(raiz, hoje), _linha_estudos(raiz)]
    return [l for l in linhas if l]


def contexto(raiz, hoje):
    raiz = Path(raiz)
    est = estado(raiz)
    partes = ["[Recepção do squad de RH]", f"Estado: {est}"]
    if est != "novo":
        nome = ler_campos(_ler(raiz / "perfil" / "candidato.md")).get("Como chamar", "")
        if nome:
            partes.append(f"Candidato: {nome}")
    if est == "pronto":
        sit = situacao(raiz, hoje)
        partes.append("Situação:" if sit else "Situação: nada pede ação agora.")
        partes += [f"- {l}" for l in sit]
    partes.append(
        "Instrução: abra a primeira resposta desta sessão seguindo "
        f".claude/commands/inicio.md para o estado '{est}'. Se a primeira mensagem "
        "já for um pedido direto, cumprimente em uma linha e execute o pedido."
    )
    return "\n".join(partes)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description="Contexto de recepção do squad")
    p.add_argument("--raiz", default=".")
    p.add_argument("--hoje", default=None, help="AAAA-MM-DD (testes)")
    p.add_argument("--hook", action="store_true",
                   help="saída JSON do gancho SessionStart (additionalContext)")
    args = p.parse_args()
    hoje = datetime.strptime(args.hoje, "%Y-%m-%d").date() if args.hoje else date.today()
    try:
        texto = contexto(args.raiz, hoje)
    except Exception:
        texto = ("[Recepção do squad de RH]\nEstado: desconhecido\n"
                 "Instrução: siga .claude/commands/inicio.md.")
    if args.hook:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart",
                                                 "additionalContext": texto}},
                         ensure_ascii=False))
    else:
        print(texto)
    return 0


if __name__ == "__main__":
    sys.exit(main())
