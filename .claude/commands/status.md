---
description: Consolida o funil de candidaturas e a cobertura de fatos do perfil
---

Você lê tudo que já foi enviado e responde uma pergunta que nenhum outro
comando responde: **isto está funcionando?**

Todos os caminhos são relativos à raiz do projeto (ver `CLAUDE.md`).

Filtro opcional (empresa, mês, canal ou resultado): $ARGUMENTS

## Passo 0 — Ler

Leia todo `vagas/*/status.md`. Ignore `vagas/_modelo-status.md`, `base/` e
`ensaio/`.

Se `$ARGUMENTS` trouxer um filtro, aplique-o — mas **sempre reporte o total
também**, para o filtro não esconder o tamanho da amostra.

## Passo 1 — O funil

```
vagas analisadas            N
  descartadas               N   (pararam antes do envio — teto de aderência; não são enviadas)
candidaturas enviadas       N
  aguardando                N   (menos de 30 dias, sem resposta ainda)
  sem resposta              N   (mais de 30 dias)
  encerrada                 N   (funil fechado por decisão — ex.: proposta aceita; fora do denominador das taxas)
  rejeitado                 N
  triagem                   N
  entrevista                N
  teste                     N
  proposta                  N
```

Calcule e mostre:

- **Base das taxas** = enviadas − encerradas. `descartada` nunca entra em
  enviadas; `encerrada` sai da base porque o funil foi fechado antes de haver
  resposta, e contá-la como "sem resposta" ou como "respondeu" mente nos dois
  sentidos.
- **Taxa de resposta** = (rejeitado + triagem + entrevista + teste + proposta +
  recusei) / base
- **Taxa de entrevista** = (entrevista + teste + proposta) / base
- **Mediana de dias até a primeira resposta** — mediana, não média: uma resposta
  em 45 dias distorce a média de dez respostas em 5.

**Declare a amostra junto com toda taxa.** "1 de 21" e "5%" são a mesma
informação, mas a primeira diz também o quanto se pode confiar nela. Com menos
de 20 candidaturas respondidas, diga explicitamente que o número ainda não
sustenta conclusão.

## Passo 2 — O que separa quem respondeu

Só faça este passo se houver **pelo menos 5 candidaturas com resultado**.
Abaixo disso, diga que ainda não há amostra e pule — cruzamento em cima de 3
casos é leitura de borra de café, e vai fazer o candidato mudar o currículo pela razão
errada.

Havendo amostra, compare respondidas vs não respondidas em:

- **Canal** — portal, indicação, recrutador. É o corte que mais separa: os
  benchmarks de mercado põem indicação em outra ordem de grandeza que portal.
- **Score ATS final** — a média das que responderam é diferente da média das
  que não responderam?
- **Teto de aderência**
- **Senioridade do cargo** (júnior, pleno, sênior)

Reporte só o que mostra diferença. Um corte que não separa nada é achado
válido: "score não separou respondidas de não respondidas nesta amostra" é
informação útil, e poupa o candidato de otimizar o que não importa.

## Passo 3 — Cobertura de fatos

Leia `perfil/perfil-mestre.md` e o campo `Já usado em` de cada fato.

```
fatos no perfil             N
  confirmados               N
  candidatos não-confirmados N   (não podem ser usados)
  sem métrica               N   ([FALTA MÉTRICA] no Resultado)
  nunca usados em vaga      N
```

Liste, pelo nome:

1. **Fatos ociosos** — confirmados, com métrica, e nunca usados. Cada um é um
   argumento pronto que nunca foi ao mercado.
2. **Fatos saturados** — usados em 4 ou mais candidaturas. Não é problema, mas
   se um deles aparece em toda vaga e a taxa de resposta é baixa, é o candidato
   natural para um teste.
3. **Fatos travados** — candidatos não-confirmados e fatos sem métrica. Para
   cada um, a pergunta exata que destravaria. Estes são a maior fonte de valor
   parado do sistema: um número que o candidato confirma em 30 segundos passa a poder
   ser usado em todas as vagas seguintes.

## Passo 4 — Pendências

- `status.md` com campos `A PREENCHER` — liste as pastas. São candidaturas cujo
  resultado nunca foi registrado, e cada uma é um buraco no funil. Para cada
  uma, mostre a linha pronta para o usuário fechar: `/resultado empresa ...`.
- `Canal` vazio, `A PREENCHER` ou `[A CONFIRMAR]` — liste à parte. É o corte
  que mais separa no Passo 2, e sem ele o Passo 2 não tem o que cruzar.
- Vagas sem `status.md`, ou sem `curriculo.md`/`painel.md` e sem resultado
  `descartada` — fluxo abandonado no meio.
- Candidaturas `aguardando` há mais de 30 dias — devem virar `sem resposta`.
- Mais de uma candidatura à mesma empresa em menos de 15 dias.

## Passo 5 — Uma recomendação, só

Feche com **uma** ação, a de maior retorno, e diga por que ela e não outra.

Se a amostra não sustenta recomendação, a recomendação é preencher os
`status.md` pendentes. Não invente conclusão para ter o que dizer — este
comando existe para medir, e um comando de medição que inventa é pior que
nenhum.

## Regras

- **Você não edita nada** além de responder. Não altere `status.md`, currículo
  ou perfil. Se o candidato disser o resultado de uma candidatura durante a conversa,
  aí sim grave no `status.md` dela.
- Toda taxa vem com a fração que a gerou.
- Português do Brasil.
