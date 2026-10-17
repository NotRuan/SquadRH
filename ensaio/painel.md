# Painel — ensaio (perfil fictício, vaga fictícia)

Rodado em 17/10/2026, depois das correções de consistência dos comandos (teto
de aderência pela fórmula ATS; seção `### Conferido` no Fatos e no Recrutador).
Três revisores acionados; Consistência não acionado (sem candidatura anterior
à empresa).

Teto de aderência (Passo 1.5), pela fórmula da rubrica ATS contando lastro:
52,5/100 — 3 de 4 obrigatórias, 0 de 3 desejáveis e 0 de 5 de contexto têm
lastro no perfil. Sem lastro: `SQL avançado`, `Databricks`, `conhecimento de
varejo`, `inglês intermediário`, `Supply`, `ruptura de gôndola`, `giro de
estoque`, `sell-out por praça`, `reposição`. Frágil: `grandes volumes de dados`
(120 mil registros). Abaixo de 55 o fluxo pararia para perguntar; o ensaio
simula "seguir", como no baseline.

## Fatos

**Números auditados:** 9 — com lastro: 9 · sem lastro: 0

Régua: `perfil/_exemplo/perfil-exemplo.md`. Documento: `ensaio/curriculo-novo.md`. Mapa: `ensaio/mapa-novo.md`.

| Número no currículo | Fato do perfil | Campo | Confere? |
|---|---|---|---|
| 3 dias → 4 horas (Resumo e Sênior b1) | Automação de relatórios operacionais | Resultado: "caiu de 3 dias para 4 horas" | Sim |
| 14 relatórios semanais (Sênior b1) | Automação de relatórios operacionais | Escala | Sim |
| 6 áreas consumidoras (Sênior b1) | Automação de relatórios operacionais | Escala | Sim |
| 40 usuários recorrentes (Sênior b2) | Painel de acompanhamento de entregas | Escala | Sim |
| três cadastros (Júnior b1) | Padronização da base de cadastro | O que fiz: "três cadastros divergentes" | Sim |
| 120 mil registros (Resumo e Júnior b1) | Padronização da base de cadastro | Escala | Sim |
| 35% (Resumo e Júnior b1) | Padronização da base de cadastro | Resultado: "erros de duplicidade caíram 35%" | Sim |
| 25 painéis (Júnior b2) | Migração de painéis para Power BI | Escala | Sim |
| semanal → diária (Júnior b2) | Migração de painéis para Power BI | Resultado | Sim (não é número, mas conferido) |

Nenhum número do currículo ficou fora do mapa. Todas as colunas "Número como está no perfil" do mapa batem com o perfil.

### BLOQUEIA
- nenhum

### Conferido
- Datas idênticas ao perfil-mestre: jan/2025 – atual, fev/2023 – dez/2024, 2020 – 2023.
- Cargos e empresa idênticos: Analista de Dados Sênior e Júnior na ACME Log; Tecnólogo em Análise de Dados, Universidade Exemplo.
- Verbos dentro do `Escopo`:
  - "Reduzi", "Construí" e "Padronizei" vêm de fatos de autoria.
  - "Integrei" e "contribuí para" vêm de fato de participação, a faixa de verbo permitida.
- Os dois números do Resumo (3 dias → 4 horas; 120 mil e 35%) repetem fatos de autoria com valores literais.
- Os valores de escala e resultado vêm de campos distintos do perfil e não foram somados nem arredondados.
- Competências (Python, SQL, Power BI; automação de rotinas, modelagem de indicadores) são idênticas às do perfil. Nenhuma está anotada como `nível estudado`, então não há conflito com a regra 6.
- As stacks citadas nos bullets (Python, Power BI) têm lastro em emprego real.
- O mapa cobre todos os bullets e as duas frases numéricas do Resumo.

### IMPORTANTE
- Placeholder pendente, Experiência, ACME Sênior, bullet 2 (painel de entregas): `[FALTA MÉTRICA]`. A pergunta a responder, do próprio perfil: "qual foi o efeito no atraso ou na decisão?" O fato só tem a escala (40 usuários).
- Redundância:
  - O Resumo repete os dois resultados principais dos bullets: 3 dias → 4 horas e 120 mil registros com queda de 35%.
  - É a mesma informação contada duas vezes na mesma página.
  - Manter os números nos bullets, que trazem escala e contexto. No Resumo, manter no máximo um dos dois resultados, para não esgotar a evidência.
  - Não é duplicidade entre bullets; nenhum bullet repete outro.
