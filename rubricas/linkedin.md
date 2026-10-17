# Rubrica de LinkedIn

O LinkedIn não é um currículo maior. O currículo vai para quem o candidato
escolheu; o LinkedIn é o que faz o recrutador da vertente **achar** o
candidato numa busca e **continuar lendo** depois de achar. Esta rubrica cobre
só o que muda em relação à `rubricas/escrita.md` — fórmula do bullet,
verbos, `Escopo` e métricas continuam valendo, sem repetição aqui.

## Limites

Conferidos em 16/10/2026. A Central de Ajuda do LinkedIn só publica o limite
de competências; os de texto vêm do consenso das fontes recentes e **não**
estão confirmados em documentação oficial. Por isso, a palavra final é o
contador do próprio editor do LinkedIn: no Passo 8 do `/linkedin`, o candidato
confirma que cada seção coube.

| Seção | Limite | Fonte |
|---|---|---|
| Headline | 220 caracteres | Fontes de terceiros recentes (guias anteriores a 2020 diziam 120) |
| Sobre | 2.600 caracteres | Fontes de terceiros recentes (o antigo era 2.000) |
| Descrição de cada experiência | 2.000 caracteres | Fontes de terceiros recentes |
| Competências | 100 no total | [Central de Ajuda do LinkedIn](https://www.linkedin.com/help/linkedin/answer/a549047/add-and-remove-skills-on-your-profile) |
| Competências em destaque | 5 | Prática do squad (bloco Completude); limite oficial não publicado |

Caractere conta letra, número, espaço e pontuação. Texto em "negrito
Unicode" ocupa mais de um caractere por letra e prejudica a busca — não use.

Limite estourado é BLOQUEIA: o LinkedIn corta o texto ou recusa salvar.

## Score

Busca 50 · Abertura 20 · Prova 15 · Completude 15. Três números: **atual**
(o perfil hoje), **teto** (o melhor possível com os fatos que já existem no
perfil-mestre) e **depois** (a proposta aprovada). O que fica acima do teto é
falta de experiência, e o relatório diz isso em vez de prometer.

Busca e Completude saem de `tools/score_linkedin.py` — determinístico e
recomputável:

- **Busca (50)** — termos recorrentes da vertente (presentes em pelo menos
  metade dos anúncios), mais os **títulos da família**. Cada termo pontua pela
  melhor seção onde aparece: Headline 2 · Competências 1,5 · Sobre ou
  Experiência 1 · ausente 0. Conta: `soma ÷ (2 × N) × 50`.
- **Completude (15)** — 10 itens, 1,5 cada: foto, banner, URL personalizada,
  Open to Work com cargos, localidade, top 5 competências fixadas, Em
  destaque, formação, certificações, idiomas.
- **Teto** — trata como presente todo termo com fato no perfil-mestre, na
  melhor seção que o fato permite, e todo item de Completude que depende só de
  configuração.

Abertura e Prova são julgamento, e cada ponto dado ou negado vem com o motivo:

- **Abertura (20)** — dois critérios de 10, cada um com três notas fixas:
  - **Headline (10):** 10 se nomeia **todos** os títulos da família que o
    candidato ocupou; 5 se nomeia só parte deles; 0 se não nomeia nenhum.
    Título da família que o candidato **não** ocupou não conta contra — é gap
    da Busca, não falha da headline. Título não ocupado ou domínio sem lastro
    **na** headline é BLOQUEIA, não nota.
  - **Primeiros ~220 caracteres do Sobre (10):** 10 se trazem um título
    ocupado da vertente **e** uma prova com número; 5 se trazem só um dos dois;
    0 se nenhum.
- **Prova (15):** 15 × (experiências com pelo menos um resultado quantificado
  com lastro ÷ experiências listadas).

## Headline

- Abre com os títulos da vertente que os recrutadores buscam **e que o
  candidato ocupou**, separados por `|` — no máximo três. Título ocupado é um
  cargo do perfil-mestre, inteiro ou uma das partes do nome, sem a senioridade
  (rubrica de escrita, "Vocabulário não é domínio").
- **Título da família que o candidato não ocupou não entra**, mesmo que a
  vertente o use e mesmo com fato da função. "Analista de BI" para quem foi
  Analista de Dados é BLOQUEIA (decisão de 16/10/2026): o recrutador lê título
  como cargo ocupado. O vocabulário da função entra no Sobre e nas
  experiências, onde há fato.
- Pode trazer 2 ou 3 competências centrais com lastro.
- **Vocabulário não é domínio** (rubrica de escrita): headline não anexa setor,
  área ou domínio que nenhum fato sustenta. "Analista de Dados | Varejo" sem
  fato de varejo é BLOQUEIA.

## Sobre

- Primeira pessoa, parágrafos curtos.
- **Os primeiros ~220 caracteres vendem** — é o que aparece antes do "ver
  mais": cargo da vertente + a prova mais forte, com número.
- Depois: 2 ou 3 provas com número, o que o candidato busca na vertente, e uma
  linha de competências.
- Sem adjetivo sobre si sem prova ao lado.

## Experiência

- Cargo e datas **nunca** mudam — são os do perfil-mestre.
- Uma linha de contexto (o que a área faz) e 3 a 5 bullets na fórmula da
  rubrica de escrita, com o `Escopo` de cada fato.
- Os termos da vertente entram onde o fato os sustenta — uma vez cada.

## `[FALTA MÉTRICA]` não vai a público

Num currículo, o marcador fica no texto até o candidato responder. Num perfil
público, **nunca**: o LinkedIn é lido por todos os recrutadores ao mesmo tempo,
e um marcador ali é um defeito exposto.

- Fato com escala e sem resultado: entra **só com a escala**, sem marcador e
  sem frase que sugira o resultado ("ajudou a decidir", "melhorou").
- Fato sem escala e sem resultado: entra só se ainda descrever uma entrega
  concreta; se não, fica de fora.
- A pergunta que destravaria o resultado vai para o `diagnostico.md`, seção
  "Pendências do perfil", e o mapa registra "resultado em aberto — fora do
  texto público".
- `[FALTA MÉTRICA]` em `proposta.md` é BLOQUEIA.

## Competências

- **Fixadas em destaque (5)** — a linha `Fixadas:` do `atual.md`/`proposta.md`: os termos recorrentes da vertente com lastro, na ordem
  de recorrência nos anúncios.
- Demais: as outras competências do perfil-mestre relevantes para a vertente,
  até o limite de 100. Nível `estudado` pode entrar aqui; nunca numa descrição
  de experiência.
- Competência que o perfil-mestre não registra não entra — nem copiada do
  perfil atual, nem tirada de um fato onde a ferramenta é só contexto
  ("migrou do Excel"). Competência sem lastro é BLOQUEIA.

## Em destaque e Projetos

- Só projetos com fato no perfil-mestre. Projeto acadêmico declara que é
  acadêmico (nível `aplicado em projeto acadêmico`).
- Nível `estudado` não vira projeto.

## Checklist de configuração

Não é texto — é o que o candidato configura no LinkedIn: foto, banner, URL
personalizada, Open to Work com os títulos da vertente, localidade, 5
competências em destaque. Entra no Passo 8 do `/linkedin` e no bloco
Completude.
