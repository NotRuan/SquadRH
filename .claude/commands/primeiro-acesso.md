---
description: Primeiro acesso — configura o candidato e constrói o perfil-mestre do zero
---

Você recebe uma pessoa nova no squad e constrói a base de tudo: a
configuração (`perfil/candidato.md`) e o perfil-mestre. Nenhum outro comando
funciona sem os dois.

Todos os caminhos são relativos à raiz do projeto (ver `CLAUDE.md`).

## Passo 0 — Onde estamos

- `perfil/candidato.md` não existe → comece do Passo 1.
- Existe, mas `perfil/perfil-mestre.md` não existe ou não tem nenhum fato com
  `Como sei: confirmado por` → diga que vai retomar a construção do perfil e
  vá ao Passo 3.
- Os dois existem e há fato confirmado → diga que o perfil já existe, ofereça
  `/sync-perfil` para atualizar e **pare**.

## Passo 1 — Boas-vindas

Em até cinco linhas:
- O squad escreve currículos orientados a vaga, modela o LinkedIn e acompanha
  as candidaturas.
- A regra que vence tudo: **nada é inventado**. Todo número, empresa e
  ferramenta vem do que a pessoa confirmar.
- O que vem agora: alguns dados, depois os fatos da carreira, validados um a um.

## Passo 2 — Dados e preferências

Pergunte numa rodada só: nome, como prefere ser chamado, tom (direto ou
formal), nível de detalhe (curto ou completo), vertente-alvo com os títulos da
família, senioridade, anos de experiência formal, pasta de Downloads, pasta de
estudos (opcional). Contato (cidade, telefone, e-mail, LinkedIn, GitHub) vai
para o perfil-mestre, seção "Dados de contato".

Grave `perfil/candidato.md` no formato de `perfil/_exemplo/candidato-exemplo.md`.
`Limite de páginas do currículo`: 1 até ~8 anos de experiência formal, 2
acima. `/mercado` nasce desligado; `/sync-pos` ligado só se houver pasta de
estudos.

## Passo 3 — De onde vêm os fatos

Pergunte (pode combinar):

1. **Export do LinkedIn** — siga o fluxo do `/sync-perfil` inteiro, que já
   valida bloco a bloco.
2. **Currículo existente** (PDF ou DOCX) — leia com `Read` (PDF) ou com a skill
   `anthropic-skills:docx` (DOCX). Quebre cada cargo em fatos distintos, no
   formato de bloco do `/sync-perfil` (Passo 2), com
   `Como sei: currículo importado — NÃO CONFIRMADO`.
3. **Entrevista guiada** — cargo a cargo: empresa, título, datas; para cada
   entrega, o que fez, escala, resultado (com unidade, período e recorte) e o
   `Escopo` — a entrega foi sua (`autoria`), você conduziu pessoas ou a
   frente (`condução`), ou fez parte de um resultado coletivo
   (`participação`)?

Fonte 2 que contradiz fonte 1 (datas, cargo, número): mostre os dois e
pergunte. Nunca escolha sozinho.

## Passo 4 — Validar

Apresente os fatos **um cargo por vez**. Para cada fato: o número está certo?
o escopo está certo? falta algo? Ao confirmar, troque `Como sei` para
`confirmado por <Nome> em DD/MM/AAAA`. **Não avance de cargo sem resposta.**

Grave `perfil/perfil-mestre.md` com: título, "Dados de contato", um bloco
`## <Empresa> — <Cargo> (<início> – <fim>)` por cargo com seus fatos,
"Formação acadêmica", "Certificações", "Idiomas", "Competências" (agrupadas em
3 a 5 categorias derivadas do que apareceu — R6) e "Respostas de formulário".

## Passo 5 — Respostas de formulário (opcional)

Pretensão salarial, modelo de trabalho, disponibilidade, inglês, CNH, PCD.
Pergunte; o que a pessoa não quiser responder fica `[A CONFIRMAR]`. **Nunca
preencha por dedução.**

## Passo 6 — Fechar

Relate: fatos confirmados, fatos sem métrica, campos de formulário em aberto.
Sugira o próximo passo: `/linkedin` para modelar o perfil para a vertente, ou
`/nova-vaga` se já houver uma vaga em vista.

## Regras

- R1 inteiro: o que a pessoa não confirmou não é fato.
- As pastas em `candidato.md` → Fora do sistema nunca são lidas.
- Português do Brasil; tom e detalhe do `candidato.md` assim que ele existir.
