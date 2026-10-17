# Painel — LinkedIn (ensaio, Fulano de Exemplo)

Rodado em 17/10/2026, depois da regra "competência sem lastro é BLOQUEIA"
(rubrica de LinkedIn e `revisor-linkedin`). Revisores: `revisor-fatos` (modo
LinkedIn) e `revisor-linkedin`.

## Fatos

**Números auditados:** 21. Com lastro: 21. Sem lastro: 0.

Régua usada: `perfil/_exemplo/perfil-exemplo.md`. Documento: `ensaio/linkedin/proposta-novo.md`. Mapa: `ensaio/linkedin/mapa-novo.md`. Vertente: `ensaio/linkedin/vertente.md`. O `perfil/perfil-mestre.md` não foi aberto.

| Número na proposta | Fato do perfil | Campo | Confere? |
|---|---|---|---|
| Sobre §1: "de 3 dias" | Automação de relatórios operacionais | Resultado ("caiu de 3 dias para 4 horas") | Sim |
| Sobre §1: "para 4 horas" | Automação de relatórios operacionais | Resultado | Sim |
| Sobre §2: "14 relatórios semanais" | Automação de relatórios operacionais | Escala ("14 relatórios semanais") | Sim |
| Sobre §2: "6 áreas" | Automação de relatórios operacionais | Escala ("6 áreas consumidoras") | Sim |
| Sobre §2: "três cadastros divergentes" | Padronização da base de cadastro | O que fiz ("unifiquei três cadastros divergentes") | Sim |
| Sobre §2: "120 mil registros" | Padronização da base de cadastro | Escala ("120 mil registros") | Sim |
| Sobre §2: "caíram 35%" | Padronização da base de cadastro | Resultado ("erros de duplicidade caíram 35%") | Sim |
| Sobre §2: "25 painéis" | Migração de painéis para Power BI | Escala ("25 painéis migrados") | Sim |
| Sobre §2: "de semanal para diária" | Migração de painéis para Power BI | Resultado | Sim |
| Sênior b1: "de 3 dias" | Automação de relatórios operacionais | Resultado | Sim |
| Sênior b1: "para 4 horas" | Automação de relatórios operacionais | Resultado | Sim |
| Sênior b1: "14 relatórios semanais" | Automação de relatórios operacionais | Escala | Sim |
| Sênior b1: "6 áreas consumidoras" | Automação de relatórios operacionais | Escala | Sim |
| Sênior b2: "40 usuários recorrentes" | Painel de acompanhamento de entregas | Escala ("40 usuários recorrentes") | Sim |
| Júnior b1: "três cadastros divergentes" | Padronização da base de cadastro | O que fiz | Sim |
| Júnior b1: "120 mil registros" | Padronização da base de cadastro | Escala | Sim |
| Júnior b1: "caíram 35%" | Padronização da base de cadastro | Resultado | Sim |
| Júnior b2: "25 painéis" | Migração de painéis para Power BI | Escala | Sim |
| Júnior b2: "de semanal para diária" | Migração de painéis para Power BI | Resultado | Sim |
| Cargo Sênior: "jan/2025 – atual" | ACME Log, Analista de Dados Sênior | Cabeçalho do cargo | Sim |
| Cargo Júnior: "fev/2023 – dez/2024" | ACME Log, Analista de Dados Júnior | Cabeçalho do cargo | Sim |

### BLOQUEIA
- nenhum

### IMPORTANTE
- nenhum

### SUGESTÃO
- Não ficou de fora nenhum fato do perfil: os quatro estão na proposta. O único ganho que ainda dá para ter é o resultado do fato "Painel de acompanhamento de entregas". A pergunta pendente é qual foi o efeito no atraso ou na decisão. Hoje o fato entra só com a escala, e é isso que a rubrica pede. A pergunta pertence a "Pendências do perfil" do `diagnostico.md`, não a este texto.

