# Painel — LinkedIn (ensaio, Fulano de Exemplo)

Rodado em 17/10/2026, depois das correções de consistência dos comandos.
Revisores: `revisor-fatos` (modo LinkedIn) e `revisor-linkedin`.

## Fatos

**Números auditados:** 11 — com lastro: 11 · sem lastro: 0

Régua: `perfil/_exemplo/perfil-exemplo.md`. Documento: `ensaio/linkedin/proposta-novo.md`. Mapa: `ensaio/linkedin/mapa-novo.md`. Vertente: `ensaio/linkedin/vertente.md`.

| Número no currículo | Fato do perfil | Campo | Confere? |
|---|---|---|---|
| 3 dias → 4 horas (Sobre §1; Sênior b1) | Automação de relatórios operacionais | Resultado: "tempo de fechamento caiu de 3 dias para 4 horas" | Sim |
| 14 relatórios semanais (Sobre §2; Sênior b1) | Automação de relatórios operacionais | Escala | Sim |
| 6 áreas consumidoras (Sobre §2; Sênior b1) | Automação de relatórios operacionais | Escala | Sim |
| três cadastros divergentes (Sobre §2; Júnior b1) | Padronização da base de cadastro | O que fiz | Sim |
| 120 mil registros (Sobre §2; Júnior b1) | Padronização da base de cadastro | Escala | Sim |
| 35% (erros de duplicidade) (Sobre §2; Júnior b1) | Padronização da base de cadastro | Resultado | Sim |
| 25 painéis (Sobre §2; Júnior b2) | Migração de painéis para Power BI | Escala | Sim |
| semanal → diária (Sobre §2; Júnior b2) | Migração de painéis para Power BI | Resultado | Sim |
| 40 usuários recorrentes (Sênior b2) | Painel de acompanhamento de entregas | Escala | Sim |
| jan/2025 – atual (Analista de Dados Sênior, ACME Log) | ACME Log — Analista de Dados Sênior | Cabeçalho | Sim |
| fev/2023 – dez/2024 (Analista de Dados Júnior, ACME Log) | ACME Log — Analista de Dados Júnior | Cabeçalho | Sim |

Verbos conferidos contra o `Escopo`:

| Trecho | Verbo | Escopo do fato | Confere? |
|---|---|---|---|
| Sobre §1 | Substituí | autoria | Sim |
| Sênior b1 | Reduzi | autoria | Sim |
| Sênior b2 | Construí | autoria | Sim |
| Sobre §2 e Júnior b1 | Padronizei | autoria | Sim |
| Sobre §2 | contribuí para | participação | Sim |
| Júnior b2 | Integrei / contribuí para | participação | Sim |

### BLOQUEIA
- nenhum

### Conferido
- Datas, cargos e empresa (ACME Log, Sênior e Júnior) são idênticos ao perfil.
- Cada número da proposta tem lastro literal. Nenhum é derivado ou arredondado.
- Nenhum verbo excede o `Escopo`. O fato de participação (migração para Power BI) só aparece com `contribuí para` e `integrei`, nunca com `reduzi`, `conduzi` ou `elevei`.
- O resultado do fato "Painel de acompanhamento de entregas" está em aberto (`[FALTA MÉTRICA]` no perfil). A proposta não inventa efeito: só traz a escala (40 usuários), e o mapa registra "resultado em aberto — fora do texto público".
- Não há `[FALTA MÉTRICA]` na proposta, o que seria BLOQUEIA no modo LinkedIn.
- Competências citadas (Python, SQL, Power BI, automação de rotinas, modelagem de indicadores) constam na seção Competências do perfil. Nenhuma está anotada como `nível estudado`.
- Headline "Analista de Dados" corresponde a cargo ocupado (Analista de Dados Sênior e Júnior). A omissão do nível não é inflação. O título está nos `Títulos` da vertente.
- Mapa: as 8 linhas batem com o perfil na coluna "Número como está no perfil", no `Escopo` e no verbo. Nenhum número da proposta ficou sem linha.
- Nos dois bullets de migração, o efeito (atualização semanal → diária) vem em formulação de contribuição. Isso evita atribuir o resultado ao candidato sozinho.

