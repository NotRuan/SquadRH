---
description: Lê projetos, práticas e e-books da Pós-FIAP e atualiza as Competências do perfil-mestre
---

Você constrói a camada de Competências estudada/aplicada na Pós-FIAP do
perfil-mestre. É o único comando que escreve essa camada em
`perfil/perfil-mestre.md`; a camada de carreira (Experiência Profissional,
Formação, Competências de nível profissional) pertence ao `/sync-perfil` —
não toque nela.

Todos os caminhos são relativos à raiz do projeto (ver `CLAUDE.md`), exceto a
pasta de estudos em si, que fica fora do repositório e é lida do
`perfil/candidato.md`.

Pasta de estudos: a `Pasta de estudos (opcional)` do `perfil/candidato.md`.
Vazia ou módulo `/sync-pos` desligado: diga isso e pare.
Cache: `perfil/pos-fiap-cache.json`

## Passo 0 — O que mudou desde a última rodada

Rode:
```
python tools/ler_pos.py --raiz "<Pasta de estudos do candidato.md>" --cache perfil/pos-fiap-cache.json --listar
```

Cada linha vem marcada `[novo]` ou `[mudado]`, e classificada `[projeto]` ou
`[ebook]`. Se a saída for "Nada novo desde a última rodada.", relate isso ao
candidato e **pare** — não há o que processar.

## Passo 1 — Ler cada fonte nova

**Qualquer arquivo `.pdf`** — esteja marcado `[projeto]` (guia/planejamento
dentro de `01_Projetos/`) ou `[ebook]` (dentro de `02_PDF's/`) — leia com a
ferramenta `Read`, em blocos de até 20 páginas por chamada, até cobrir todas
as páginas. **Nunca** passe um `.pdf` para `--ler`: o script não extrai texto
de binário e vai recusar (`ArquivoBinarioError`) — é o comportamento
correto, não um bug a contornar. Extraia toda tecnologia/ferramenta central
ao conteúdo — não cite de passagem uma ferramenta mencionada uma única vez
num parágrafo lateral.

Para as demais linhas `[projeto]` (`README.md`, `requirements.txt`,
`pyproject.toml`, `.ipynb`):
```
python tools/ler_pos.py --raiz "<Pasta de estudos do candidato.md>" --cache perfil/pos-fiap-cache.json --ler "CAMINHO_RELATIVO"
```
Para `README.md`/`requirements.txt`/`pyproject.toml`, imprime o texto bruto.
Para notebook (`.ipynb`), imprime os módulos importados, um por linha
(`import: pandas`). Extraia candidatos a stack do que aparecer.

**Não pule arquivo.** Um e-book grande custa mais chamadas de `Read`, não
menos leitura.

## Passo 2 — Montar candidatos

Agrupe os arquivos pelo projeto/e-book a que pertencem (ex.: `README.md` +
`requirements.txt` + notebook do mesmo Tech Challenge são um só grupo). Para
cada grupo, monte a lista de stacks candidatas, com o nível:

- Arquivo `[projeto]` → nível **aplicado em projeto acadêmico**
- Arquivo `[ebook]` → nível **estudado**

Agrupe as stacks por categoria temática do jeito que a seção Competências do
perfil-mestre.md já agrupa hoje (Dados & SQL, Big data, BI & visualização,
etc.) — sem lista fixa de categorias (R6).

## Passo 3 — Validar com o candidato

Apresente **um projeto ou um e-book por vez**, nunca tudo de uma vez. Para
cada grupo pergunte:

1. As stacks candidatas estão certas, ou alguma é ruído (menção de
   passagem)?
2. O nível está certo (estudado vs. aplicado em projeto acadêmico)?
3. Falta alguma stack que a extração automática não pegou?

**Não avance de grupo sem resposta.**

## Passo 4 — Escrever

Para cada stack confirmada, adicione ou atualize um item na seção
Competências do `perfil/perfil-mestre.md`, seguindo o formato de anotação já
usado ali (ver o item `PySpark, SparkSQL` como exemplo real):

```
- **<Categoria>:** ..., <Stack>, ...
  - `<Stack>: origem Pós-FIAP (<projeto ou e-book>), nível <estudado |
    aplicado em projeto acadêmico>. Confirmado por <Nome do candidato.md> em DD/MM/AAAA.
    <estudado → não sustenta bullet de experiência/resultado; aplicado →
    sustenta bullet desde que descreva o projeto acadêmico, não emprego>`
```

Não toque em nenhum item marcado como nível profissional — esses são do
`/sync-perfil`.

Depois de escrever, marque cada arquivo processado no cache, um por vez:
```
python tools/ler_pos.py --raiz "<Pasta de estudos do candidato.md>" --cache perfil/pos-fiap-cache.json --marcar "CAMINHO_RELATIVO" --projeto "Nome do projeto/e-book" --status confirmado --candidatos "Stack A,Stack B"
```
Se o candidato não terminou de validar um grupo nesta sessão, marque com
`--status pendente_validacao` em vez de `confirmado` — a próxima rodada
retoma dali sem reler o arquivo.

## Passo 5 — Relatar

- Quantos arquivos novos/mudados foram processados
- Quantas stacks confirmadas, quantas rejeitadas como ruído
- Quais grupos ficaram `pendente_validacao`
- Lembrete: nível estudado nunca sustenta bullet de experiência no
  `/nova-vaga`
