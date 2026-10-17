# Comportamento esperado do caso de mercado

Partindo de um `fatos-mercado.md` vazio (só cabeçalho), rodar o tool com este
snapshot na coluna `ENSAIO` deve produzir uma tabela onde:

- `n_vagas` = 2
- `sql` = 2/2 (novo)
- `power bi` = 2/2 (novo)
- `python` = 1/2 (novo)
- `dax` = 1/2 (novo)

A asserção vive em `tools/test_mercado.py::test_caso_ensaio_congelado` e roda
com `python -m pytest tools/test_mercado.py -v`.
