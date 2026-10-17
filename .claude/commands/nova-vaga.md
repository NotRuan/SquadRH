---
description: Escreve um currículo para a vaga colada, aciona o painel de 4 revisores e consolida os achados
---

Você é o orquestrador do sistema de currículos. Siga esta ordem à risca.

Todos os caminhos são relativos à raiz do projeto (ver `CLAUDE.md`).

Vaga colada: $ARGUMENTS

## Passo 0 — Pré-requisitos

1. Se `$ARGUMENTS` estiver vazio, peça o texto da vaga e **pare** até recebê-lo.
2. Confirme que `perfil/candidato.md` existe e que `perfil/perfil-mestre.md`
   tem pelo menos um fato com `Como sei: confirmado por` (o mesmo critério da
   recepção). Senão, diga ao candidato para rodar `/primeiro-acesso` primeiro e
   **pare**.
3. Leia as duas rubricas por completo: `rubricas/escrita.md` e
   `rubricas/ats.md`. As regras delas vencem qualquer instrução deste
   arquivo. (`rubricas/cultura.md` é lida pelo `revisor-recrutador` no
   Passo 6 — o orquestrador não precisa dela.)
4. Crie a pasta `vagas/AAAA-MM-DD-empresa-cargo/` (data de hoje, empresa e
   cargo em minúsculas com hífen) e grave `vaga.md` com o texto recebido.
5. **Histórico com esta empresa.** Verifique se já existe pasta anterior em
   `vagas/` com o mesmo nome de empresa **e com `curriculo.md`** (uma pasta
   `descartada` só tem `vaga.md` e `status.md` — não há currículo a contradizer).
   Havendo, leia o currículo anterior e
   avise o candidato — o novo não pode contradizer o que já foi enviado em cargo,
   datas e números. Mudança de ângulo é legítima; mudança de fato não é.
   O `revisor-consistencia` confere isso de novo no Passo 6, mas você precisa
   saber disso **antes** de escrever.

   **Não leia** nenhuma pasta listada em `perfil/candidato.md` → Fora do
   sistema. Não são fonte de fato nem de vocabulário.

   **Não leia** `base/` nem `ensaio/` como candidatura anterior — não são.

6. **Material pendente na pasta de estudos.** Se o módulo `/sync-pos`
   estiver ligado no `perfil/candidato.md`, rode
   `python tools/ler_pos.py --raiz "<Pasta de estudos do candidato.md>" --cache perfil/pos-fiap-cache.json --listar`
   Desligado: pule este item. É só comparação de data/tamanho, não lê PDF nem pergunta nada. Guarde a
   saída para o aviso do Passo 8. **Não bloqueia** o fluxo — mesmo com
   material pendente, siga escrevendo o currículo com o perfil-mestre como
   está.

## Passo 1 — Ler a vaga

Extraia e registre no início do seu raciocínio:
- Requisitos obrigatórios vs desejáveis
- As três listas de keywords (rubrica ATS)
- Senioridade pedida
- O ângulo: a vaga é mais de dados, de produto, de automação ou de negócio?
- 5 a 8 termos de vocabulário da vaga (R6) — é o idioma em que você vai
  escrever
- **As perguntas eliminatórias** que o formulário provavelmente fará: pretensão
  salarial, modelo de trabalho, disponibilidade, inglês, formação exigida, CNH,
  PCD. Anote as que a vaga menciona.

## Passo 1.5 — Aderência, antes de escrever

Barato e vai na frente de propósito: escrever e revisar uma vaga que o perfil
não atende custa quatro agentes para descobrir o que três minutos de conta já
diziam.

Calcule o **teto de aderência** com a fórmula da rubrica ATS ("Score de match",
inclusive a redistribuição de peso quando uma lista estiver vazia), contando
como "presente" toda keyword das três listas que tenha lastro em algum fato do
`perfil-mestre.md` — estando ou não no currículo, que ainda não existe. É o
melhor score que esta vaga pode alcançar, e é na mesma escala N/100 dos limites
abaixo.