- Vocabulário no limite, bullet 2 do Sênior: "adotado por 40 usuários recorrentes". O fato registra apenas escala ("40 usuários recorrentes"), sem dizer "adoção". Não é número inventado, mas "adotado" afirma um efeito que o perfil não declara. Uma redação neutra como "usado por 40 usuários recorrentes" fica mais perto do fato. Se o auditor de consistência ou o candidato entender que "adotado" extrapola, passa a ser BLOQUEIA.

### SUGESTÃO
- Nenhum fato forte do perfil ficou de fora: os 4 fatos aparecem no currículo.
- A vaga pede SQL avançado, grandes volumes, Databricks, varejo e inglês. O perfil-mestre não tem fato que sustente "SQL avançado" (SQL está só em Competências, sem nível), Databricks, varejo nem inglês. Não escrever nada disso sem o candidato confirmar e registrar o fato.

## Consistência

Não acionado: nenhuma candidatura anterior a esta empresa em `vagas/`.

## ATS

**Score:** 52,5/100 (faixa "< 55": a vaga pede algo que o perfil não tem). Conta aberta: 3/4 obrigatórias, 0/3 desejáveis, 0/6 contexto.

```
obrigatórias: 3/4 * 70 = 52,5
desejáveis:   0/3 * 20 =  0
contexto:     0/6 * 10 =  0
score = 52,5
```

**Keywords extraídas de `ensaio/vaga.md`**
- Obrigatórias:
  - `SQL avançado`: presente só como "SQL" em COMPETÊNCIAS. Conta como presente pelo termo. O nível "avançado" não aparece e nenhum fato sustenta (ver Gaps).
  - `Python`: presente.
  - `construção de painéis`: presente no RESUMO e no bullet "Construí um painel de indicadores…".
  - `experiência com grandes volumes de dados`: ausente.
- Desejáveis (todas ausentes):
  - `Databricks`
  - `conhecimento de varejo`
  - `inglês intermediário`
- De contexto (todas ausentes):
  - `ruptura de gôndola`
  - `giro de estoque`
  - `sell-out`
  - `praça`
  - `reposição`
  - `Supply`

### BLOQUEIA
- nenhum

### Conferido
- Coluna única, sem tabela, imagem ou caixa de texto.
- Contato no corpo do texto, sem cabeçalho nem rodapé.
- Seções com os nomes de R3: `RESUMO PROFISSIONAL`, `EXPERIÊNCIA PROFISSIONAL`, `FORMAÇÃO ACADÊMICA`, `COMPETÊNCIAS`.
- Datas da experiência em `mês/ano` (`jan/2025 – atual`, `fev/2023 – dez/2024`).
- Bullets de lista real (`-`), sem `•` digitado.
- COMPETÊNCIAS só tem hard skills, então a ordem hard antes de soft está respeitada.

### IMPORTANTE
- **Keyword real, não escrita:** nenhuma. Nenhum termo ausente tem fato comprobatório no perfil. Por isso o score não pode subir sem inserir termo sem lastro, e não subiu.
- **Aderência baixa por conteúdo, não por formato.** O currículo cobre o núcleo técnico (Python, SQL, painéis), mas não tem vocabulário de varejo nem de Supply. O perfil não oferece lastro para esse vocabulário. A decisão de aplicar assim mesmo é do candidato.

### SUGESTÃO
- **Repetição de termo ("uma vez basta"):**
  - `Python` aparece no RESUMO, no bullet 1 e em COMPETÊNCIAS.
  - `Power BI` aparece no bullet da migração e em COMPETÊNCIAS.
  - Considere manter cada termo só onde tem contexto. Isso é ajuste de redação para o `revisor-recrutador`; não editei nada.
- **Datas da formação:** `2020 – 2023` está só em ano, fora do padrão `mês/ano`. O perfil só tem o ano, então não dá para completar sem inventar. Se o candidato souber os meses, vale informar.
- **`[FALTA MÉTRICA]` no segundo bullet da ACME Log Sênior:** a máquina lê sem problema. É pendência de conteúdo, tratada pelo `revisor-fatos` e pela trava do `/exportar`.
- **Perguntas eliminatórias que a vaga sinaliza:**
  - `inglês intermediário` (listado como desejável).
  - A vaga não menciona pretensão salarial, modelo de trabalho, formação exigida, CNH nem PCD.
  - O perfil-exemplo não tem a seção "Respostas de formulário", então não há resposta padrão de inglês. O candidato precisa informar, e o texto não deve afirmar nível.

