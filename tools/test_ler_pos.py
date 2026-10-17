import json
import subprocess
import sys
from pathlib import Path

import ler_pos

AQUI = Path(__file__).parent
LEITOR = AQUI / "ler_pos.py"


def _pos_falsa(tmp_path):
    raiz = tmp_path / "pos"
    projeto = raiz / "01_Projetos" / "TECH CHALLENGE" / "FASE 01"
    projeto.mkdir(parents=True)
    (projeto / "README.md").write_text("Projeto com FastAPI e Docker.", encoding="utf-8")
    (projeto / "requirements.txt").write_text("fastapi\n", encoding="utf-8")

    pratica = raiz / "00_Práticas - Exercicios" / "aula-01"
    pratica.mkdir(parents=True)
    (pratica / "README.md").write_text("Exercício de pandas.", encoding="utf-8")

    ebooks = raiz / "02_PDF's"
    ebooks.mkdir(parents=True)
    (ebooks / "Spark na prática.pdf").write_bytes(b"%PDF-1.4 conteudo falso")

    (raiz / "02_PDF's" / "ignorar.txt").write_text("não é relevante", encoding="utf-8")

    return raiz


def test_arquivos_relevantes_pega_readme_requirements_e_pdf_ignora_o_resto(tmp_path):
    raiz = _pos_falsa(tmp_path)
    achados = ler_pos.arquivos_relevantes(raiz)
    assert "01_Projetos/TECH CHALLENGE/FASE 01/README.md" in achados
    assert "01_Projetos/TECH CHALLENGE/FASE 01/requirements.txt" in achados
    assert "00_Práticas - Exercicios/aula-01/README.md" in achados
    assert "02_PDF's/Spark na prática.pdf" in achados
    assert not any(c.endswith("ignorar.txt") for c in achados)


def test_impressao_digital_tem_tamanho_e_data(tmp_path):
    raiz = _pos_falsa(tmp_path)
    fp = ler_pos.impressao_digital(raiz, "01_Projetos/TECH CHALLENGE/FASE 01/README.md")
    assert fp["tamanho_bytes"] > 0
    assert "T" in fp["modificado_em"]  # formato ISO


def test_carregar_cache_ausente_comeca_vazio(tmp_path):
    cache = ler_pos.carregar_cache(tmp_path / "nao-existe.json")
    assert cache == {"processados": []}


def test_diff_marca_tudo_como_novo_na_primeira_rodada(tmp_path):
    raiz = _pos_falsa(tmp_path)
    cache = ler_pos.carregar_cache(tmp_path / "cache.json")
    novos, mudados = ler_pos.diff_contra_cache(raiz, cache)
    assert len(novos) == 4
    assert mudados == []


def test_diff_nao_repete_arquivo_ja_processado_sem_mudanca(tmp_path):
    raiz = _pos_falsa(tmp_path)
    caminho_readme = "01_Projetos/TECH CHALLENGE/FASE 01/README.md"
    fp = ler_pos.impressao_digital(raiz, caminho_readme)
    cache = {"processados": [{"caminho": caminho_readme, **fp}]}
    novos, mudados = ler_pos.diff_contra_cache(raiz, cache)
    assert caminho_readme not in novos
    assert caminho_readme not in mudados


def test_diff_marca_como_mudado_quando_tamanho_muda(tmp_path):
    raiz = _pos_falsa(tmp_path)
    caminho_readme = "01_Projetos/TECH CHALLENGE/FASE 01/README.md"
    cache = {"processados": [{"caminho": caminho_readme, "tamanho_bytes": 1, "modificado_em": "2020-01-01T00:00:00"}]}
    novos, mudados = ler_pos.diff_contra_cache(raiz, cache)
    assert caminho_readme in mudados
    assert caminho_readme not in novos


