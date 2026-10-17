from pathlib import Path

import mercado


SNAPSHOT_EXEMPLO = """\
# Snapshot 2026-S36

### Analista de Dados Pleno — Empresa A
- Link: https://exemplo/1
- Termos: SQL, Python, Power BI

### Analista de BI Jr — Empresa B
- Link: https://exemplo/2
- Termos: sql, power bi, dbt

### Analista de Dados — Empresa C
- Link: https://exemplo/3
- Termos: SQL , Python
"""


def test_parse_conta_vagas_e_termos():
    n, contagem = mercado.parse_snapshot(SNAPSHOT_EXEMPLO)
    assert n == 3
    assert contagem["sql"] == 3
    assert contagem["python"] == 2
    assert contagem["power bi"] == 2
    assert contagem["dbt"] == 1


def test_parse_bloco_sem_termos_conta_na_amostra():
    texto = SNAPSHOT_EXEMPLO + "\n### Analista sem termos — Empresa D\n- Link: https://exemplo/4\n"
    n, contagem = mercado.parse_snapshot(texto)
    assert n == 4
    assert contagem["sql"] == 3  # o denominador cresce, a contagem do termo não


def test_formata_fracao():
    assert mercado.formata_fracao(6, 20) == "6/20"


def test_tendencia_novo_sobe_desce_estavel():
    assert mercado.tendencia(None, "6/20") == "novo"
    assert mercado.tendencia("6/20", "11/20") == "↑"    # +25 p.p.
    assert mercado.tendencia("11/20", "6/20") == "↓"    # -25 p.p.
    assert mercado.tendencia("10/20", "11/22") == "estável"  # ~0 p.p.
    assert mercado.tendencia("6/20", None) == ""


FATOS_INICIAL = """\
| termo | categoria | tendência |
|-------|-----------|-----------|
"""

FATOS_UMA_COLUNA = """\
| termo | categoria | 2026-S35 | tendência |
|-------|-----------|----------|-----------|
| sql | linguagem | 18/20 | novo |
| dbt | ferramenta | 6/20 | novo |
"""


def test_atualiza_primeira_rodada_cria_colunas():
    out = mercado.atualiza_fatos(FATOS_INICIAL, {"sql": 3, "python": 2}, 3, "2026-S36")
    assert "2026-S36" in out
    assert "| sql | ? | 3/3 | novo |" in out
    assert "| python | ? | 2/3 | novo |" in out


def test_atualiza_preserva_categoria_e_calcula_tendencia():
    out = mercado.atualiza_fatos(FATOS_UMA_COLUNA, {"sql": 20, "dbt": 11}, 22, "2026-S36")
    # categoria preservada, não vira '?'
    linha_sql = [l for l in out.splitlines() if l.startswith("| sql ")][0]
    assert "| sql | linguagem |" in linha_sql
    assert "18/20" in linha_sql and "20/22" in linha_sql
    assert linha_sql.rstrip().endswith("estável |")  # 0.90 -> 0.91
    linha_dbt = [l for l in out.splitlines() if l.startswith("| dbt ")][0]
    assert linha_dbt.rstrip().endswith("↑ |")  # 0.30 -> 0.50


def test_atualiza_termo_ausente_vira_zero():
    out = mercado.atualiza_fatos(FATOS_UMA_COLUNA, {"sql": 20}, 22, "2026-S36")
    linha_dbt = [l for l in out.splitlines() if l.startswith("| dbt ")][0]
    assert "0/22" in linha_dbt
    assert linha_dbt.rstrip().endswith("↓ |")  # 0.30 -> 0.0


def test_atualiza_termo_novo_tem_traco_nas_colunas_antigas():
    out = mercado.atualiza_fatos(FATOS_UMA_COLUNA, {"powerbi": 9}, 22, "2026-S36")
    linha = [l for l in out.splitlines() if l.startswith("| powerbi ")][0]
    assert "| powerbi | ? | — | 9/22 | novo |" == linha.rstrip()


def test_caso_ensaio_congelado():
    raiz = Path(__file__).resolve().parent.parent
    snap = (raiz / "ensaio" / "mercado" / "snapshot-congelado.md").read_text(encoding="utf-8")
    n, contagem = mercado.parse_snapshot(snap)
    assert n == 2
    assert contagem == {"sql": 2, "power bi": 2, "python": 1, "dax": 1}
    fatos = "| termo | categoria | tendência |\n|---|---|---|\n"
    out = mercado.atualiza_fatos(fatos, contagem, n, "ENSAIO")
    assert "| sql | ? | 2/2 | novo |" in out
    assert "| dax | ? | 1/2 | novo |" in out
