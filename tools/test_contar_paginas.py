import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).parent
CONTADOR = AQUI / "contar_paginas.py"

PDF_UMA_PAGINA = (
    b"%PDF-1.4\n"
    b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n"
    b"2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n"
    b"3 0 obj\n<< /Type /Page /Parent 2 0 R >>\nendobj\n"
    b"trailer\n<< /Root 1 0 R >>\n%%EOF\n"
)

PDF_DUAS_PAGINAS = PDF_UMA_PAGINA.replace(b"/Count 1", b"/Count 2")


def _grava(tmp_path, dados, nome="cv.pdf"):
    p = tmp_path / nome
    p.write_bytes(dados)
    return p


def test_uma_pagina_passa(tmp_path):
    p = _grava(tmp_path, PDF_UMA_PAGINA)
    r = subprocess.run(
        [sys.executable, str(CONTADOR), str(p), "--max", "1"],
        capture_output=True, text=True,
    )
    assert r.returncode == 0
    assert "1" in r.stdout


def test_duas_paginas_falha(tmp_path):
    p = _grava(tmp_path, PDF_DUAS_PAGINAS)
    r = subprocess.run(
        [sys.executable, str(CONTADOR), str(p), "--max", "1"],
        capture_output=True, text=True,
    )
    assert r.returncode == 1


def test_arquivo_invalido_sai_2(tmp_path):
    p = _grava(tmp_path, b"isso nao e um pdf")
    r = subprocess.run(
        [sys.executable, str(CONTADOR), str(p), "--max", "1"],
        capture_output=True, text=True,
    )
    assert r.returncode == 2
    # Sem esta checagem o teste passa pelo motivo errado: o proprio Python
    # devolve 2 quando o script nao existe.
    assert "não é um PDF" in (r.stdout + r.stderr)


def test_pdf_sem_count_sai_2(tmp_path):
    p = _grava(tmp_path, b"%PDF-1.4\ntrailer\n<< /Root 1 0 R >>\n%%EOF\n")
    r = subprocess.run(
        [sys.executable, str(CONTADOR), str(p), "--max", "1"],
        capture_output=True, text=True,
    )
    assert r.returncode == 2
    assert "Count" in (r.stdout + r.stderr)


def test_arvore_aninhada_usa_o_count_da_raiz(tmp_path):
    # PDFs com arvore de paginas aninhada trazem varios /Count; o da raiz e o
    # maior, porque soma os filhos. Um /Count 1 de um no folha nao pode
    # mascarar um documento de 3 paginas.
    aninhado = (
        b"%PDF-1.4\n"
        b"1 0 obj\n<< /Type /Pages /Kids [2 0 R 3 0 R] /Count 3 >>\nendobj\n"
        b"2 0 obj\n<< /Type /Pages /Count 1 >>\nendobj\n"
        b"3 0 obj\n<< /Type /Pages /Count 2 >>\nendobj\n"
        b"%%EOF\n"
    )
    p = _grava(tmp_path, aninhado)
    r = subprocess.run(
        [sys.executable, str(CONTADOR), str(p), "--max", "1"],
        capture_output=True, text=True,
    )
    assert r.returncode == 1
    assert "3" in r.stdout