### Conferido
- **Mapa:** todo número da proposta tem linha no `mapa-novo.md`. A coluna "Número como está no perfil" bate literalmente com o perfil nas 8 linhas. O mapa não tem linhas para a headline nem para as Competências, mas nenhuma das duas traz número. Conferi as duas direto contra o perfil (itens abaixo).
- **Headline:** "Analista de Dados" é parte do nome de um cargo ocupado, sem a senioridade: Analista de Dados Sênior e Júnior. "Analista de BI", que a vertente usa, ficou de fora, e isso está correto. Python, SQL e Power BI têm lastro em Competências. A headline não traz setor nem domínio.
- **Verbos e escopo:**
  - Fatos de `autoria` (Automação, Painel, Padronização): "Troquei", "Reduzi", "Construí", "Unifiquei" e "Padronizei" são todos verbos de Construção ou Mudança, dentro do teto do escopo.
  - Fato de `participação` (Migração para Power BI): o texto usa "contribuí para" no Sobre e "Integrei… e contribuí para" no bullet Júnior 2. São verbos de Contribuição e atribuem o resultado ao time de BI. Correto.
- **Placeholder:** não há `[FALTA MÉTRICA]` na proposta. O bullet do painel entra só com a escala e não tem frase que sugira resultado. O mapa registra "resultado em aberto — fora do texto público".
- **Cargos, empresa e datas:** "Analista de Dados Sênior — ACME Log (jan/2025 – atual)" e "Analista de Dados Júnior — ACME Log (fev/2023 – dez/2024)" são idênticos ao perfil. "Sou Analista de Dados na ACME Log" também é consistente com o perfil.
- **Competências (fixadas e linha do Sobre):** SQL, Python, Power BI, Automação de rotinas e Modelagem de indicadores estão todas no perfil. Excel não foi promovido a competência, e está certo: no fato de migração a ferramenta é só contexto. O perfil não tem nenhuma stack de nível `estudado` citada em Experiência.
- **Redundância entre bullets da Experiência:** nenhuma. São quatro bullets, cada um sobre um fato diferente. O Sobre reconta três desses fatos, e no LinkedIn isso é próprio da estrutura, não uma duplicação entre bullets. Há um ponto fora do meu escopo que passo ao revisor de escrita: a frase do Sobre sobre os cadastros ("unifiquei três cadastros divergentes num único modelo de 120 mil registros, e os erros de duplicidade caíram 35%") repete quase palavra por palavra o bullet Júnior 1. Isso é matéria da regra "o resumo não pode ser eco dos bullets", não de verdade.

## LinkedIn

**Score recomputado:** 85,50/100 — busca 40,00 · abertura 20 · prova 15 · completude 10,50 (conta aberta abaixo). Orquestrador: 85,50/100.

**Conta aberta**

Termos recorrentes. São 5 anúncios, e o corte é aparecer em pelo menos metade deles (2c ≥ 5, ou seja, 3 ou mais). Entram sql (5/5), python (3/5) e power bi (3/5). Os títulos da vertente também contam: analista de dados e analista de bi. Ficam fora do corte etl (2/5), dax (2/5), excel (1/5) e databricks (1/5). Total: 5 termos.

| Termo | Melhor seção na proposta | Peso |
|---|---|---|
| analista de dados | Headline | 2 |
| python | Headline | 2 |
| sql | Headline | 2 |
| power bi | Headline | 2 |
| analista de bi | ausente ("time de BI" no Sobre não casa com o termo) | 0 |

