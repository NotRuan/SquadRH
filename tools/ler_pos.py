"""Lê projetos, práticas e e-books da Pós-FIAP para alimentar o /sync-pos.

Fonte separada do LinkedIn (ver ler_linkedin.py): aqui não há zip, é uma
pasta local fora do repositório. Três operações: --listar (o que é novo
desde a última rodada), --ler (conteúdo bruto de um arquivo, pra virar
candidato a stack) e --marcar (grava o resultado da validação no cache).

stdlib apenas — o ambiente não garante pip.
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

SUBPASTA_TIPO = {
    "01_Projetos": "projeto",
    "00_Práticas - Exercicios": "projeto",
    "02_PDF's": "ebook",
}

NOMES_RELEVANTES = {"README.md", "requirements.txt", "pyproject.toml"}
EXTENSOES_RELEVANTES = {".ipynb", ".pdf"}


def _tipo_de(caminho_relativo):
    primeira_parte = Path(caminho_relativo).parts[0]
    return SUBPASTA_TIPO.get(primeira_parte)


def arquivos_relevantes(raiz):
    """Devolve os caminhos relativos (à raiz) de todo arquivo que interessa."""
    encontrados = []
    for caminho in Path(raiz).rglob("*"):
        if not caminho.is_file():
            continue
        relevante = caminho.name in NOMES_RELEVANTES or caminho.suffix.lower() in EXTENSOES_RELEVANTES
        if not relevante:
            continue
        relativo = caminho.relative_to(raiz).as_posix()
        if _tipo_de(relativo) is None:
            continue
        encontrados.append(relativo)
    return sorted(encontrados)


def impressao_digital(raiz, caminho_relativo):
    stat = (Path(raiz) / caminho_relativo).stat()
    return {
        "tamanho_bytes": stat.st_size,
        "modificado_em": datetime.fromtimestamp(stat.st_mtime).isoformat(timespec="seconds"),
    }


def carregar_cache(caminho_cache):
    caminho_cache = Path(caminho_cache)
    if not caminho_cache.exists():
        return {"processados": []}
    with open(caminho_cache, encoding="utf-8") as f:
        return json.load(f)


def salvar_cache(caminho_cache, dados):
    caminho_cache = Path(caminho_cache)
    caminho_cache.parent.mkdir(parents=True, exist_ok=True)
    with open(caminho_cache, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")


def _entrada_por_caminho(cache, caminho_relativo):
    for entrada in cache["processados"]:
        if entrada["caminho"] == caminho_relativo:
            return entrada
    return None


def diff_contra_cache(raiz, cache):
    """Devolve (novos, mudados): listas de caminhos relativos, ordenadas."""
    novos, mudados = [], []
    for caminho_relativo in arquivos_relevantes(raiz):
        atual = impressao_digital(raiz, caminho_relativo)
        entrada = _entrada_por_caminho(cache, caminho_relativo)
        if entrada is None:
            novos.append(caminho_relativo)
        elif (entrada["tamanho_bytes"], entrada["modificado_em"]) != (atual["tamanho_bytes"], atual["modificado_em"]):
            mudados.append(caminho_relativo)
    return novos, mudados


_PADRAO_IMPORT = re.compile(r"^\s*(?:import|from)\s+([A-Za-z_][A-Za-z0-9_.]*)")


def imports_do_notebook(texto_json):
    """Devolve os módulos top-level importados nas células de código, sem duplicar."""
    notebook = json.loads(texto_json)
    modulos = set()
    for celula in notebook.get("cells", []):
        if celula.get("cell_type") != "code":
            continue
        linhas = celula.get("source", [])
        if isinstance(linhas, str):
            linhas = linhas.splitlines()
        for linha in linhas:
            m = _PADRAO_IMPORT.match(linha)
            if m:
                modulos.add(m.group(1).split(".")[0])
    return sorted(modulos)


class ArquivoBinarioError(Exception):
    """PDF (ou outro binário) pedido via --ler — precisa da ferramenta Read, não deste script."""


def ler_conteudo(raiz, caminho_relativo):
    caminho_absoluto = Path(raiz) / caminho_relativo
    if caminho_absoluto.suffix == ".pdf":
        raise ArquivoBinarioError(
            f"{caminho_relativo} é um PDF — leia com a ferramenta Read, não com --ler "
            "(texto extraído de binário aqui sairia corrompido)."
        )
    if caminho_absoluto.suffix == ".ipynb":
        modulos = imports_do_notebook(caminho_absoluto.read_text(encoding="utf-8"))
        return "\n".join(f"import: {m}" for m in modulos)
    return caminho_absoluto.read_text(encoding="utf-8", errors="replace")


def marcar(caminho_cache, raiz, caminho_relativo, status, candidatos, projeto):
    cache = carregar_cache(caminho_cache)
    atual = impressao_digital(raiz, caminho_relativo)
    entrada = _entrada_por_caminho(cache, caminho_relativo)
    dados = {
        "caminho": caminho_relativo,
        "projeto": projeto,
        "tipo": _tipo_de(caminho_relativo),
        "tamanho_bytes": atual["tamanho_bytes"],
        "modificado_em": atual["modificado_em"],
        "processado_em": datetime.now().date().isoformat(),
        "status": status,
        "candidatos": candidatos,
    }
    if entrada is None:
        cache["processados"].append(dados)
    else:
        entrada.update(dados)
    salvar_cache(caminho_cache, cache)


def main():
    # Caminhos da Pós ("Práticas", "Pós-FIAP") têm acento, e o processo não
    # roda num console interativo — sem isto, o Windows imprime na codepage
    # ANSI local (cp1252) e quem lê a saída como UTF-8 (nossos testes, o
    # Claude Code) recebe lixo ou crash de decodificação.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser()
    parser.add_argument("--raiz", help="pasta raiz da Pós-FIAP")
    parser.add_argument("--cache", required=True, help="caminho do pos-fiap-cache.json")
    parser.add_argument("--listar", action="store_true")
    parser.add_argument("--ler", metavar="CAMINHO")
    parser.add_argument("--marcar", metavar="CAMINHO")
    parser.add_argument("--status", choices=["confirmado", "pendente_validacao"])
    parser.add_argument("--candidatos", help="lista separada por vírgula")
    parser.add_argument("--projeto", help="nome do projeto/e-book que agrupa o arquivo")
    args = parser.parse_args()

    if args.listar:
        if not args.raiz:
            print("--raiz é obrigatório com --listar", file=sys.stderr)
            sys.exit(1)
        cache = carregar_cache(args.cache)
        novos, mudados = diff_contra_cache(args.raiz, cache)
        if not novos and not mudados:
            print("Nada novo desde a última rodada.")
            return
        for caminho in novos:
            print(f"[novo][{_tipo_de(caminho)}] {caminho}")
        for caminho in mudados:
            print(f"[mudado][{_tipo_de(caminho)}] {caminho}")
        return

    if args.ler:
        if not args.raiz:
            print("--raiz é obrigatório com --ler", file=sys.stderr)
            sys.exit(1)
        try:
            print(ler_conteudo(args.raiz, args.ler))
        except ArquivoBinarioError as e:
            print(f"erro: {e}", file=sys.stderr)
            sys.exit(1)
        return

    if args.marcar:
        if not args.raiz or not args.status or args.candidatos is None or not args.projeto:
            print("--marcar exige --raiz, --status, --candidatos e --projeto", file=sys.stderr)
            sys.exit(1)
        candidatos = [c.strip() for c in args.candidatos.split(",") if c.strip()]
        marcar(args.cache, args.raiz, args.marcar, args.status, candidatos, args.projeto)
        print(f"Cache atualizado: {args.marcar}")
        return

    parser.print_help()
    sys.exit(1)


if __name__ == "__main__":
    main()
