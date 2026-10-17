# Painel — ensaio (perfil fictício, vaga fictícia)

Rodado em 17/10/2026, depois da decisão "traduz-se o objeto, nunca o efeito"
(rubrica de escrita). Três revisores acionados; Consistência não acionado (sem
candidatura anterior à empresa).

Teto de aderência (Passo 1.5): 53/100 — 3 de 4 obrigatórias têm lastro (uma
frágil). Sem lastro: `SQL avançado`. Frágil: `grandes volumes de dados` (120
mil registros). Abaixo de 55 o fluxo pararia para perguntar; o ensaio simula
"seguir", como no baseline.

## Fatos

**Números auditados:** 17 — com lastro: 17 · sem lastro: 0

| Número no currículo | Fato do perfil | Campo | Confere? |
|---|---|---|---|
| 3 dias (Resumo) | Automação de relatórios operacionais | Resultado: "tempo de fechamento caiu de 3 dias para 4 horas" | Sim |
| 4 horas (Resumo) | Automação de relatórios operacionais | Resultado | Sim |
| 120 mil registros (Resumo) | Padronização da base de cadastro | Escala: "120 mil registros" | Sim |
| 35% menos duplicidade (Resumo) | Padronização da base de cadastro | Resultado: "erros de duplicidade caíram 35%" | Sim |
| 3 dias (ACME Sênior, bullet 1) | Automação de relatórios operacionais | Resultado | Sim |
| 4 horas (ACME Sênior, bullet 1) | Automação de relatórios operacionais | Resultado | Sim |
| 14 relatórios semanais (ACME Sênior, bullet 1) | Automação de relatórios operacionais | Escala: "14 relatórios semanais" | Sim |
| 6 áreas consumidoras (ACME Sênior, bullet 1) | Automação de relatórios operacionais | Escala: "6 áreas consumidoras" | Sim |
| 40 usuários recorrentes (ACME Sênior, bullet 2) | Painel de acompanhamento de entregas | Escala: "40 usuários recorrentes" | Sim |
| três cadastros (ACME Júnior, bullet 1) | Padronização da base de cadastro | O que fiz: "unifiquei três cadastros divergentes" | Sim |
| 120 mil registros (ACME Júnior, bullet 1) | Padronização da base de cadastro | Escala | Sim |
| 35% (ACME Júnior, bullet 1) | Padronização da base de cadastro | Resultado | Sim |
| 25 painéis (ACME Júnior, bullet 2) | Migração de painéis para Power BI | Escala: "25 painéis migrados" | Sim |
| semanal → diária (ACME Júnior, bullet 2) | Migração de painéis para Power BI | Resultado: "atualização dos painéis passou de semanal para diária" | Sim |
| jan/2025 – atual (ACME Sênior) | Cabeçalho "ACME Log — Analista de Dados Sênior (jan/2025 – atual)" | Data | Sim |
| fev/2023 – dez/2024 (ACME Júnior) | Cabeçalho "ACME Log — Analista de Dados Júnior (fev/2023 – dez/2024)" | Data | Sim |
| 2020 – 2023 (Formação) | Formação: "Tecnólogo em Análise de Dados — Universidade Exemplo (2020 – 2023)" | Data | Sim |

### BLOQUEIA
- nenhum

### IMPORTANTE
- **Placeholder pendente — ACME Sênior, bullet 2** ("Construí um painel de indicadores de entrega... `[FALTA MÉTRICA]`"). O que precisa ser respondido, nas palavras do próprio perfil: *qual foi o efeito do painel no atraso das entregas ou na decisão da operação?* Se não houver resposta confirmada, a saída é tirar o marcador e deixar o bullet só com a escala (40 usuários recorrentes), que tem lastro.

### SUGESTÃO
- Nenhum fato do perfil ficou de fora: os quatro fatos foram usados. A única melhora possível em conteúdo é fechar o resultado do Painel de acompanhamento de entregas no perfil (ver IMPORTANTE).

### Conferido
- **Mapa vs. perfil:** as 6 linhas de `ensaio/mapa-novo.md` batem literalmente com os campos do perfil, e não existe número no currículo sem linha no mapa.
- **Verbos vs. Escopo:**
  - "Reduzi" (Sênior b1) está sobre um fato de escopo `autoria` em que o candidato substituiu a apuração manual. Compatível.
  - "Construí" (Sênior b2) está sobre um fato de escopo `autoria` em que o candidato construiu o painel. Compatível.
  - "Padronizei" (Júnior b1) está sobre um fato de escopo `autoria` em que o candidato unificou os três cadastros. Compatível.
  - "Integrei... e contribuí para" (Júnior b2) está sobre um fato de escopo `participação`. São verbos de Contribuição, então está correto. Não há "migrei" nem "reduzi" atribuídos só ao candidato.
  - O Resumo diz "troca apuração manual por rotina automatizada e constrói painéis". As duas afirmações têm lastro em fatos de `autoria`.