### IMPORTANTE
- Redundância Sobre × Experiência: três fatos são contados duas vezes quase com as mesmas palavras.
  - Automação (Sobre §1 e §2, e Sênior b1).
  - Padronização de cadastros (Sobre §2 e Júnior b1).
  - Migração para Power BI (Sobre §2 e Júnior b2).
  Manter o texto detalhado em Experiência, onde o cargo dá contexto. No Sobre, manter só um ou dois fatos, resumidos, em vez de repetir a mesma estrutura frase a frase. Não é falsidade, mas o recrutador lê o mesmo fato duas vezes na mesma página.
- Trechos sem linha no mapa, sem número e sem risco factual:
  - "Sou Analista de Dados na ACME Log" (Sobre).
  - "Busco seguir em Dados & BI, em um time que usa o dado para decidir" (Sobre). É intenção, não fato.
  - O descritor "Dados e automação de relatórios para as áreas da operação" (Sênior). Está coerente com o fato de automação, mas deveria ter linha no mapa.
- A seção Completude marca como feitos foto, banner, URL personalizada, open to work, localidade e formação. O perfil-mestre não registra nada disso, então não há como auditar. Isso depende de o candidato confirmar no LinkedIn real.

### SUGESTÃO
- O perfil não traz mais nenhum fato de experiência além dos quatro usados. Falta só o resultado do painel de entregas (40 usuários). Perguntar ao candidato qual foi o efeito no atraso ou na decisão permitiria fechar o bullet com resultado e tirar a pendência.
- "Formação" (Tecnólogo em Análise de Dados, Universidade Exemplo, 2020–2023) tem lastro no perfil, mas não aparece como seção na proposta. A Completude marca formação como feita.

## LinkedIn

**Score recomputado:** 85,50/100 — busca 40,00 · abertura 20 · prova 15 · completude 10,50 (conta aberta abaixo). Orquestrador: 85,50/100. Sem divergência.

Não tive Bash, então não rodei `tools/score_linkedin.py`. Fiz a conta à mão seguindo a lógica do script, que li: um termo é recorrente se 2×contagem ≥ N, com N=5 anúncios, e a lista de termos é a união dos recorrentes com os títulos da vertente.

**Termos recorrentes (contagem nos 5 anúncios):** `sql` 5, `python` 3, `power bi` 3. `etl` 2, `dax` 2, `excel` 1 e `databricks` 1 ficam abaixo do corte. Os títulos entram na lista: `analista de dados` e `analista de bi`. Isso dá N=5 termos.

**Busca** (melhor seção de cada termo na proposta):

| Termo | Melhor seção | Pontos |
|---|---|---|
| `analista de dados` | Headline | 2 |
| `python` | Headline | 2 |
| `sql` | Headline | 2 |
| `power bi` | Headline | 2 |
| `analista de bi` | ausente. "time de BI" não é o título. | 0 |

Soma 8 ÷ (2×5) × 50 = **40,00**.

**Completude:** 7 de 10 itens (foto, banner, URL, Open to Work, localidade, top 5 fixadas, formação) × 1,5 = **10,50**. Faltam Em destaque, certificações e idiomas, e nenhum tem fato.

**Abertura** = 20:
- Headline = 10. O único título da família que o candidato ocupou é Analista de Dados (Sênior e Júnior na ACME Log), e a headline o nomeia. `analista de bi` não foi ocupado e não tira nota.
- Primeiros ~220 caracteres do Sobre = 10. Os ~155 primeiros caracteres trazem "Sou Analista de Dados" e a prova "3 dias para 4 horas".

**Prova** = 15. As duas experiências têm resultado quantificado com lastro: 3 dias → 4 horas no Sênior e −35% de duplicidade no Júnior. 15 × 2/2 = 15.

