# Esperado — /sync-pos sobre `01_Projetos/projeto-exemplo`

A fixture reproduz o layout real da Pós-FIAP: o projeto fica dentro de
`01_Projetos/`, porque `tools/ler_pos.py` só classifica (e só considera
relevante) arquivo cujo primeiro componente do caminho seja `01_Projetos`,
`00_Práticas - Exercicios` ou `02_PDF's` — um arquivo solto na raiz é
ignorado, igual seria na pasta real da Pós.

Caso fixo: `tools/ler_pos.py --raiz ensaio/pos-fiap --cache <cache temporário>
--listar` deve listar, na primeira rodada:

```
[novo][projeto] 01_Projetos/projeto-exemplo/README.md
[novo][projeto] 01_Projetos/projeto-exemplo/requirements.txt
```

`--ler 01_Projetos/projeto-exemplo/README.md` deve conter as palavras `FastAPI`,
`Docker` e `PostgreSQL` — são as três stacks candidatas que o Passo 2 do
`/sync-pos` deve propor ao candidato, nível **aplicado em projeto acadêmico**.

Depois de marcar os dois arquivos com
`--marcar <arquivo> --status confirmado --candidatos "FastAPI,Docker,PostgreSQL" --projeto projeto-exemplo`
(o `--marcar` recusa rodar sem `--candidatos` e `--projeto`), uma
segunda rodada de `--listar` sobre a mesma pasta e cache deve responder
"Nada novo desde a última rodada." — é a garantia de que o cache está
funcionando e o `/sync-pos` não vai pedir validação de novo do mesmo
arquivo sem mudança.

Se qualquer um dos três comportamentos acima mudar depois de uma edição em
`tools/ler_pos.py` ou `.claude/commands/sync-pos.md`, é regressão.
