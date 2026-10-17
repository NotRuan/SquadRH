# Status da candidatura

Um arquivo por vaga. É a única memória de resultado do sistema — sem ele, o
squad melhora currículo sem nunca saber se melhorou resposta.

Registre o retorno com `/resultado empresa resultado` — leva segundos. O
`/status` lê todos e consolida.

---

- **Empresa:**
- **Cargo:**
- **Data da candidatura:** AAAA-MM-DD
- **Canal:** portal | LinkedIn | indicação | recrutador me procurou | site da empresa
- **Teto de aderência:** N/100
- **Score ATS final:** N/100
- **Conexões na empresa:** nenhuma | nome — cargo
- **Indicação pedida:** não | sim, para NOME em DD/MM
- **Resultado:** aguardando | sem resposta | rejeitado | triagem | entrevista | teste | proposta | recusei | descartada | encerrada
- **Data do resultado:** AAAA-MM-DD
- **Dias até a resposta:**
- **O que aprendi:** (uma linha — o que essa candidatura ensinou sobre o
  currículo, a vaga ou o canal. Vazio é resposta válida.)

---

## Convenções

**`sem resposta`** só depois de 30 dias. Antes disso é `aguardando` — a
diferença importa no funil.

**`Canal`** é o campo que mais ensina. Portal e indicação convertem em ordens
de grandeza diferentes; sem registrar isso, o funil mistura os dois e não diz
nada.

**`descartada`** é a vaga que parou antes do envio — em geral pelo teto de
aderência do `/nova-vaga`. Não é candidatura enviada e fica fora do
denominador do funil, mas conta como dado: mostra que tipo de vaga o perfil
ainda não alcança.

**`encerrada`** é o funil fechado por decisão (ex.: proposta aceita em outra
empresa) sem retorno registrado. Também fica fora do denominador.

**`O que aprendi`** não é obrigatório e não deve ser inventado. Uma linha
honesta a cada dez candidaturas vale mais que dez linhas de suposição sobre por
que alguém não respondeu.
