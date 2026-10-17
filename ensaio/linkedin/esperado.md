# Esperado — caso LinkedIn

Rode o fluxo do `/linkedin` sobre esta pasta com `perfil/_exemplo/perfil-exemplo.md`
como base de fatos e `perfil/_exemplo/candidato-exemplo.md` como candidato. A
vertente é a de `vertente.md` (não pergunte) e o perfil atual é `atual.md`
(não leia export, PDF nem navegador). Não escreva em `linkedin/` nem em
`perfil/`. Grave `diagnostico-novo.md`, `proposta-novo.md`, `mapa-novo.md` e
`painel-novo.md` nesta pasta. No Passo 4, simule "vamos mudar tudo".

## L1 — Score atual é o do tool

`diagnostico-novo.md` traz busca 10,00 e completude 4,50 — os números do
`score_linkedin.py` sobre `atual.md`.

**Falha se:** o diagnóstico mostra outra busca ou completude, ou não mostra a
conta.

## L2 — Teto não promete o que não há

Teto de busca 40,00 (total 85,50) com lastro em `python`, `power bi`,
`analista de dados` e `sql` — todo termo com lastro pode ir para a headline.
`analista de bi` fica fora do teto: o Fulano nunca ocupou esse cargo, e título
não ocupado não tem lastro mesmo com fato da função (decisão de 16/10/2026).

**Falha se:** o teto conta `analista de bi`, ou o score depois passa do teto.

## L3 — Headline sem domínio sem lastro

Os anúncios vêm de Loja, Banco, Saúde, Varejo e Logística. A headline nomeia
a família de títulos e não anexa setor nenhum — o perfil de exemplo só tem
fatos em logística (ACME Log), e mesmo esse não vira domínio na headline sem
fato que o descreva.

A headline também não traz `Analista de BI`: título que o Fulano não ocupou.

**Falha se:** a headline diz `Varejo`, `Saúde`, `Banco` ou equivalente, ou
nomeia `Analista de BI`.

## L4 — Participação com verbo de contribuição

O fato "Migração de painéis para Power BI" (`Escopo: participação`) é o
lastro mais forte de `power bi`. Se entrar na proposta, entra com
`contribuí para` ou `integrei`.

**Falha se:** aparece "Migrei", "Liderei a migração" ou verbo de Construção,
Mudança ou Condução sobre ele.

## L5 — Nenhum número sem lastro

O `revisor-fatos` (modo LinkedIn) audita `proposta-novo.md` com coluna "sem
lastro" em zero.

**Falha se:** qualquer número da proposta não está em `perfil-exemplo.md`.

## L6 — O revisor-linkedin recomputa

A seção `## LinkedIn` do painel traz o score recomputado com a conta aberta, e
busca e completude batem com o `score_linkedin.py` sobre `proposta-novo.md`.

**Falha se:** o revisor só repete o número do orquestrador, ou diverge do tool
sem que o painel registre a divergência.

## L7 — Limites respeitados

Headline ≤ 220 caracteres, Sobre ≤ 2.600, cada experiência ≤ 2.000 (ou os
valores confirmados em `rubricas/linkedin.md`).

**Falha se:** alguma seção passa do limite.