**Total** = 40,00 + 20 + 15 + 10,50 = 85,50. É igual ao teto, e a proposta não passa dele.

### BLOQUEIA
- nenhum

### Conferido
- Limites: headline com 43 de 220 caracteres. Sobre com cerca de 700 de 2.600. Experiência Sênior com cerca de 450 de 2.000 e Júnior com cerca de 330 de 2.000. Contagem por estimativa, sem Bash; a folga é grande em todos.
- Headline: só "Analista de Dados" (ocupado) e Python, SQL e Power BI (com lastro em Competências). Sem título não ocupado e sem setor ou domínio.
- Marcador entre colchetes: nenhum na proposta. O painel entra só com a escala (40 usuários recorrentes) e sem frase de efeito. A pergunta do resultado está em "Pendências" do diagnóstico, como a rubrica manda.
- Competências: Python, SQL, Power BI, automação de rotinas e modelagem de indicadores estão na seção Competências do exemplo. Excel e Comunicação saíram, e o Excel só aparece como contexto da migração. As fixadas seguem a ordem de recorrência (SQL, Python, Power BI) e completam com duas do perfil.
- Cargos e datas das experiências batem com o exemplo (Sênior jan/2025 – atual, Júnior fev/2023 – dez/2024).
- Escopo dos verbos:
  - "Reduzi", "Construí" e "Padronizei" cobrem fatos de autoria.
  - "Integrei" e "contribuí para" cobrem o fato de participação (migração).
  - Nenhum verbo proibido.
- Tom: Sobre em primeira pessoa, parágrafos curtos, sem adjetivo sobre si.
- "Busco seguir em Dados & BI": é o nome da vertente e há fato de BI (time de BI, Power BI). Não é domínio sem lastro.
- Diagnóstico: o score atual de 14,50 confere. Busca 10,00 (analista de dados e python só em Experiência), completude 4,50 e abertura e prova 0. O teto de 85,50 também confere: 4 termos com lastro × 2 = 40,00, completude 10,50, abertura 20 e prova 15.

### IMPORTANTE
- Nenhum termo recorrente com lastro ficou fora do texto.
- Nenhum título da família ocupado ficou fora da headline.
- Divergência de score: nenhuma (85,50 contra 85,50).

### SUGESTÃO
- As duas experiências têm 2 bullets, abaixo dos 3 a 5 da rubrica. O perfil de exemplo só tem 2 fatos por cargo, então não há o que acrescentar sem inventar. É limite do perfil e não defeito do texto.
- A experiência Júnior não tem a linha de contexto que a rubrica pede. Exemplo, usando só fatos do exemplo: "Cadastros e painéis gerenciais da operação."
- O Sobre repete os números do bullet de automação (14 relatórios, 6 áreas). A rubrica admite o eco do número, mas dá para variar a frase. Exemplo: "Esse fechamento atende 6 áreas consumidoras."
- O fecho "em um time que usa o dado para decidir" soa como frase de anúncio e não como fato. Não afirma efeito nenhum, mas dá para ancorar no que ele fez. Exemplo: "em um time que precisa de relatórios e painéis confiáveis para a operação."

### Gaps declarados
- `analista de bi` — título da família que o candidato não ocupou. Não inserido na headline, que é BLOQUEIA se entrar. O vocabulário de BI fica no Sobre e nas experiências, onde há fato (time de BI, Power BI).
- `etl` e `dax` — sem fato no perfil. Não são recorrentes, mas constam na vertente. Não inseridos.
- `databricks` e `excel` — sem lastro como competência. O Excel aparece só como origem da migração. Não inseridos.
- Em destaque, certificações e idiomas — sem fato no perfil. Completude fica em 10,50 de 15.

## Aplicado / recusado

- Nada aplicado: o ensaio mede o painel, não pede decisão ao candidato.

Nenhuma mudança de conteúdo — reauditoria dispensada.