### Gaps declarados
- `SQL avançado` (nível "avançado"): o perfil só registra "SQL" em Competências, sem nível. A palavra "SQL" está no currículo, e o nível não foi inserido.
- `experiência com grandes volumes de dados`: nenhum fato sustenta. O maior volume do perfil é "120 mil registros" (fato "Padronização da base de cadastro"). Chamar isso de "grande volume" seria juízo sem lastro. Não inserido.
- `Databricks`: nenhum fato no perfil sustenta. Não inserido.
- `conhecimento de varejo`: nenhum fato no perfil sustenta. Os fatos são de logística (ACME Log). Não inserido.
- `inglês intermediário`: nenhum fato no perfil sustenta. Não inserido.
- `ruptura de gôndola`, `giro de estoque`, `sell-out`, `praça`, `reposição`, `Supply`: nenhum fato no perfil sustenta. Não inseridos.

Arquivos lidos (nenhum editado; `perfil/perfil-mestre.md` não foi aberto):
- `rubricas/ats.md`
- `ensaio/vaga.md`
- `ensaio/curriculo-novo.md`
- `perfil/_exemplo/perfil-exemplo.md`

## Recrutador

**Veredito dos 6 segundos:** avança, com ressalva. Nome, "Analista de Dados" e a primeira linha do resumo (rotinas em Python, painéis para a operação) casam com a vaga. Falta só o vínculo explícito com acompanhamento/painéis, e não há sinal de varejo ou Supply.

### BLOQUEIA
- nenhum

### Conferido
- A headline "Analista de Dados" usa título realmente ocupado (ACME Log, Analista de Dados Sênior/Júnior). Não anexa Supply, varejo nem outro domínio sem fato.
- O nome domina o topo (H1), a headline vem logo abaixo e as seções têm nomes fixos em pt-BR, na ordem da rubrica.
- O cargo dentro da experiência não foi alterado para agradar a vaga.
- Os verbos respeitam o `Escopo` do perfil. Os fatos de autoria usam Mudança/Construção (`Reduzi`, `Construí`, `Padronizei`). O fato de participação (migração para o Power BI) usa Contribuição (`Integrei`, `contribuí para`).
- Nenhum verbo proibido aparece.
- O fato do painel usa a escala (40 usuários recorrentes) e marca só o resultado com `[FALTA MÉTRICA]`. Não afirma efeito na decisão, que não está confirmado.
- O resumo não é eco literal dos bullets. Os números se repetem, mas as frases são diferentes.
- A seção Competências não traz tecnologia fora do perfil.

### IMPORTANTE
- **A primeira linha do resumo descreve mais do que vende para esta vaga.** "Analista de dados que troca apuração manual por rotinas em Python e constrói painéis de indicadores para a operação" é boa, mas "painéis de indicadores" não ecoa o "acompanhamento" que a vaga repete. O que ela deveria dizer, usando só o que está no perfil: "Analista de dados que troca apuração manual por rotinas em Python e entrega à operação painéis de acompanhamento, com fechamento de relatórios de 3 dias para 4 horas." Isso é tradução do objeto e do destinatário do fato, sem afirmar efeito.
- **Bullet 4 (migração para o Power BI) é o mais fraco do documento.**
  - Tem duas linhas cheias, junta dois verbos de contribuição (`Integrei` + `contribuí para`) e carrega Excel/Power BI, tecnologia que a vaga não pede.
  - O resultado (semanal para diária) é bom, mas o bullet está inflado de "como".
  - Enxugamento possível, só com fatos do perfil: "Integrei o time de BI que migrou 25 painéis gerenciais do Excel para o Power BI; a atualização passou de semanal para diária." Mantém o papel e a atribuição ao conjunto.
- **A vaga exige SQL avançado e o corpo do currículo não o mostra.** SQL só aparece em Competências, sem nenhum bullet que o use. O perfil também não tem fato com SQL, então não há o que reescrever. É informação para o candidato: se houver um fato com SQL, ele precisa entrar no perfil-mestre antes. Não é pontuação de keyword, é o que o recrutador procura no corpo do texto.

### SUGESTÃO
- **Os 3 bullets mais fracos, em ordem:**
  1. Bullet 4: longo, com "como" demais e tecnologia irrelevante (ver acima).
  2. Bullet 3 ("Padronizei três cadastros divergentes…"): forte em número (120 mil registros, −35%), mas é o mais distante do que a vaga descreve (ruptura, giro, sell-out, reposição). Funciona como prova de "grandes volumes", mas o bullet não diz isso.
  3. Bullet 2 (painel): a escala é boa, mas o bullet é o mais curto e sem "como". Isso decorre do `[FALTA MÉTRICA]`, que é uma pergunta aberta ao candidato e não um erro de escrita.