Reporte em duas linhas:

> Teto de aderência: N/100 — X de Y obrigatórias, X de Y desejáveis e X de Y de
> contexto têm lastro no perfil. Sem lastro: `termo`, `termo`, `termo`.

- **Teto abaixo de 55:** pare e pergunte se vale seguir. Mostre o que falta.
  O candidato decide — pode haver motivo que não está na conta (a empresa, o time, o
  momento). **Não decida sozinho por ele, e não siga sem resposta.**

  Se o candidato decidir não seguir, grave o `status.md` da pasta a partir de
  `vagas/_modelo-status.md` com `Resultado: descartada`, o teto, a data de
  hoje em `Data do resultado` e, em `O que aprendi`, as obrigatórias sem
  lastro. Pare aí. Uma pasta só com `vaga.md` parece fluxo abandonado; com o
  status, vira dado — o `/status` passa a mostrar que tipo de vaga o perfil
  ainda não alcança.
- **Teto entre 55 e 70:** avise, e siga sem esperar.
- **Acima de 70:** siga direto.

## Passo 1.6 — Quem eu conheço lá dentro

Uma indicação converte muito acima de uma candidatura por portal — e o dado já
está no export do LinkedIn. É o passo mais barato de toda a candidatura.

Se houver um zip do LinkedIn na pasta `Downloads (zip do LinkedIn)` do
`perfil/candidato.md`, rode:

```
python "tools/ler_linkedin.py" --zip CAMINHO --empresa "NOME DA EMPRESA"
```

- Achou conexões: liste nome, cargo e data da conexão, e sugira que o candidato fale
  com elas **antes** de enviar pelo portal. Registre no `status.md` (Passo 4.5).
- Não achou, ou não há export disponível: diga isso em uma linha e siga. Não
  transforme em bloqueio, e não invente contato nenhum.

## Passo 2 — Selecionar fatos

Aplique "Seleção de fatos" da rubrica de escrita ao `perfil-mestre.md`.
Aplique a regra de deduplicação: dois fatos com o mesmo resultado ou projeto
viram um só.

Prefira, em empate de aderência, o fato com `Já usado em` mais vazio — um fato
forte que nunca saiu do perfil não está sendo testado no mercado.

Mostre ao candidato a lista selecionada, em uma linha cada, antes de escrever.

## Passo 3 — Perguntar, uma vez só

Junte **todas** as métricas faltantes numa única rodada, em português,
agrupadas por empresa e cargo. Nunca pergunte de bullet em bullet.

Na mesma rodada, para cada fato selecionado sem `Escopo` preenchido, pergunte:
a entrega foi sua, você conduziu, ou fez parte? Grave a resposta no fato.

Se não faltar nada, diga isso e siga.

As respostas vão para o `perfil-mestre.md` — acrescente o fato ou preencha o
campo, e registre a data no campo `Como sei`. É isto que faz a próxima vaga
perguntar menos.

## Passo 4 — Escrever

Escreva `curriculo.md` seguindo a rubrica de escrita: estrutura fixa, resumo de
3 linhas, fórmula do bullet, verbos permitidos, vocabulário da vaga.

**Todo número sai do perfil-mestre.** Sem métrica, o bullet termina em
`[FALTA MÉTRICA]`.

Junto com o currículo, grave `mapa.md` na pasta da vaga — uma linha por bullet
e uma por número do resumo:

```
# Mapa bullet → fato

| Onde | Início do bullet | Fato (título no perfil) | Número como está no perfil | Escopo do fato | Verbo usado |
|---|---|---|---|---|---|
| Resumo | "Analista de dados com..." | Automação de relatórios | de 3 dias para 4 horas | autoria | — |
| ACME atual, bullet 1 | "Construí um painel..." | Painel de acompanhamento de entregas | 40 usuários recorrentes | autoria | construí |
```

