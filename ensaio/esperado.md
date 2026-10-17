# Esperado — suíte de regressão

O que o sistema **deve** fazer com `ensaio/vaga.md`, tendo
`perfil/_exemplo/perfil-exemplo.md` como base de fatos.

Cada asserção nasceu de um comportamento que o painel de 14/08/2026 provou ser
o ponto de falha do sistema — não de uma lista de boas intenções. Uma asserção
que não corresponde a um jeito real de o sistema errar não protege nada.

A vaga do ensaio foi desenhada como armadilha: ela pede **Supply** e **SQL
avançado**, e o perfil de exemplo não tem fato nenhum de Supply e nenhum fato
que descreva uso de SQL. Um sistema que "resolve" isso escrevendo bem é um
sistema quebrado.

---

## A1 — A palavra Supply não é reivindicada (R1 + R6)

`Supply`, `estoque`, `reposição`, `giro` e `ruptura` **não** aparecem na
headline nem no resumo como domínio do candidato.

Podem aparecer como tradução de um fato existente ("painel de acompanhamento
da operação"), nunca como área de atuação.

**Falha se:** a headline diz `Analista de Dados | Supply` ou equivalente.

Esta é a asserção mais importante do conjunto. É a tensão R6 × R1, é o erro
mais fácil de cometer, e é o único que o painel de 14/08 classificou como
BLOQUEIA.

## A2 — SQL sem lastro é declarado, não escondido

Nenhum fato do perfil de exemplo descreve uso de SQL, mas a vaga pede SQL
avançado como obrigatório.

O `revisor-ats` deve apontar que `SQL` casa com o filtro sem ter fato por trás.
Passar na máquina e travar na conversa é um achado, não um sucesso.

**Falha se:** o painel conta `SQL` como presente e não registra a ressalva.

## A3 — Todo número tem lastro

O `revisor-fatos` audita cada número e a coluna "sem lastro" fecha em **zero**.

**Falha se:** aparece no currículo qualquer número que não esteja em
`perfil-exemplo.md`, ou um número arredondado/derivado dos que estão.

## A4 — `[FALTA MÉTRICA]` sobrevive

O fato "Painel de acompanhamento de entregas" não tem resultado no perfil de
exemplo. O bullet correspondente deve usar a escala que existe e marcar
`[FALTA MÉTRICA]`.

**Falha se:** o marcador some, ou vira "resultados expressivos", ou o bullet é
descartado junto com a escala, ou o bullet ou o resumo sugerem o efeito
pendente ("usado na decisão da operação") — traduz-se o objeto, nunca o
efeito (rubrica de escrita, decisão de 17/10/2026).

## A5 — O resumo não é eco dos bullets

Com três bullets, um resumo que reconta dois deles palavra por palavra
desperdiça dois terços do documento.

O número pode se repetir entre resumo e bullet; a frase, não.

**Falha se:** uma linha do resumo repete a estrutura de um bullet.

## A6 — O verbo não é maior que o fato

Todo verbo do currículo tem lastro no fato correspondente. `liderei` exige
liderança escrita no fato; `arquitetei` exige desenho, não uso.

**Falha se:** um verbo de condução aparece sobre um fato que só descreve
execução.

## A7 — Nenhum bullet novo cobre um gap de cultura

A vaga fala em "decide rápido e com autonomia". A seção Cultura do
`revisor-recrutador` pode reportar o gap e sugerir ângulo de resumo; **não**
pode propor bullet novo, e o currículo não pode ganhar um.

**Falha se:** aparece bullet que não corresponde a um fato do perfil.

## A8 — Cultura não emite BLOQUEIA

Alinhamento lido de anúncio é o mais fraco dos julgamentos do painel. A saída
da seção Cultura, dentro do relatório do `revisor-recrutador`, é IMPORTANTE
no máximo.

**Falha se:** há BLOQUEIA na seção de cultura do painel.

## A9 — O score vem com a conta aberta

O `revisor-ats` mostra a aritmética recomputável, não uma impressão. Com a
lista de desejáveis não vazia, os três pesos aparecem.

**Falha se:** o score aparece sem a fração de cada lista, ou a conta não bate
quando refeita à mão.

## A10 — O painel tem quatro relatórios e cinco seções

Quatro revisores rodam: Fatos, Consistência, ATS e Recrutador — nesta ordem,
com Fatos primeiro. O `revisor-recrutador` devolve duas seções na mesma
resposta, `## Recrutador` e `## Cultura`, então o `painel.md` final continua
com cinco seções de conteúdo — só que a última vem do mesmo agente que a
penúltima, não de um quinto agente separado.

Não há candidatura anterior à empresa do ensaio, então o
`revisor-consistencia` **não é acionado** (desde 16/10/2026): o orquestrador
escreve ele mesmo a seção `## Consistência` com "Não acionado: nenhuma
candidatura anterior a esta empresa". A seção existe; o agente, não.

**Falha se:** falta uma seção, a ordem muda, a seção Cultura aparece como
saída de um agente `revisor-cultura` separado, ou o `revisor-consistencia` é
acionado sem candidatura anterior à empresa.

## A11 — O teto de aderência é calculado antes de escrever

O Passo 1.5 do `/nova-vaga` reporta o teto antes de existir currículo, pela
fórmula da rubrica ATS contando como presente toda keyword com lastro no perfil.

Com o perfil de exemplo, `SQL avançado` e `grandes volumes` são frágeis — o
teto deve sair abaixo de 100 e o relatório deve nomear o que falta.

**Falha se:** o teto não é reportado, ou sai como 100 ignorando os gaps.

## A12 — Fato de participação usa verbo de contribuição

O fato "Migração de painéis para Power BI" tem `Escopo: participação` e é
aderente ao requisito "construção de painéis" — a armadilha é escrevê-lo como
autoria ("Migrei 25 painéis...", "Acelerei a atualização..."). Se ele entrar
no currículo, o verbo é de Contribuição (`contribuí para`, `integrei`) e o
bullet atribui o resultado ao time (rubrica de escrita, "Disciplina de
escopo").

Se o currículo não usar esse fato, a asserção vale **não aplicável** — e o
relatório diz isso, em vez de contar como passou.

**Falha se:** o fato aparece com verbo de Construção, Mudança ou Condução, ou
o `revisor-fatos` deixa passar um verbo assim sem BLOQUEIA.

## A13 — O mapa bullet → fato existe e copia o número literal

`ensaio/mapa-novo.md` tem uma linha para cada bullet e para cada número do
resumo. A coluna "Número como está no perfil" é cópia literal do
`perfil-exemplo.md` — "de 3 dias para 4 horas", "35%", "120 mil registros" —
e o `revisor-fatos` cita o mapa na auditoria.

**Falha se:** falta o mapa, falta a linha de algum bullet, ou a coluna do
número difere do perfil.

## A14 — BLOQUEIA só contém bloqueio

Em cada relatório do painel, a seção `### BLOQUEIA` traz apenas itens que
impedem o envio, ou exatamente `- nenhum`. Confirmações ("coluna única,
conforme", "datas idênticas") vão em `### Conferido`.

**Falha se:** alguma seção BLOQUEIA traz um item que afirma conformidade, ou
fica vazia sem o `- nenhum`.

---

## O que não é falha

Redação diferente da rodada anterior. Ordem diferente de bullets igualmente
aderentes. Score alguns pontos acima ou abaixo por leitura diferente da lista
de contexto. Uma sugestão nova que nenhuma asserção proíbe.

O ensaio existe para pegar **regressão de comportamento**, não variação de
escrita. Um relatório que trata cada frase diferente como achado treina o candidato a
ignorar o relatório.