- **"adotado por 40 usuários recorrentes":** é uma leitura fiel do campo Escala ("40 usuários recorrentes") e não afirma nenhum resultado.
- **Cargos, empresa e datas:** ACME Log, Analista de Dados Sênior e Analista de Dados Júnior batem com o perfil, assim como os períodos. O título "Analista de Dados" no topo cabe nos dois cargos ocupados.
- **Formação:** curso, instituição e período batem com o perfil.
- **Competências vs. Experiência:** o perfil não marca nenhuma stack como `nível estudado`. Python e Power BI citados nos bullets têm lastro em fato de emprego (Automação de relatórios e Migração para Power BI).
- **Redundância:** os quatro bullets contam quatro fatos diferentes. O Resumo repete números dos bullets (3 dias → 4 horas, 120 mil, 35%), mas isso é síntese do Resumo, não dois bullets contando a mesma história.

Arquivos auditados: `ensaio/curriculo-novo.md`, `ensaio/mapa-novo.md`, `ensaio/vaga.md`. Régua: `perfil/_exemplo/perfil-exemplo.md` (`perfil/perfil-mestre.md` não foi aberto).

## Consistência

Não acionado: nenhuma candidatura anterior a esta empresa em `vagas/`.

## ATS

**Score:** 52,5/100. Conta aberta: 3/4 obrigatórias, 0/3 desejáveis, 0/5 de contexto.

- Obrigatórias: (3/4) × 70 = 52,5
  - Presentes: `SQL` (está em COMPETÊNCIAS; o qualificador "avançado" não aparece), `Python`, `construção de painéis`.
  - Ausente: `grandes volumes de dados`.
- Desejáveis: (0/3) × 20 = 0
  - Ausentes: `Databricks`, `conhecimento de varejo`, `inglês intermediário`.
- De contexto: (0/5) × 10 = 0
  - Ausentes: `Supply`, `ruptura de gôndola`, `giro de estoque`, `sell-out (por praça)`, `reposição`.
- Total: 52,5 + 0 + 0 = **52,5**. Fica na faixa abaixo de 55: a vaga pede algo que o perfil não tem, e a decisão de se candidatar é do candidato.

### BLOQUEIA
- nenhum

### Conferido
- O formato está correto. O documento tem coluna única, sem tabela, imagem, cabeçalho ou rodapé. As seções seguem R3 (RESUMO PROFISSIONAL, EXPERIÊNCIA PROFISSIONAL, FORMAÇÃO ACADÊMICA, COMPETÊNCIAS). As datas de experiência estão em `mês/ano`, os bullets são lista de verdade (`-`) e não `•` digitado, e as hard skills vêm antes em COMPETÊNCIAS (não há soft skills listadas).

### IMPORTANTE
- **Nenhuma keyword real, não escrita.** Todas as keywords ausentes no currículo também não têm fato no perfil que as comprove. Os pontos que faltam são gaps de aderência, não falta de palavra. Nenhuma inserção resolve isso sem violar R1.
- **Qualificador "avançado" em SQL:** o filtro reconhece `SQL`, mas nenhum fato do perfil mostra nível avançado. Além disso, SQL só aparece em COMPETÊNCIAS, sem nenhum bullet que o use. O termo conta como presente; "avançado" não deve ser acrescentado.

### SUGESTÃO
- **Data da formação:** está como `2020 – 2023`, só com o ano, e as experiências usam `mês/ano`. A inconsistência não impede a leitura. O perfil também não registra os meses, então eles não devem ser inventados. Se o candidato souber os meses, eles entram primeiro no perfil.
- **Repetição (rubrica, "Uma vez basta"):** `Python` está no bullet 1 da ACME Log Sênior e em COMPETÊNCIAS. `Power BI` está no bullet 2 da ACME Log Júnior e em COMPETÊNCIAS. A repetição é pequena e não prejudica o filtro, mas a rubrica dispensa a segunda menção quando o termo já tem lastro num bullet.
- **`[FALTA MÉTRICA]` no bullet 2 da ACME Log Sênior:** o placeholder está entre crases, então no .docx pode sair em fonte monoespaçada. A máquina lê sem problema. O conteúdo é assunto do `revisor-fatos` e da trava do `/exportar`; menciono só como registro.

