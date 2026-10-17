import subprocess
import sys
from datetime import date
from pathlib import Path

import recepcao

AQUI = Path(__file__).parent
SCRIPT = AQUI / "recepcao.py"
HOJE = date(2026, 10, 16)

CANDIDATO = """\
# Candidato
- **Nome:** Fulano de Exemplo
- **Como chamar:** Fulano
- **Pasta de estudos (opcional):**
- **/sync-pos:** desligado
"""

PERFIL_CONFIRMADO = "### Fato: X\n- **Como sei:** confirmado por Fulano em 01/01/2026\n"


def _raiz(tmp_path, candidato=True, perfil=None):
    (tmp_path / "perfil").mkdir()
    (tmp_path / "vagas").mkdir()
    if candidato:
        (tmp_path / "perfil" / "candidato.md").write_text(CANDIDATO, encoding="utf-8")
    if perfil is not None:
        (tmp_path / "perfil" / "perfil-mestre.md").write_text(perfil, encoding="utf-8")
    return tmp_path


def _status(raiz, pasta, resultado, data):
    d = raiz / "vagas" / pasta
    d.mkdir()
    (d / "status.md").write_text(
        f"- **Data da candidatura:** {data}\n- **Resultado:** {resultado}\n", encoding="utf-8")


def test_ler_campos():
    c = recepcao.ler_campos(CANDIDATO)
    assert c["Como chamar"] == "Fulano"
    assert c["Pasta de estudos (opcional)"] == ""


def test_estado_novo_sem_candidato(tmp_path):
    assert recepcao.estado(_raiz(tmp_path, candidato=False)) == "novo"


def test_estado_construcao_sem_fato_confirmado(tmp_path):
    raiz = _raiz(tmp_path, perfil="### Fato: X\n- **Como sei:** NÃO CONFIRMADO\n")
    assert recepcao.estado(raiz) == "construcao"


def test_estado_construcao_sem_perfil(tmp_path):
    assert recepcao.estado(_raiz(tmp_path)) == "construcao"


def test_estado_pronto(tmp_path):
    assert recepcao.estado(_raiz(tmp_path, perfil=PERFIL_CONFIRMADO)) == "pronto"


def test_situacao_conta_retornos_em_aberto_e_atrasados(tmp_path):
    raiz = _raiz(tmp_path, perfil=PERFIL_CONFIRMADO)
    _status(raiz, "2026-08-01-a-cargo", "aguardando", "2026-08-01")   # 76 dias
    _status(raiz, "2026-10-10-b-cargo", "aguardando", "2026-10-10")   # 6 dias
    _status(raiz, "2026-08-02-c-cargo", "encerrada — proposta aceita", "2026-08-02")
    _status(raiz, "2026-08-03-d-cargo", "A PREENCHER", "2026-08-03")  # 74 dias
    linhas = recepcao.situacao(raiz, HOJE)
    assert any("3 candidatura(s) com retorno em aberto" in l and "2 há mais de 30 dias" in l
               for l in linhas)


def test_situacao_linkedin_nao_modelado(tmp_path):
    raiz = _raiz(tmp_path, perfil=PERFIL_CONFIRMADO)
    assert any("/linkedin" in l and "ainda não modelado" in l
               for l in recepcao.situacao(raiz, HOJE))


def test_situacao_linkedin_antigo(tmp_path):
    raiz = _raiz(tmp_path, perfil=PERFIL_CONFIRMADO)
    (raiz / "linkedin").mkdir()
    (raiz / "linkedin" / "publicado.md").write_text(
        "- **Publicado em:** 2026-06-01\n", encoding="utf-8")
    assert any("137 dias" in l for l in recepcao.situacao(raiz, HOJE))


def test_situacao_linkedin_recente_nao_aparece(tmp_path):
    raiz = _raiz(tmp_path, perfil=PERFIL_CONFIRMADO)
    (raiz / "linkedin").mkdir()
    (raiz / "linkedin" / "publicado.md").write_text(
        "- **Publicado em:** 2026-10-01\n", encoding="utf-8")
    assert not any("linkedin" in l.lower() for l in recepcao.situacao(raiz, HOJE))


def test_contexto_pronto_traz_nome_e_instrucao(tmp_path):
    raiz = _raiz(tmp_path, perfil=PERFIL_CONFIRMADO)
    txt = recepcao.contexto(raiz, HOJE)
    assert txt.startswith("[Recepção do squad de RH]")
    assert "Estado: pronto" in txt
    assert "Candidato: Fulano" in txt
    assert ".claude/commands/inicio.md" in txt


def test_cli_nunca_falha(tmp_path):
    r = subprocess.run(
        [sys.executable, str(SCRIPT), "--raiz", str(tmp_path / "nao-existe"), "--hoje", "2026-10-16"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert r.returncode == 0
    assert "Estado: novo" in r.stdout


def test_cli_hook_emite_json_de_sessionstart(tmp_path):
    import json
    raiz = _raiz(tmp_path, perfil=PERFIL_CONFIRMADO)
    r = subprocess.run(
        [sys.executable, str(SCRIPT), "--raiz", str(raiz), "--hoje", "2026-10-16", "--hook"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert r.returncode == 0
    saida = json.loads(r.stdout)
    assert saida["hookSpecificOutput"]["hookEventName"] == "SessionStart"
    assert "Estado: pronto" in saida["hookSpecificOutput"]["additionalContext"]