def test_cli_listar_sem_mudanca_avisa(tmp_path):
    raiz = tmp_path / "pos-vazia"
    raiz.mkdir()
    cache = tmp_path / "cache.json"
    r = subprocess.run(
        [sys.executable, str(LEITOR), "--raiz", str(raiz), "--cache", str(cache), "--listar"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert r.returncode == 0
    assert "Nada novo" in r.stdout


def test_cli_listar_classifica_novo_e_tipo(tmp_path):
    raiz = _pos_falsa(tmp_path)
    cache = tmp_path / "cache.json"
    r = subprocess.run(
        [sys.executable, str(LEITOR), "--raiz", str(raiz), "--cache", str(cache), "--listar"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert r.returncode == 0
    assert "[novo][projeto]" in r.stdout
    assert "[novo][ebook]" in r.stdout
    assert "Spark na prática.pdf" in r.stdout


NOTEBOOK_EXEMPLO = json.dumps({
    "cells": [
        {"cell_type": "code", "source": ["import pandas as pd\n", "from sklearn.linear_model import LinearRegression\n"]},
        {"cell_type": "markdown", "source": ["# Título\n"]},
        {"cell_type": "code", "source": ["import pandas as pd\n", "import docker\n"]},
    ]
})


def test_imports_do_notebook_ignora_duplicata_e_markdown():
    modulos = ler_pos.imports_do_notebook(NOTEBOOK_EXEMPLO)
    assert modulos == ["docker", "pandas", "sklearn"]


def test_ler_conteudo_de_readme_devolve_texto_bruto(tmp_path):
    raiz = _pos_falsa(tmp_path)
    texto = ler_pos.ler_conteudo(raiz, "01_Projetos/TECH CHALLENGE/FASE 01/README.md")
    assert "FastAPI" in texto


def test_ler_conteudo_de_notebook_devolve_imports(tmp_path):
    raiz = _pos_falsa(tmp_path)
    nb = raiz / "01_Projetos" / "TECH CHALLENGE" / "FASE 01" / "analise.ipynb"
    nb.write_text(NOTEBOOK_EXEMPLO, encoding="utf-8")
    texto = ler_pos.ler_conteudo(raiz, "01_Projetos/TECH CHALLENGE/FASE 01/analise.ipynb")
    assert texto == "import: docker\nimport: pandas\nimport: sklearn"


def test_cli_ler_imprime_conteudo(tmp_path):
    raiz = _pos_falsa(tmp_path)
    cache = tmp_path / "cache.json"
    r = subprocess.run(
        [sys.executable, str(LEITOR), "--raiz", str(raiz), "--cache", str(cache),
         "--ler", "01_Projetos/TECH CHALLENGE/FASE 01/README.md"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert r.returncode == 0
    assert "FastAPI" in r.stdout


def test_ler_conteudo_de_pdf_levanta_erro_claro(tmp_path):
    raiz = _pos_falsa(tmp_path)
    import pytest
    with pytest.raises(ler_pos.ArquivoBinarioError):
        ler_pos.ler_conteudo(raiz, "02_PDF's/Spark na prática.pdf")


def test_cli_ler_em_pdf_sai_com_erro_claro(tmp_path):
    raiz = _pos_falsa(tmp_path)
    cache = tmp_path / "cache.json"
    r = subprocess.run(
        [sys.executable, str(LEITOR), "--raiz", str(raiz), "--cache", str(cache),
         "--ler", "02_PDF's/Spark na prática.pdf"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert r.returncode == 1
    assert "Read" in r.stderr


def test_marcar_grava_nova_entrada_no_cache(tmp_path):
    raiz = _pos_falsa(tmp_path)
    caminho_cache = tmp_path / "cache.json"
    caminho_readme = "01_Projetos/TECH CHALLENGE/FASE 01/README.md"
    ler_pos.marcar(caminho_cache, raiz, caminho_readme, "confirmado", ["FastAPI", "Docker"], "Tech Challenge — Fase 01")
    cache = ler_pos.carregar_cache(caminho_cache)
    entrada = cache["processados"][0]
    assert entrada["caminho"] == caminho_readme
    assert entrada["projeto"] == "Tech Challenge — Fase 01"
    assert entrada["tipo"] == "projeto"
    assert entrada["status"] == "confirmado"
    assert entrada["candidatos"] == ["FastAPI", "Docker"]
    assert "processado_em" in entrada


def test_marcar_atualiza_entrada_existente_em_vez_de_duplicar(tmp_path):
    raiz = _pos_falsa(tmp_path)
    caminho_cache = tmp_path / "cache.json"
    caminho_readme = "01_Projetos/TECH CHALLENGE/FASE 01/README.md"
    ler_pos.marcar(caminho_cache, raiz, caminho_readme, "pendente_validacao", ["FastAPI"], "Tech Challenge — Fase 01")
    ler_pos.marcar(caminho_cache, raiz, caminho_readme, "confirmado", ["FastAPI", "Docker"], "Tech Challenge — Fase 01")
    cache = ler_pos.carregar_cache(caminho_cache)
    assert len(cache["processados"]) == 1
    assert cache["processados"][0]["status"] == "confirmado"
    assert cache["processados"][0]["candidatos"] == ["FastAPI", "Docker"]


def test_diff_nao_repete_apos_marcar(tmp_path):
    raiz = _pos_falsa(tmp_path)
    caminho_cache = tmp_path / "cache.json"
    caminho_readme = "01_Projetos/TECH CHALLENGE/FASE 01/README.md"
    ler_pos.marcar(caminho_cache, raiz, caminho_readme, "confirmado", ["FastAPI"], "Tech Challenge — Fase 01")
    cache = ler_pos.carregar_cache(caminho_cache)
    novos, mudados = ler_pos.diff_contra_cache(raiz, cache)
    assert caminho_readme not in novos
    assert caminho_readme not in mudados


def test_cli_marcar_grava_no_arquivo(tmp_path):
    raiz = _pos_falsa(tmp_path)
    cache = tmp_path / "cache.json"
    r = subprocess.run(
        [sys.executable, str(LEITOR), "--raiz", str(raiz), "--cache", str(cache),
         "--marcar", "01_Projetos/TECH CHALLENGE/FASE 01/README.md",
         "--status", "confirmado", "--candidatos", "FastAPI, Docker",
         "--projeto", "Tech Challenge — Fase 01"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert r.returncode == 0
    dados = json.loads(cache.read_text(encoding="utf-8"))
    assert dados["processados"][0]["candidatos"] == ["FastAPI", "Docker"]