### Gaps declarados
- `grandes volumes de dados` (obrigatória): nenhum fato do perfil sustenta. O maior volume registrado são os 120 mil registros do fato "Padronização da base de cadastro", e usá-lo para afirmar "grandes volumes" seria inflar o fato. Não inserido.
- `SQL avançado` (o nível, obrigatória): nenhum fato comprova esse nível. Não inserido.
- `Databricks` (desejável): nenhum fato no perfil sustenta. Não inserido.
- `conhecimento de varejo` (desejável): toda a experiência registrada é na ACME Log (logística), sem fato de varejo. Não inserido.
- `inglês intermediário` (desejável): o perfil não traz idioma nem nível. Não inserido.
- `Supply` (contexto): o fato "Painel de acompanhamento de entregas" trata de indicadores de entrega numa operação logística. Isso é vizinho de supply, não equivalente: chamá-lo de "Supply" adaptaria o fato, não o vocabulário (R6). Não inserido.
- `ruptura de gôndola` (contexto): nenhum fato no perfil sustenta. Não inserido.
- `giro de estoque` (contexto): nenhum fato no perfil sustenta. Não inserido.
- `sell-out (por praça)` (contexto): nenhum fato no perfil sustenta. Não inserido.
- `reposição` (contexto): nenhum fato no perfil sustenta. Não inserido.

### Perguntas eliminatórias
- **Inglês:** a vaga cita "inglês intermediário" como desejável, e o formulário provavelmente vai perguntar o nível. O perfil de exemplo não tem a seção "Respostas de formulário", então a resposta precisa vir do candidato.
- Pretensão salarial, modelo de trabalho, disponibilidade, formação exigida, CNH e PCD: a vaga não sinaliza nenhuma dessas.

## Recrutador

**Veredito dos 6 segundos:** avança. O topo mostra um analista de dados que automatiza com Python e constrói painéis, com resultado numérico logo no primeiro bullet. Isso cobre dois dos quatro requisitos obrigatórios antes do olho sair do primeiro bloco.

### BLOQUEIA
- nenhum

### IMPORTANTE
- **`[FALTA MÉTRICA]` no bullet do painel (ACME Log, Sênior, bullet 2).** Não é um erro de escrita. É uma pergunta que ainda está em aberto para o candidato: "qual foi o efeito no atraso ou na decisão?". Ela precisa ser respondida no perfil antes do envio, ou a marca sai do texto e o bullet fica só com a escala (40 usuários recorrentes), que já se sustenta sozinha. Um recrutador que vê a marca impressa descarta o documento.
- **"SQL avançado" é obrigatório e aparece só em COMPETÊNCIAS.** Nenhum bullet mostra SQL em uso, e o perfil não tem nenhum fato que o sustente. Na leitura rápida, o recrutador vê Python e painéis comprovados e SQL apenas declarado. Não há o que reescrever sem inventar. Fica a pergunta ao candidato: existe um fato com SQL na vida real que ainda não está no perfil-mestre?
- **"Grandes volumes de dados" (obrigatório) se apoia em 120 mil registros.** É o único número de volume no currículo. Para quem lê uma vaga de 180 lojas, pode parecer pouco. Também não há como corrigir sem fato novo. É informação para o candidato pesar, não um defeito do texto.

### SUGESTÃO
- **Primeira linha do resumo.** Ela já vende, porque diz o que a pessoa faz acontecer ("troca apuração manual por rotina automatizada"). Só que esconde a ferramenta que a vaga pede. Exemplo usando apenas o que já está no currículo: *"Analista de dados que troca apuração manual por rotinas em Python e constrói painéis de indicadores para a operação."*
- **Os 3 bullets mais fracos.** Nenhum é ruim; com quatro bullets no total, esses são os relativamente mais fracos.
  1. **Migração para Power BI (Júnior, bullet 2):** longo demais, com dois verbos e duas orações ("Integrei... e contribuí para..."). O verbo de contribuição está correto para um fato de participação. O problema é só o comprimento. Exemplo: *"Integrei o time de BI que migrou 25 painéis gerenciais do Excel para o Power BI e levou a atualização de semanal para diária."*
  2. **Automação de relatórios (Sênior, bullet 1):** é o bullet mais forte, mas a escala chega pendurada no final ("em 14 relatórios semanais para 6 áreas consumidoras"), e o "em... para..." trava a leitura. Exemplo: *"Reduzi de 3 dias para 4 horas o fechamento de 14 relatórios semanais, usados por 6 áreas, ao substituir a apuração manual por rotinas em Python agendadas."*
  3. **Padronização de cadastro (Júnior, bullet 1):** o resultado vem depois de uma vírgula e de um "e" solto, e o 35% perde força. Exemplo: *"Padronizei três cadastros divergentes num único modelo de 120 mil registros, reduzindo em 35% os erros de duplicidade."*
