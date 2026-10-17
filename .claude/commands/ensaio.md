---
description: Roda a suíte de regressão do sistema — o caso fixo do ensaio, comparado com o comportamento esperado
---

Você verifica se o sistema ainda se comporta como deve. Rode isto **depois de
mudar qualquer rubrica, revisor ou comando**.

Uma edição em `rubricas/` muda o comportamento de quatro agentes de uma vez, e
nada mais no sistema avisa se piorou. O currículo só é conferido por julgamento
de modelo — sem um caso fixo, uma regressão só aparece numa candidatura real.

Todos os caminhos são relativos à raiz do projeto (ver `CLAUDE.md`).

## Passo 0 — O caso

`ensaio/vaga.md` é uma vaga fixa e versionada. `ensaio/esperado.md` diz o que o
sistema **deve** fazer com ela. `ensaio/curriculo.md` e `ensaio/painel.md` são a
última saída registrada.

A régua do ensaio é **`perfil/_exemplo/perfil-exemplo.md`**, um perfil
fictício — não o `perfil-mestre.md` do candidato. É o que torna o caso estável: o
perfil real cresce a cada vaga, e um teste cuja entrada muda toda semana não
mede regressão nenhuma.

Leia `ensaio/esperado.md` inteiro antes de qualquer coisa.

## Passo 1 — Rodar

Rode o fluxo do `/nova-vaga` sobre `ensaio/vaga.md`, com quatro diferenças:

- **A base de fatos é `perfil/_exemplo/perfil-exemplo.md`, e o candidato é
  `perfil/_exemplo/candidato-exemplo.md`.** Não abra o
  `perfil-mestre.md` em momento nenhum desta execução — nem para ler.
- **Não crie pasta em `vagas/`.** O ensaio não é candidatura e não entra no
  funil.
- **Não escreva em `perfil/`.** Nem `Já usado em`, nem métrica nova. Um comando
  de teste que altera a própria entrada deixa de medir a mesma coisa na segunda
  vez.
- **Não pergunte métrica faltante.** Onde faltar, deixe `[FALTA MÉTRICA]` — é
  precisamente um dos comportamentos sob teste.

Escreva em `ensaio/curriculo-novo.md`, `ensaio/mapa-novo.md` e
`ensaio/painel-novo.md`.

## Passo 2 — Conferir contra o esperado

Para cada asserção de `ensaio/esperado.md`, diga **passou** ou **falhou**, com
a evidência — o trecho do currículo ou do painel que sustenta o veredito.

Não arredonde a favor. Uma asserção que passou "quase" falhou.

## Passo 3 — Comparar com a saída anterior

Compare `curriculo-novo.md` com `curriculo.md` e os dois painéis.

Diferença **não é** falha por si só — o sistema deve melhorar. Classifique cada
uma:

- **Melhora** — a mudança de rubrica surtiu o efeito pretendido
- **Regressão** — algo que funcionava parou
- **Neutra** — variação de redação sem consequência

A terceira classe é a maior e a menos interessante. Não gaste relatório com ela
além de contá-la: dois modelos rodando o mesmo prompt escrevem frases
diferentes, e isso não é sinal.

## Passo 4 — Relatar

```
asserções    N   passou N · falhou N
diferenças   melhora N · regressão N · neutra N
```

Liste as falhas e as regressões, cada uma com a asserção violada e a evidência.

Se tudo passou, diga isso em uma linha. Não invente ressalva para parecer
rigoroso.

## Passo 5 — Promover, só se o candidato mandar

Se a saída nova é melhor e o candidato aprovar, substitua `ensaio/curriculo.md` e
`ensaio/painel.md` pelas novas e apague os `-novo`. É isto que faz a próxima
rodada comparar contra o estado atual, não contra um estado antigo.

**Não promova sozinho.** Promover uma regressão a novo padrão apaga o sinal
justamente quando ele aparece.

## Caso do mercado

Rode `python -m pytest tools/test_mercado.py -v`. Todos os testes devem passar.
Isto trava a lógica determinística do `/mercado` (contagem e tendência): se um
número mudou, a análise de mercado regrediu e o relatório vai mentir tendência.

## Caso da Pós-FIAP

Rode `python -m pytest tools/test_ler_pos.py -v`. Todos os testes devem
passar — trava a varredura, o diff contra o cache e a leitura de
projeto/notebook do `/sync-pos`.

Depois, confira `ensaio/pos-fiap/esperado.md` contra a fixture congelada em
`ensaio/pos-fiap/01_Projetos/projeto-exemplo/`: rode `--listar`, `--ler` e
`--marcar` como o arquivo descreve, e confirme que os três comportamentos
batem. Use um cache temporário (fora de `perfil/`) — este caso não escreve em
`perfil/pos-fiap-cache.json`, o cache real do candidato.

## Caso do LinkedIn

Leia `ensaio/linkedin/esperado.md` e rode o que ele descreve. Para cada
asserção (L1 a L7), diga **passou** ou **falhou**, com a evidência. Confira os
números de L1 e L2 rodando `tools/score_linkedin.py` sobre a fixture.

## Caso da troca de nome

Rode `grep -rn "R[u]an\|ru[a]ni" .claude rubricas ensaio`. A saída deve ser vazia: os
prompts falam do "candidato" e leem nome e caminhos de `perfil/candidato.md`.
Qualquer linha é regressão. (Os colchetes no padrão impedem que esta própria
linha case com a busca.)

## Regras

- Este comando **não escreve** em `perfil/`, `vagas/` nem `rubricas/`. Só em
  `ensaio/` (inclusive `ensaio/linkedin/`).
- Se `ensaio/esperado.md` não existir, pare e reporte — sem asserções não há
  teste, só uma segunda opinião.
- Português do Brasil.
