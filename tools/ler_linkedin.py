"""Lê o export do LinkedIn (zip) em memória, sem extrair nada para o disco.

O export é um zip plano com dezenas de CSVs, a maioria irrelevante para um
currículo. Este utilitário expõe só os que importam.

stdlib apenas — o ambiente não garante pip.
"""

import argparse
import csv
import io
import sys
import zipfile

# Confirmado contra o export real de 14/08/2026 (43 arquivos). Courses.csv e
# Recommendations_Received.csv NÃO existem neste export — o equivalente é
# Learning.csv.
RELEVANTES = [
    "Positions.csv",
    "Profile.csv",
    "Education.csv",
    "Skills.csv",
    "Certifications.csv",
    "Languages.csv",
    "Learning.csv",
]

# Não alimentam o currículo — alimentam a decisão de candidatura. Connections
# responde "eu conheço alguém aí dentro?", que converte muito melhor que o
# formulário do portal. Job Applications é o histórico de candidaturas do
# próprio LinkedIn, ponto de partida do funil.
DE_CANDIDATURA = [
    "Connections.csv",
    "Jobs/Job Applications.csv",
]


def listar(caminho_zip):
    with zipfile.ZipFile(caminho_zip) as z:
        presentes = set(z.namelist())
    for rotulo, grupo in (("perfil", RELEVANTES), ("candidatura", DE_CANDIDATURA)):
        print(f"[{rotulo}]")
        for nome in grupo:
            marca = "presente" if nome in presentes else "ausente "
            print(f"  {marca}  {nome}")
    return 0


def _linhas_csv(caminho_zip, nome_csv):
    """Devolve as linhas do CSV como dicts. O export traz um preâmbulo em
    alguns arquivos: a primeira linha com vírgula suficiente vira cabeçalho."""
    with zipfile.ZipFile(caminho_zip) as z:
        if nome_csv not in z.namelist():
            return None
        texto = z.read(nome_csv).decode("utf-8-sig", errors="replace")
    linhas = list(csv.reader(io.StringIO(texto)))
    for i, linha in enumerate(linhas):
        if len(linha) >= 2:
            cabecalho = [c.strip() for c in linha]
            return [dict(zip(cabecalho, l)) for l in linhas[i + 1:] if len(l) == len(cabecalho)]
    return []


def buscar_empresa(caminho_zip, termo):
    """Quem da minha rede trabalha (ou trabalhou) nesta empresa.

    Uma indicação converte muito acima de uma candidatura por portal — este é o
    passo mais barato de toda a candidatura, e o dado já está no export.
    """
    registros = _linhas_csv(caminho_zip, "Connections.csv")
    if registros is None:
        print("erro: Connections.csv não está neste export", file=sys.stderr)
        return 1

    alvo = termo.strip().lower()
    achados = [r for r in registros if alvo in (r.get("Company") or "").lower()]

    if not achados:
        print(f"nenhuma conexão em empresa contendo \"{termo}\" ({len(registros)} conexões lidas)")
        return 0

    print(f"{len(achados)} conexão(ões) em empresa contendo \"{termo}\":")
    print()
    for r in achados:
        nome = f"{r.get('First Name', '')} {r.get('Last Name', '')}".strip()
        print(f"  {nome} — {r.get('Position', '?')} @ {r.get('Company', '?')}"
              f" (conectado em {r.get('Connected On', '?')})")
    return 0


def imprimir(caminho_zip, nome_csv):
    with zipfile.ZipFile(caminho_zip) as z:
        if nome_csv not in z.namelist():
            print(f"erro: {nome_csv} não encontrado no export", file=sys.stderr)
            return 1
        bruto = z.read(nome_csv)
    texto = bruto.decode("utf-8-sig", errors="replace")
    sys.stdout.write(texto)
    return 0


def main():
    # No Windows, stdout redirecionado usa a codepage do console (cp1252) e
    # estoura em qualquer acento — e tanto o CSV do LinkedIn quanto as
    # mensagens daqui são cheios deles. A saída deste utilitário é sempre
    # lida por outro processo, então é sempre redirecionada.
    for fluxo in (sys.stdout, sys.stderr):
        try:
            fluxo.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass

    p = argparse.ArgumentParser(description="Lê o export do LinkedIn")
    p.add_argument("--zip", required=True, help="caminho do arquivo .zip")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--listar", action="store_true", help="lista os CSVs relevantes")
    g.add_argument("--csv", help="imprime o conteúdo de um CSV")
    g.add_argument("--empresa", help="lista conexões que trabalham nesta empresa")
    a = p.parse_args()

    try:
        if a.listar:
            return listar(a.zip)
        if a.empresa:
            return buscar_empresa(a.zip, a.empresa)
        return imprimir(a.zip, a.csv)
    except FileNotFoundError:
        print(f"erro: arquivo não encontrado: {a.zip}", file=sys.stderr)
        return 2
    except zipfile.BadZipFile:
        print(f"erro: não é um zip válido: {a.zip}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
