---
description: Registra em segundos o retorno de uma candidatura no status.md da vaga
---

Você registra o que aconteceu com uma candidatura. É o comando mais curto do
sistema, e de propósito: o `/status` só mede o que alguém registrou, e um
registro que custa mais de um minuto não acontece. Foi assim que 21 de 37
candidaturas terminaram com `Resultado: A PREENCHER`.

Todos os caminhos são relativos à raiz do projeto (ver `CLAUDE.md`).

Entrada: $ARGUMENTS

Formato esperado, em linguagem livre: empresa (ou trecho do nome da pasta),
resultado e, opcionalmente, data e canal. Exemplos:
`cielo entrevista`, `nestle rejeitado 2026-10-02`, `porto triagem canal indicação`.

## Passo 0 — Achar a vaga

1. Se `$ARGUMENTS` estiver vazio, pergunte empresa e resultado em uma linha só e
   **pare** até receber.
2. Procure em `vagas/` as pastas cujo nome contém a empresa. Ignore
   `vagas/_modelo-status.md`, `base/` e `ensaio/`.
   - **Uma pasta:** siga.
   - **Mais de uma:** liste com data e cargo e pergunte qual. Não escolha pela
     mais recente: candidaturas à mesma empresa em cargos diferentes são
     comuns, e gravar na errada estraga as duas.
   - **Nenhuma:** diga isso e pare. Não crie pasta retroativa.

## Passo 1 — Normalizar o resultado

O valor gravado é sempre um dos do modelo (`vagas/_modelo-status.md`):
`aguardando`, `sem resposta`, `rejeitado`, `triagem`, `entrevista`, `teste`,
`proposta`, `recusei`, `descartada`, `encerrada`.

Traduza a fala para o valor ("me chamaram pra conversar com o RH" → `triagem`;
"caso técnico" → `teste`). Se a fala não cabe em nenhum, pergunte — não
force.

## Passo 2 — Gravar

Edite só o `status.md` da pasta escolhida:

- **Resultado** — o valor normalizado. Se já havia um resultado anterior que
  não era `aguardando`, preserve a trajetória: `entrevista (antes: triagem em
  2026-09-20)`. A ordem em que as etapas aconteceram é dado do funil.
- **Data do resultado** — a informada, ou hoje.
- **Dias até a resposta** — `Data do resultado − Data da candidatura`, em dias.
  Se `Data da candidatura` não estiver preenchida, deixe em branco e avise.
- **Canal** — se veio na entrada, grave. Se o campo está vazio ou
  `A PREENCHER` e não veio, **pergunte uma vez**, com as opções do modelo.
  Sem resposta, deixe como está.

Não toque em nenhum outro campo, nem em outro arquivo.

## Passo 3 — Relatar

Uma linha: pasta, resultado gravado, dias até a resposta.

Se o resultado é `entrevista` ou `teste`, sugira `/entrevista` com a pasta.
Se é `proposta`, pergunte se as demais candidaturas `aguardando` devem virar
`encerrada` — e só faça isso com um "sim" explícito.

## Regras

- `O que aprendi` só se o usuário disser algo que caiba ali. Nunca deduza a
  causa de uma rejeição: "provavelmente foi o inglês" sem evidência é a
  suposição que o modelo de status pede para não registrar.
- Português do Brasil.
