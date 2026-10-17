---
description: Constrói ou atualiza o perfil-mestre a partir do export do LinkedIn
---

Você constrói a camada de carreira do perfil-mestre — Experiência
Profissional, Formação e Competências de nível profissional. É o único
comando que escreve essa camada em `perfil/perfil-mestre.md`; a camada de
Competências estudada/aplicada na Pós-FIAP pertence ao `/sync-pos` (ver
CLAUDE.md § Fontes dos fatos) — não toque nela.

Todos os caminhos são relativos à raiz do projeto (ver `CLAUDE.md`).

Caminho do export informado pelo candidato: $ARGUMENTS

## Passo 0 — Localizar o export

Se `$ARGUMENTS` estiver vazio, procure um zip do LinkedIn na
pasta `Downloads (zip do LinkedIn)` do `perfil/candidato.md`. Se não achar, peça ao candidato que baixe em
Configurações → Privacidade de dados → Obter uma cópia dos seus dados, e
**pare**.

Rode:
```
python "tools/ler_linkedin.py" --zip CAMINHO --listar
```

Relate quais CSVs relevantes estão presentes e quais faltam. Nem todo export
traz todos — trabalhe com o que veio, não pare por causa de um ausente.

## Passo 1 — Ler o conteúdo

Para cada CSV presente, rode o leitor com `--csv NOME`. Os que mais importam:

- `Positions.csv` — cargos, empresas, datas e descrições (a fonte dos fatos)
- `Profile.csv` — nome, headline, cidade, resumo
- `Education.csv`, `Certifications.csv`, `Languages.csv`, `Learning.csv`
- `Skills.csv` — costuma trazer dezenas de itens soltos

Dois CSVs não alimentam o currículo e alimentam a candidatura. Não precisam de
validação bloco a bloco; só registre o que existe:

- `Connections.csv` — a rede. É o que o `/nova-vaga` consulta para achar quem
  o candidato conhece na empresa da vaga, com `--empresa`. Não copie o conteúdo para o
  perfil-mestre: são dados de terceiros, e o zip já fica fora do versionamento.
- `Jobs/Job Applications.csv` — o histórico de candidaturas do próprio
  LinkedIn. Compare com as pastas de `vagas/`: candidatura que está lá e não
  tem pasta aqui é um buraco no funil do `/status`. Relate; não crie pasta
  retroativa sozinho.

O LinkedIn é a **fonte única** (decisão de 14/08/2026). Não consulte
nenhuma pasta listada em `perfil/candidato.md` → Fora do sistema, para
nada — nem para conferir um número, nem para recuperar um que falte. O que não
está no export não entra no perfil, a menos que o candidato digite à mão durante a
validação.

## Passo 2 — Montar o rascunho

Para cada posição, quebre a descrição em **fatos distintos** — não em frases.
Duas frases sobre o mesmo projeto são um fato só.

Cada fato vira um bloco no formato do perfil-mestre:

```
### Fato: <título curto>
- **O que fiz:** <a ação, com o verbo real>
- **Escopo:** autoria | condução | participação
- **Escala:** <volume, usuários, praças — se houver>
- **Resultado:** <a métrica, com unidade, período e recorte exatos>
- **Stack:** <ferramentas — se houver>
- **Como sei:** <origem e data da confirmação>
- **Já usado em:** —
```

`Escopo` nasce vazio no rascunho — só o candidato sabe se a entrega foi dele, se ele
conduziu ou se fez parte. É ele que define o teto do verbo no currículo
(rubrica de escrita, "Disciplina de escopo").

E aqui está a regra que não pode ser quebrada:

> Números que vieram da descrição do LinkedIn entram como **candidatos
> não-confirmados**. Eles vieram de texto corrido, não de uma resposta do candidato.
> Marque `Como sei: candidato do LinkedIn — NÃO CONFIRMADO`.
>
> Um candidato não-confirmado **não pode ser usado em currículo**.

Agrupe as skills soltas em 3 a 5 categorias temáticas, derivadas do que
apareceu — sem categorias pré-definidas (R6).

**Eco do próprio sistema.** Se existir `linkedin/publicado.md`, compare cada
trecho de headline, Sobre e descrição de experiência do export com ele:

- **Trecho idêntico ao publicado** → foi o `/linkedin` que escreveu, a partir
  de fatos já confirmados. Não vira fato candidato.
- **Trecho diferente** → o candidato editou à mão no LinkedIn. Entra como
  candidato não confirmado, como qualquer outro.

Relate quantos trechos foram reconhecidos como eco. Sem isso, cada revisão do
LinkedIn devolveria ao perfil-mestre, como "candidato", o próprio texto do
sistema.

Se o export trouxer fato forte que não está no `publicado.md`, avise que vale
revisar o LinkedIn com `/linkedin`.

## Passo 3 — Validar com o candidato

Apresente os fatos **em blocos por cargo**, não todos de uma vez. Para cada
bloco pergunte:

1. Os números estão certos? (mostre cada um)
2. O escopo — a entrega foi sua (`autoria`), você conduziu pessoas ou a
   frente (`condução`), ou fez parte de um resultado coletivo
   (`participação`)? Grave a resposta no campo `Escopo`.
3. Falta algum fato importante que o LinkedIn não registrou?

Conforme ele confirma, troque `Como sei` para
`confirmado por <Nome do candidato.md> em DD/MM/AAAA`.

**Não avance de bloco sem resposta.** Um perfil montado sem validação é um
perfil de candidatos não-confirmados, e nenhum deles pode ser usado — o
resultado seria um sistema completo que não consegue escrever nada.

## Passo 4 — Escrever

Escreva `perfil/perfil-mestre.md`.

**Se o arquivo já existir**, é merge, não substituição:
- Fato confirmado pelo candidato **nunca** é sobrescrito pelo LinkedIn.
- Fato novo do LinkedIn entra como candidato não-confirmado.
- Fato que sumiu do LinkedIn **permanece** no perfil — o LinkedIn pode ter sido
  editado, e o fato continua verdadeiro.

Preserve os campos `Já usado em` de fatos já existentes — é o histórico de
onde cada fato apareceu.

## Passo 4.5 — Respostas de formulário

O perfil-mestre tem uma seção "Respostas de formulário" com as perguntas
eliminatórias — pretensão, modelo de trabalho, disponibilidade, inglês, CNH,
PCD. É o filtro que mais descarta candidatura, e o export do LinkedIn não
responde quase nada dela.

Liste os campos ainda em `[A CONFIRMAR]` e pergunte. Se o candidato responder, grave
com a data; se não quiser responder agora, deixe como está e siga — mas
registre no relatório, porque cada campo em branco é uma candidatura que pode
morrer no formulário.

**Nunca preencha esses campos por dedução.** Pretensão salarial deduzida do
cargo é invenção com consequência financeira.

## Passo 5 — Relatar

- Quantos fatos no total, quantos confirmados, quantos candidatos
- Quais fatos ainda estão sem métrica
- Lembrete: fatos não-confirmados não serão usados em currículo nenhum