- **Ruído no resumo.** "Na prática:" é um conector que ocupa espaço sem trazer nada. Já "Busco um time que decide rápido" repete quase literalmente o anúncio ("Somos um time que decide rápido"). Como aspiração é permitido, mas um recrutador atento percebe o espelho. Vale reformular com palavras próprias.
- **Ruído em COMPETÊNCIAS.** A linha "Processos: automação de rotinas, modelagem de indicadores" repete o que o resumo e os bullets já provam. É um bom candidato a corte se o espaço apertar.
- **Senioridade.** O candidato é Sênior desde jan/2025 e a vaga é Pleno. A headline sem senioridade está correta. Mesmo assim, o recrutador vai ver "Sênior" no cargo e pode levantar a questão de faixa salarial na triagem. Vale o candidato ter essa resposta pronta.

### Conferido
- A headline "Analista de Dados" é um título ocupado, sem senioridade, e não anexa "Supply" nem "Varejo", domínios que nenhum fato sustenta.
- Os cargos dentro da experiência estão iguais aos do perfil.
- O fato de participação (migração para Power BI) usa verbos de contribuição ("Integrei", "contribuí para"), dentro do teto do escopo.
- O resumo não ecoa os bullets: os números se repetem, as frases não.
- A hierarquia visual funciona. O nome domina (H1), as seções se distinguem (H2) e cada cargo vem em negrito com o período na mesma linha. O olho desce sem tropeçar.
- O bullet do painel não traduz o efeito: diz "para a operação" e não "usado na decisão", o que respeita o resultado pendente.

## Cultura

**Valores lidos na vaga:**
1. `Velocidade de decisão` — evidência: "Somos um time que decide rápido"
2. `Autonomia` — evidência: "e com autonomia"
3. `Melhoria de processo por iniciativa própria` — evidência: "Aqui ninguém espera aprovação para melhorar um processo."
4. `Dado a serviço da decisão operacional` — evidência: "apoiar decisões de reposição das 180 lojas"

Setor (varejo) e "180 lojas" não foram usados para gerar nenhum valor (R6).

**Mapeamento:**

| Valor | Bullet que demonstra | Como |
|---|---|---|
| Velocidade de decisão | Sênior, bullet 1 (3 dias para 4 horas); Júnior, bullet 2 (semanal para diária) | Parcial: mostra o dado chegando mais rápido a quem usa, não uma decisão mais rápida |
| Autonomia | Sênior, bullet 1; Júnior, bullet 1 | Parcial: as entregas são de autoria própria, mas o texto não diz se partiram de iniciativa dele |
| Melhoria de processo por iniciativa própria | Sênior, bullet 1 (apuração manual virou rotina); Júnior, bullet 1 (três cadastros unificados) | Parcial: são melhorias de processo claras, mas o perfil não registra se alguém pediu |
| Dado a serviço da decisão operacional | Sênior, bullet 2 (painel para a operação, 40 usuários) | Parcial: comprova adoção, mas o efeito na decisão é exatamente o `[FALTA MÉTRICA]` em aberto |

### IMPORTANTE
- nenhum. Os quatro valores têm alguma demonstração, ainda que parcial.

### SUGESTÃO
- **Ângulo do resumo:** *"Encurto o tempo até o dado chegar à operação: relatórios que fechavam em 3 dias passaram a sair em 4 horas para 6 áreas consumidoras."*
- **Melhoria de processo por iniciativa / Autonomia.** Existe na vida, não está no perfil? Perguntar ao candidato se a automação dos relatórios e a unificação dos cadastros partiram dele. Se sim, registrar isso no perfil-mestre, no campo `O que fiz` dos dois fatos. Hoje o currículo não pode afirmar essa iniciativa.
- **Dado a serviço da decisão.** Existe na vida, não está no perfil? É a mesma pergunta pendente do painel: qual foi o efeito no atraso ou na decisão? Com resposta confirmada, o bullet passa a cobrir esse valor por inteiro. Sem ela, nada de "usado na decisão" no texto.
- **Velocidade de decisão.** Já existe no perfil e já está no currículo, mas só como velocidade do dado. Não há fato que mostre uma decisão mais rápida. Ler isso como alinhamento parcial é o honesto. Não é um buraco a tapar.

## Aplicado / recusado

- Nada aplicado: o ensaio mede o painel, não pede decisão ao candidato.

Nenhuma mudança de conteúdo — reauditoria dispensada.
