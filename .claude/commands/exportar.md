---
description: Gera .docx e .pdf a partir do currículo aprovado, com verificação de uma página real
---

Você exporta um currículo já aprovado. O `.md` é a fonte da verdade; `.docx` e
`.pdf` são derivados regeneráveis (R5).

Todos os caminhos são relativos à raiz do projeto (ver `CLAUDE.md`).

Pasta da vaga (ou vazio para a mais recente): $ARGUMENTS

## Passo 0 — Localizar

Se `$ARGUMENTS` estiver vazio, use a pasta de vaga mais recente em `vagas/` —
pelo prefixo de data no nome. Ignore arquivos soltos como
`vagas/_modelo-status.md`, e nunca use `base/` nem `ensaio/`: não são
candidaturas. Leia o `curriculo.md` da pasta escolhida.

## Passo 1 — Trava de placeholder

Procure `[FALTA MÉTRICA]` no texto. Se houver:

> Pare, liste onde está cada um, e pergunte se o candidato quer exportar assim mesmo.
> Só siga com um "sim" explícito.

## Passo 2 — Trava de bloqueio

Leia o `painel.md` da mesma pasta. Se houver item **BLOQUEIA** sem resolução
registrada, pare e reporte. Não exporte por cima de um bloqueio.

Item de BLOQUEIA é qualquer linha da seção diferente de `- nenhum`. Painéis
anteriores a 16/10/2026 podem trazer confirmações dentro da seção ("idêntico
em todos", "coluna única, conforme"): leia o conteúdo antes de travar — o que
afirma conformidade não é bloqueio.

Se não existir `painel.md`, avise que este currículo nunca passou pelo painel e
pergunte se deve seguir mesmo assim.

Confira também a **re-auditoria de fatos** registrada no fim do `painel.md`
(Passo 7.5 do `/nova-vaga`). Se as correções foram aplicadas e a re-auditoria
não consta, avise: o documento que vai ser exportado é o de depois, e ele pode
não ter sido auditado.

## Passo 3 — Gerar o .docx

Use a skill `anthropic-skills:docx`. Regras de formato (rubrica ATS):

- Coluna única. Sem tabelas, caixas de texto, colunas ou imagens.
- Sem cabeçalho e sem rodapé.
- Bullets como lista real do Word (`numbering`), nunca o caractere `•`
  digitado.
- Papel A4, não US-Letter.
- Nome em destaque; seções em caixa alta; corpo em 10-11pt.
- Margens de 1,5 cm a 2 cm — é o que permite uma página sem apertar a fonte.

Salve como `curriculo.docx` na pasta da vaga.

## Passo 4 — Gerar o .pdf

Converta com o `soffice.py` que a própria skill `docx` traz embutido (não há
LibreOffice solto no PATH). Salve como `curriculo.pdf` na mesma pasta.

## Passo 5 — Verificar uma página de verdade

Rode:
```
python "tools/contar_paginas.py" "CAMINHO/curriculo.pdf" --max 1
```

- Saída `0` → pronto.
- Saída `1` → **não** encolha a fonte para caber. Reporte ao candidato o que sobrou e
  proponha cortes concretos, na ordem: bullets mais fracos do cargo mais
  antigo, depois competências menos relevantes para a vaga, depois a terceira
  linha do resumo. Espere a decisão dele.
- Saída `2` → o PDF não foi gerado corretamente; investigue antes de seguir.

**O corte acontece no `.md`, nunca no `.docx`.** O markdown é a fonte da
verdade (R5): corte lá e regenere os dois derivados, senão a próxima exportação
traz o texto cortado de volta.

## Passo 6 — Checklist de envio

O currículo é só metade da candidatura. O que mais elimina candidato não está
no documento — está no formulário, e nenhum revisor do painel o enxerga.

Antes de fechar, apresente:

**Qual arquivo enviar.** Aceitando os dois, envie o `.docx` — parseia melhor
que o PDF (rubrica ATS, "Qual arquivo enviar"). PDF quando o formulário só
aceitar PDF, ou quando for anexo direto a uma pessoa.

**As perguntas eliminatórias.** Releia o `vaga.md` e liste as que ela sinaliza
— pretensão, modelo de trabalho, disponibilidade, inglês, formação, CNH, PCD.
Para cada uma, traga a resposta da seção "Respostas de formulário" do
`perfil-mestre.md`.

- Campo `[A CONFIRMAR]` que a vaga pede: **avise**. É onde a candidatura morre
  em silêncio, e é a resposta do candidato, não sua — nunca preencha pretensão
  salarial, disponibilidade ou faixa por conta própria.
- Se ele responder agora, grave no `perfil-mestre.md` com a data. Vale para
  todas as vagas seguintes.

**A indicação.** Se o Passo 1.6 do `/nova-vaga` achou conexões na empresa e o
`status.md` marca `Indicação pedida: não`, lembre — falar com alguém de dentro
antes de enviar pelo portal muda a ordem de grandeza da resposta.

**O status.** Confirme que o `status.md` da pasta existe. Se `Canal` ou
`Data da candidatura` estiverem vazios, `A PREENCHER` ou `[A CONFIRMAR]`,
**pergunte agora, numa pergunta só**: "Por onde vai enviar (portal, LinkedIn,
indicação, recrutador, site da empresa) e em que data?" — e grave a resposta
no `status.md`. Data não informada: grave a de hoje e diga que assumiu.

É o momento certo de perguntar porque é o único em que a resposta é óbvia para
quem envia. Lembrar disso depois não acontece: na primeira busca, o `Canal`
ficou vazio em 27 de 37 candidaturas, e o `/status` não teve o que cruzar.

Feche lembrando que o retorno se registra com `/resultado empresa resultado`.

## Passo 7 — Relatar

Diga onde ficaram os arquivos e quantas páginas o PDF tem.

Lembre que `.docx` e `.pdf` estão no `.gitignore` — se ele quiser guardar uma
versão enviada, deve copiá-la para fora da pasta do projeto.