A coluna "Número como está no perfil" é **cópia literal** do campo
`Resultado`/`Escala`, com unidade, período e recorte (rubrica de escrita,
"Métricas"). Se o número no bullet não é idêntico ao da coluna, o erro está no
bullet. O verbo usado tem de caber no `Escopo` (rubrica, "Disciplina de
escopo").

Escrever o mapa é a sua autoconferência antes do painel: os erros que o
`revisor-fatos` mais barrou na primeira busca — unidade trocada, período
inventado, verbo maior que o escopo — aparecem aqui antes de custar um
BLOQUEIA. O mapa é atualizado sempre que um bullet mudar (Passos 5 e 7).

## Passo 4.5 — Abrir o status

Grave `status.md` na pasta da vaga, a partir do modelo em
`vagas/_modelo-status.md`. Preencha o que você já sabe: data, empresa, cargo,
canal, teto de aderência, conexões encontradas no Passo 1.6.

O campo `Resultado` nasce como `aguardando`. É o `/status` que consolida isso
depois — sem este arquivo, a candidatura não existe no funil.

## Passo 5 — Inserir keywords

Etapa separada, **estritamente aditiva** (rubrica ATS). Classifique cada
keyword antes de inserir. Ausente do perfil = não insere, vira gap.

Não troque verbos. Não reordene frases. Não mexa em número nenhum.

**Uma vez basta.** ATS moderno pontua relevância no contexto, não frequência —
repetir o termo para reforçar derruba o score em vez de subir.

## Passo 6 — Painel

Invoque os revisores em paralelo, numa única mensagem, passando a cada um o
caminho da pasta da vaga:

- `revisor-fatos`
- `revisor-consistencia` — **só se o item 5 do Passo 0 achou candidatura
  anterior a esta empresa (pasta com `curriculo.md`)**
- `revisor-ats`
- `revisor-recrutador` (devolve também a seção Cultura)

**Por que o Consistência é condicional.** Se o `revisor-fatos` garante que todo
número vem do perfil-mestre, dois currículos não têm como divergir em número
— e nas 11 rodadas em que ele rodou sem candidatura anterior à mesma empresa,
não encontrou contradição nenhuma. O que só ele enxerga é a mesma empresa:
cargo, datas e ângulo contra o que aquele recrutador já viu, e a densidade de
candidaturas. Sem candidatura anterior, ele gasta a leitura de cinco
currículos para confirmar o que o Fatos já garantiu.

Consequência aceita: sem candidatura anterior à empresa, a checagem de número
entre empresas diferentes também não roda — ela cabe ao `revisor-fatos`, que
garante o lastro de todo número no perfil-mestre.

Sem candidatura anterior à empresa, escreva você mesmo a seção no
`painel.md`, no lugar dele:

```
## Consistência

Não acionado: nenhuma candidatura anterior a esta empresa em `vagas/`.
```

Junte as saídas em `painel.md`, na ordem acima — Fatos e Consistência
primeiro, porque são os dois que podem bloquear a entrega. O
`revisor-recrutador` devolve duas seções markdown (`## Recrutador` e
`## Cultura`) numa única resposta — copie as duas para `painel.md`, na ordem
em que ele as devolveu.

**Não filtre nem reescreva o que os revisores disseram.** O `painel.md` guarda
o julgamento deles, verbatim. Sua opinião sobre um achado entra na
consolidação, não no relatório.

## Passo 7 — Consolidar

Apresente ao candidato, em pt-BR:

1. **BLOQUEIA** — em destaque, com a pergunta correspondente. Um número sem
   lastro tem duas saídas apenas: o candidato confirma que é real (e você registra no
   perfil-mestre com a data) ou o número sai do currículo. **Não há terceira
   opção e você não decide sozinho.**
2. **IMPORTANTE** — lista numerada, cada item com a correção proposta.
3. **SUGESTÃO** — resumidas em uma linha cada.
4. **Conflitos entre revisores** — se o ATS pede mais keyword e o Recrutador
   pede menos texto, apresente o conflito. Não resolva sozinho.

Espere a decisão do candidato. Aplique só o que ele aprovar. Reescreva
`curriculo.md` e registre no fim de `painel.md`, **sempre** — inclusive quando
nada foi aplicado:

```
## Aplicado / recusado

- Aplicado: (achado — revisor — o que mudou)
- Recusado: (achado — revisor — motivo dado pelo candidato, ou "sem motivo")
```

**Um BLOQUEIA só conta como resolvido se aparecer em "Aplicado"** — com o
prefixo `BLOQUEIA resolvido:` e o que mudou (número confirmado e registrado no
perfil-mestre com a data, ou número removido). O `painel.md` guarda o
BLOQUEIA verbatim; é este registro que o `/exportar` lê para saber que ele foi
tratado. BLOQUEIA recusado ou sem registro continua bloqueando.

É a única memória do que o candidato rejeita. Sem ela, um tipo de sugestão recusado
em toda vaga continua sendo feito em toda vaga, e ninguém percebe que a
rubrica é que precisa mudar. Na primeira busca, só 5 de 33 painéis tinham
esse registro.

**Não rode o painel inteiro de novo depois de aplicar as correções**, a menos
que o candidato peça. Um segundo ciclo completo gasta tokens e tende a produzir uma
nova rodada de sugestões de estilo sem fim.

## Passo 7.5 — Re-auditoria de fatos (inline, sem novo agente)

O documento que o candidato envia é o **de depois**, e até aqui ninguém o auditou.
Uma correção aplicada às pressas pode ter mexido num número ou inflado um
verbo. Você mesmo faz essa checagem agora — sem invocar um agente novo,
porque você acabou de fazer a edição e já sabe exatamente o que mudou.

1. Liste os bullets que você editou no Passo 7.
2. Nenhum bullet de conteúdo mudou (só houve recusas, ou a mudança não tocou
   número nem verbo): registre no fim de `painel.md` — "Nenhuma mudança de
   conteúdo — reauditoria dispensada." — e siga para o Passo 8.
3. Para cada bullet editado, atualize a linha dele no `mapa.md` e confira
   contra o fato daquela linha:
   - O número do bullet bate com o valor do fato no perfil-mestre — sem
     arredondar, sem derivar.
   - O verbo não é maior do que o fato descreve e cabe no `Escopo` dele
     (`liderei` exige liderança escrita no fato; `arquitetei` exige desenho,
     não uso; fato de `participação` só aceita Contribuição).
   - Se o bullet editado não tem fato citado no Passo 2 para confirmar,
     releia no `perfil-mestre.md` só a linha do fato em questão (não o
     arquivo inteiro) antes de concluir. **Nunca aprove por falta de
     informação.**
4. Limpo: registre no fim de `painel.md` — "Re-auditoria de fatos após
   correções: limpa (escopo: N bullets revisados)." — e siga.
5. Achado: leve ao candidato. **Não exporte por cima disso.**

## Passo 8 — Fechar

Relate:
- Fatos usados / disponíveis no perfil
- Score ATS com a conta aberta, e o teto de aderência do Passo 1.5
- `[FALTA MÉTRICA]` restantes
- Quantas perguntas foram feitas — e quantas o perfil já respondeu sozinho
- Conexões na empresa, se houve
- Resultado da re-auditoria
- Se o Passo 0 encontrou material novo/mudado na Pós, avise: "N arquivo(s)
  novo(s) na Pós-FIAP ainda não sincronizados — rode /sync-pos se quiser que
  entrem no perfil antes da próxima vaga." Se não encontrou nada, não
  mencione — silêncio aqui não é omissão, é "nada pendente".
- Lembre de responder as perguntas eliminatórias do Passo 1 no formulário — é
  onde mais candidatura morre, e nenhum revisor cobre isso
- Sugira `/exportar` se não houver BLOQUEIA aberto

Atualize o campo `Já usado em` de cada fato usado, no `perfil-mestre.md`.

## A regra que vence tudo

Nenhum agente cria fato. Se a única forma de avançar for inventar um número,
uma ferramenta ou um verbo mais forte que o real, **não faça** — pare e
pergunte.
