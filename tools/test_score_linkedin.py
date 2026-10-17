import re
import subprocess
import sys
from pathlib import Path

import pytest

import score_linkedin as sl

AQUI = Path(__file__).parent
SCRIPT = AQUI / "score_linkedin.py"

VERTENTE = """\
# Vertente

- **Nome:** Dados & BI
- **Títulos:** Analista de Dados, Analista de BI

## Anúncios

### Analista de Dados Pleno — Empresa A
- Termos: SQL, Python, Power BI

### Analista de BI — Empresa B
- Termos: sql, power bi, dbt

### Analista de Dados Jr — Empresa C
- Termos: SQL, Python

### Analista de Analytics — Empresa D
- Termos: sql, excel
"""

PERFIL = """\
# Perfil LinkedIn — atual

## Headline
Analista de Dados | SQL · Python

## Sobre
Trabalho com Power BI e automação.

## Experiência

### Analista de Dados — ACME (jan/2025 – atual)
Construí painéis em Power BI.

## Competências
- Fixadas: SQL, Python, Excel

## Completude
- [x] foto
- [ ] banner
- [x] url personalizada
- [x] localidade
- [x] formação
- [x] idiomas
"""


def test_titulos_normalizados():
    assert sl.titulos(VERTENTE) == ["analista de dados", "analista de bi"]


def test_recorrentes_em_metade_dos_anuncios_mais_titulos():
    # 4 anúncios: sql 4, python 2, power bi 2, dbt 1, excel 1 → corte em 2
    assert sl.termos_recorrentes(VERTENTE) == [
        "analista de bi", "analista de dados", "power bi", "python", "sql",
    ]


def test_parse_perfil_secoes_e_completude():
    p = sl.parse_perfil(PERFIL)
    assert p["headline"] == "analista de dados | sql · python"
    assert "power bi" in p["experiencia"]
    assert p["completude"]["formacao"] is True
    assert p["completude"]["banner"] is False


def test_peso_pela_melhor_secao():
    p = sl.parse_perfil(PERFIL)
    assert sl.peso_termo("SQL", p) == 2.0          # headline vence competências
    assert sl.peso_termo("power bi", p) == 1.0     # só sobre/experiência
    assert sl.peso_termo("analista de bi", p) == 0.0
    assert sl.peso_termo("Automação", p) == 1.0    # sem acento casa com acento


def test_termo_nao_casa_dentro_de_outra_palavra():
    p = sl.parse_perfil("## Headline\nSQLite e Pythonista\n")
    assert sl.peso_termo("sql", p) == 0.0
    assert sl.peso_termo("python", p) == 0.0


def test_score_busca_conta_aberta():
    p = sl.parse_perfil(PERFIL)
    termos = sl.termos_recorrentes(VERTENTE)
    # 0 + 2 + 1 + 2 + 2 = 7 de 10 possíveis → 35
    assert sl.score_busca(termos, p) == 35.0


def test_score_completude():
    p = sl.parse_perfil(PERFIL)
    assert sl.score_completude(p["completude"]) == 7.5   # 5 itens × 1,5


def test_total_e_limites():
    assert sl.total(35.0, 10, 9, 7.5) == 61.5
    with pytest.raises(ValueError):
        sl.total(35.0, 21, 9, 7.5)
    with pytest.raises(ValueError):
        sl.total(35.0, 10, 16, 7.5)


def test_busca_teto_nunca_abaixo_do_atual():
    p = sl.parse_perfil(PERFIL)
    termos = sl.termos_recorrentes(VERTENTE)
    lastro = {"sql", "python", "power bi", "analista de dados"}
    # todo termo com lastro pode ir para a headline (2): 4 × 2 = 8 de 10 → 40
    assert sl.busca_teto(termos, sl.titulos(VERTENTE), lastro, p) == 40.0


def test_busca_teto_nunca_abaixo_do_depois():
    # o teto é o melhor arranjo possível: nenhum perfil que só use termos com
    # lastro pode passar dele — foi a falha L2 do ensaio de 16/10/2026
    termos = sl.termos_recorrentes(VERTENTE)
    lastro = {"sql", "python", "power bi", "analista de dados"}
    atual = sl.parse_perfil("## Headline\nProfissional de dados\n")
    depois = sl.parse_perfil("## Headline\nAnalista de Dados | SQL · Python · Power BI\n")
    teto = sl.busca_teto(termos, sl.titulos(VERTENTE), lastro, atual)
    assert sl.score_busca(termos, depois) <= teto


def test_completude_teto():
    p = sl.parse_perfil(PERFIL)
    # 6 de configuração + em destaque (lastro) + formação e idiomas (já marcados)
    assert sl.completude_teto(["em destaque"], p["completude"]) == 13.5


def _arquivos(tmp_path):
    v = tmp_path / "vertente.md"
    v.write_text(VERTENTE, encoding="utf-8")
    pf = tmp_path / "atual.md"
    pf.write_text(PERFIL, encoding="utf-8")
    return v, pf


def test_cli_score(tmp_path):
    v, pf = _arquivos(tmp_path)
    r = subprocess.run(
        [sys.executable, str(SCRIPT), "score", "--vertente", str(v), "--perfil", str(pf),
         "--abertura", "10", "--prova", "9"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert r.returncode == 0, r.stderr
    assert re.search(r"busca\s+35,00 / 50", r.stdout)
    assert re.search(r"completude\s+7,50 / 15", r.stdout)
    assert re.search(r"total\s+61,50 / 100", r.stdout)


def test_cli_teto(tmp_path):
    v, pf = _arquivos(tmp_path)
    r = subprocess.run(
        [sys.executable, str(SCRIPT), "teto", "--vertente", str(v), "--perfil", str(pf),
         "--lastro", "sql,python,power bi,analista de dados", "--itens", "em destaque",
         "--abertura", "20", "--prova", "15"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert r.returncode == 0, r.stderr
    assert re.search(r"total\s+88,50 / 100", r.stdout)   # 40 + 20 + 15 + 13,5