- **Observação sobre o `[FALTA MÉTRICA]` do bullet 2:** continua em aberto para o candidato (qual foi o efeito no atraso ou na decisão?). Ele é o bullet que mais se aproxima do "acompanhamento" da vaga, então responder à pergunta teria o maior retorno.
- **Hierarquia:** o painel de aderência sugere que o bullet do painel (requisito "construção de painéis") poderia vir antes do bullet de cadastro dentro do cargo Júnior. Isso não vale no cargo atual, onde a automação em primeiro lugar é a prova mais forte. Em Júnior, o bullet 4 já fala de painéis.
- **Linha de contato:** "LinkedIn · GitHub" aparece como texto sem URL. Se for placeholder do ensaio, ignore. Num currículo real, link sem endereço gasta espaço e não paga nada.
- **Linha 3 do resumo:** "…a análise chegue a quem opera a tempo de ser usada" é aceitável, mas abstrata. Pode ficar mais concreta, sem inventar nada, ecoando "operação" e "acompanhar".
- **Expressão de transição "Entre as provas":** é enchimento na linha 2. Pode ser cortada sem perda: "Relatórios que fechavam em 3 dias passaram a fechar em 4 horas, e os erros de duplicidade de um cadastro de 120 mil registros caíram 35%."
- **Lacunas da vaga sem fato no perfil** (Supply/varejo, Databricks, inglês): não há como cobrir sem inventar. Ficam como informação para a decisão de aplicar, sem tentar disfarçar na headline.

## Cultura

**Valores lidos na vaga:**
1. `Autonomia` — evidência: "Somos um time que decide rápido e com autonomia."
2. `Velocidade de decisão` — evidência: "decide rápido"
3. `Iniciativa para melhorar processos` — evidência: "Aqui ninguém espera aprovação para melhorar um processo."
4. `Análise a serviço da decisão operacional` — evidência: "apoiar decisões de reposição das 180 lojas" (fonte 2, descrição do dia a dia)

**Mapeamento:**

| Valor | Bullet que demonstra | Como |
|---|---|---|
| Iniciativa para melhorar processos | Bullet 1: "Reduzi de 3 dias para 4 horas o fechamento de 14 relatórios semanais… ao substituir a apuração manual por rotinas em Python agendadas" | Fato de autoria: trocou um processo manual por rotina automatizada, com ganho medido. |
| Iniciativa para melhorar processos | Bullet 3: "Padronizei três cadastros divergentes num único modelo de 120 mil registros, reduzindo em 35% os erros de duplicidade" | Fato de autoria: unificou fontes divergentes e reduziu erro. |
| Velocidade de decisão | Bullet 1 (3 dias para 4 horas) e bullet 4 (atualização "de semanal para diária") | Demonstram redução de tempo de ciclo da informação. Não afirmam que a decisão ficou mais rápida, e isso não deve ser dito. |
| Análise a serviço da decisão operacional | Bullet 2: "Construí um painel de indicadores de entrega para a operação, adotado por 40 usuários recorrentes" | Painel feito para a operação e usado de forma recorrente. O efeito na decisão não está confirmado (`[FALTA MÉTRICA]`). |
| Autonomia | (cobertura parcial) bullets 1 e 3 | Os verbos de autoria mostram dono da entrega, mas nada no currículo diz que ele agiu sem aprovação ou por conta própria. |

### IMPORTANTE
- Nenhum valor central ficou sem demonstração. Autonomia tem cobertura apenas parcial, ver SUGESTÃO.

### SUGESTÃO
- **Ângulo do resumo:** "Analista de dados que troca apuração manual por rotinas em Python e entrega à operação painéis de acompanhamento, reduzindo o fechamento de relatórios de 3 dias para 4 horas." Usa só fatos presentes e aproxima o texto de "melhorar processo", "decidir rápido" e "operação".
- **Gap parcial em Autonomia — existe na vida, não está no perfil (a confirmar):** os bullets mostram autoria, mas não iniciativa própria. Se o candidato já automatizou ou padronizou algo por conta própria, sem pedido formal, vale registrar isso no perfil-mestre com a evidência. Não se deve escrever "sem aprovação" nem "por iniciativa própria" no currículo sem esse fato confirmado.
- **Limite do julgamento:** a vaga tem apenas duas frases de cultura, então a leitura é fraca. Setor e estágio não sustentaram nenhum valor (R6).
- **Nenhum gap pede bullet novo.** Os pontos fora do alcance (Supply/varejo, Databricks) são técnicos e não valores culturais. Ficam para a decisão do candidato de aplicar ou não.

## Aplicado / recusado

- Nada aplicado: o ensaio mede o painel, não pede decisão ao candidato.

Nenhuma mudança de conteúdo — reauditoria dispensada.