- **Busca:** soma 8 ÷ (2 × 5) × 50 = **40,00**.
- **Completude:** 7 itens marcados × 1,5 = **10,50**. Os itens são foto, banner, URL personalizada, Open to Work, localidade, top 5 fixadas e formação. Ficam sem marca, e sem fato, em destaque, certificações e idiomas.
- **Abertura, headline: 10.** A família tem um só título ocupado, "Analista de Dados" (os cargos são Analista de Dados Sênior e Júnior, sem a senioridade), e a headline o nomeia. "Analista de BI" não foi ocupado e não tira nota.
- **Abertura, primeiros ~220 caracteres do Sobre: 10.** O primeiro parágrafo tem cerca de 151 caracteres. Traz o título ocupado ("Sou Analista de Dados na ACME Log") e uma prova com número ("de 3 dias para 4 horas").
- **Prova: 15 × 2/2 = 15.** No cargo Sênior, o fechamento caiu de 3 dias para 4 horas. No Júnior, os erros de duplicidade caíram 35%.
- **Divergência com o orquestrador:** 0 ponto.

### BLOQUEIA
- nenhum

### Conferido
- **Headline:** cerca de 43 caracteres, limite de 220.
- **Sobre:** cerca de 650 caracteres, limite de 2.600.
- **Experiências:** Sênior com cerca de 345 caracteres e Júnior com cerca de 255. O limite é 2.000 cada.
- **Título na headline:** "Analista de Dados" é cargo ocupado.
- **Competências na headline:** Python, SQL e Power BI estão nas Competências do perfil-mestre.
- **Domínio:** a headline não anexa setor nem domínio.
- **Marcadores:** a proposta não tem nenhum marcador entre colchetes. O fato do painel de entregas, que tem escala e não tem resultado, entra só com "40 usuários recorrentes", sem frase que sugira efeito.
- **Busca:** os quatro termos recorrentes com lastro (analista de dados, python, sql, power bi) já estão na headline, com peso máximo.
- **Abertura:** headline 10 e início do Sobre 10, conferidos acima.
- **Escopo do fato de participação (migração para Power BI):** usa verbo de contribuição no Sobre ("contribuí para a migração") e na experiência ("Integrei o time de BI… contribuí para que…").
- **Escopo dos fatos de autoria:** os verbos ficam dentro do teto (Reduzi/Troquei, Construí, Padronizei/unifiquei).
- **Fixadas:** SQL, Python, Power BI, Automação de rotinas e Modelagem de indicadores. Todas estão nas Competências do perfil-mestre. Excel e Comunicação saíram e não têm lastro como competência.
- **Cargos e datas:** iguais aos do perfil-mestre.
- **Tom:** o Sobre está em primeira pessoa e não tem adjetivo sobre o candidato sem prova ao lado.

### IMPORTANTE
- nenhum

### SUGESTÃO
- **O Sobre repete o bullet da padronização quase palavra por palavra.** Sobre: "unifiquei três cadastros divergentes num único modelo de 120 mil registros, e os erros de duplicidade caíram 35%". Bullet do Júnior: "Padronizei três cadastros divergentes num único modelo de 120 mil registros, e os erros de duplicidade caíram 35%". O Sobre deveria resumir e deixar o detalhe para o bullet. Exemplo com os mesmos fatos: "Antes disso, reduzi em 35% os erros de duplicidade ao unificar a base de cadastro, com 120 mil registros."
- **A experiência Júnior não tem a linha de contexto que a rubrica pede.** A Sênior tem. Exemplo sem domínio novo: "Base de cadastro e painéis gerenciais."
- **Os dois cargos têm 2 bullets cada, e a rubrica pede de 3 a 5.** Não há mais fatos no perfil-mestre para preencher, então não é para completar. Fica registrado só para o candidato saber que um terceiro fato por cargo daria mais corpo às experiências.

### Gaps declarados
- `analista de bi` — recorrente na vertente (é um dos títulos dela), mas o candidato não ocupou esse cargo. Não inserido na headline.
- `etl` (2/5), `dax` (2/5) e `databricks` (1/5) ficam abaixo do corte de recorrência e não têm fato no perfil. Não inseridos.
- Certificações, idiomas e Em destaque — nenhum fato no perfil, por isso continuam desmarcados na Completude.

## Aplicado / recusado

- Nada aplicado: o ensaio mede o painel, não pede decisão ao candidato.

Nenhuma mudança de conteúdo — reauditoria dispensada.
