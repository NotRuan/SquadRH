import subprocess
import sys
import zipfile
from pathlib import Path

AQUI = Path(__file__).parent
LEITOR = AQUI / "ler_linkedin.py"


def _zip_falso(tmp_path):
    z = tmp_path / "export.zip"
    with zipfile.ZipFile(z, "w") as f:
        f.writestr("Positions.csv", "Company Name,Title,Description\nACME,Analista,Fiz X\n")
        f.writestr("Skills.csv", "Name\nPython\nSQL\n")
        f.writestr("Ad_Targeting.csv", "irrelevante\n")
    return z


def test_listar_mostra_apenas_csvs_relevantes(tmp_path):
    z = _zip_falso(tmp_path)
    r = subprocess.run(
        [sys.executable, str(LEITOR), "--zip", str(z), "--listar"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert r.returncode == 0
    assert "Positions.csv" in r.stdout
    assert "Skills.csv" in r.stdout
    assert "Ad_Targeting.csv" not in r.stdout


def test_csv_imprime_conteudo(tmp_path):
    z = _zip_falso(tmp_path)
    r = subprocess.run(
        [sys.executable, str(LEITOR), "--zip", str(z), "--csv", "Positions.csv"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert r.returncode == 0
    assert "ACME" in r.stdout


def test_csv_ausente_sai_com_erro(tmp_path):
    z = _zip_falso(tmp_path)
    r = subprocess.run(
        [sys.executable, str(LEITOR), "--zip", str(z), "--csv", "Projects.csv"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert r.returncode == 1
    assert "não encontrado" in (r.stdout + r.stderr)


def _zip_com_conexoes(tmp_path):
    """O Connections.csv real vem com um preâmbulo de 3 linhas antes do
    cabeçalho — o leitor precisa pular isso sozinho."""
    z = tmp_path / "export-conexoes.zip"
    conexoes = (
        "Notes:\n"
        '"When exporting your connection data, you may notice..."\n'
        "\n"
        "First Name,Last Name,URL,Email Address,Company,Position,Connected On\n"
        "Ana,Souza,https://x,,Cielo,Analista de Dados,10 Mar 2025\n"
        "Bruno,Lima,https://y,,XP Inc.,Product Manager,02 Jan 2024\n"
        "Carla,Dias,https://z,,Cielo S.A.,Gerente de Riscos,15 Jun 2023\n"
    )
    with zipfile.ZipFile(z, "w") as f:
        f.writestr("Connections.csv", conexoes)
        f.writestr("Positions.csv", "Company Name,Title\nACME,Analista\n")
    return z


def test_empresa_encontra_conexoes_ignorando_caixa_e_sufixo(tmp_path):
    z = _zip_com_conexoes(tmp_path)
    r = subprocess.run(
        [sys.executable, str(LEITOR), "--zip", str(z), "--empresa", "cielo"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert r.returncode == 0
    assert "Ana Souza" in r.stdout
    assert "Carla Dias" in r.stdout          # "Cielo S.A." casa com "cielo"
    assert "Bruno Lima" not in r.stdout


def test_empresa_sem_conexao_nao_e_erro(tmp_path):
    z = _zip_com_conexoes(tmp_path)
    r = subprocess.run(
        [sys.executable, str(LEITOR), "--zip", str(z), "--empresa", "Bradesco"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert r.returncode == 0
    assert "nenhuma" in r.stdout


def test_empresa_sem_connections_no_export_avisa(tmp_path):
    z = _zip_falso(tmp_path)
    r = subprocess.run(
        [sys.executable, str(LEITOR), "--zip", str(z), "--empresa", "Cielo"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert r.returncode == 1
    assert "Connections.csv" in (r.stdout + r.stderr)


def test_listar_separa_perfil_de_candidatura(tmp_path):
    z = _zip_com_conexoes(tmp_path)
    r = subprocess.run(
        [sys.executable, str(LEITOR), "--zip", str(z), "--listar"],
        capture_output=True, text=True, encoding="utf-8",
    )
    assert r.returncode == 0
    assert "[perfil]" in r.stdout
    assert "[candidatura]" in r.stdout
    assert "Connections.csv" in r.stdout
