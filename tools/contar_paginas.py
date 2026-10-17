"""Conta as páginas de um PDF lendo o /Count do nó de páginas.

Existe porque estimar páginas contando linhas de markdown erra — a página real
só é conhecida depois de gerar o PDF. stdlib apenas.
"""

import argparse
import re
import sys

PADRAO_COUNT = re.compile(rb"/Count\s+(\d+)")


def contar(caminho):
    with open(caminho, "rb") as f:
        dados = f.read()
    if not dados.startswith(b"%PDF"):
        raise ValueError("não é um PDF")
    achados = [int(m.group(1)) for m in PADRAO_COUNT.finditer(dados)]
    if not achados:
        raise ValueError("nenhum /Count encontrado no PDF")
    # Em PDFs com árvore de páginas aninhada há vários /Count; o da raiz é o
    # maior, porque soma os filhos.
    return max(achados)


def main():
    p = argparse.ArgumentParser(description="Conta páginas de um PDF")
    p.add_argument("pdf", help="caminho do PDF")
    p.add_argument("--max", type=int, default=1, help="máximo aceitável")
    a = p.parse_args()

    try:
        n = contar(a.pdf)
    except FileNotFoundError:
        print(f"erro: arquivo não encontrado: {a.pdf}", file=sys.stderr)
        return 2
    except ValueError as e:
        print(f"erro: {e}", file=sys.stderr)
        return 2

    if n > a.max:
        print(f"{n} páginas — excede o máximo de {a.max}")
        return 1
    print(f"{n} página(s) — dentro do máximo de {a.max}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
