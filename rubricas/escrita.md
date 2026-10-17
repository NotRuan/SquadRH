# Rubrica de escrita

Origem: prompts #1 (recrutador) e #3 (quantificador), adaptados às regras R1-R6.

## Seleção de fatos

Antes de escrever qualquer linha, escolha quais fatos do perfil-mestre entram.

1. Ordene os fatos por aderência ao que a vaga pede — não por ordem
   cronológica dentro do cargo.
2. **Regra de deduplicação:** dois fatos que compartilham o mesmo resultado
   ou o mesmo projeto viram **um só**. Entra o mais forte; o outro é
   descartado para esta vaga. Espaço gasto em eco é espaço perdido.
3. Limite prático: 4 a 5 bullets no cargo atual, 2 a 3 no anterior.
4. Um fato sem `Como sei` preenchido **não pode ser usado** (R1). Se ele for
   essencial para a vaga, pergunte — não escreva.

## Fórmula do bullet

```
[VERBO FORTE] + [O QUÊ] + [RESULTADO MENSURÁVEL] + [COMO]
```

Exemplo, a partir do fato "Automação de relatórios operacionais":

> Reduzi o fechamento de relatórios operacionais de 3 dias para 4 horas ao
> substituir a apuração manual por rotinas em Python agendadas, atendendo 6
> áreas consumidoras.

Cada bullet: uma linha e meia, no máximo duas. Se passar disso, corte o "como".

## Verbos

**Proibidos** — enfraquecem e não dizem nada:
`ajudei`, `auxiliei`, `participei de`, `trabalhei em`, `fui responsável por`,
`atuei em`, `apoiei`, `colaborei em`, `envolvido em`.

**Preferidos** — escolha pelo que você de fato fez:
- Construção: `construí`, `desenvolvi`, `implementei`, `automatizei`, `criei`
- Mudança: `reduzi`, `aumentei`, `acelerei`, `eliminei`, `padronizei`
- Condução: `liderei`, `conduzi`, `coordenei`, `articulei`

**Disciplina de escopo:** o verbo não pode ser maior que o fato. Um verbo
inflado é tão falso quanto um número inventado, e cai na primeira pergunta da
entrevista.

O teto do verbo é o campo `Escopo` do fato no perfil-mestre:

| Escopo do fato | Famílias de verbo permitidas |
|---|---|
| `autoria` — a entrega é sua | Construção e Mudança |
| `condução` — você conduziu pessoas ou uma frente | Construção, Mudança e Condução |
| `participação` — o resultado é de um conjunto do qual você fez parte | **Contribuição** |

**Contribuição** — para fato de participação: `contribuí para`, `integrei`.
O bullet nomeia o seu papel e atribui o resultado ao conjunto:

> Na gestão da rede do Sul, contribuí para elevar o aceite eletrônico de
> serviços em 20% em 3 meses.

Não é a mesma coisa que os verbos proibidos. `participei de` e `atuei em`
dizem só que você estava lá; `contribuí para elevar X em 20%` diz o que o
conjunto entregou e que parte disso é sua. É a saída honesta e ainda forte
para um fato de participação — sem ela, a única opção que sobra ao escritor é
inflar o verbo, e foi exatamente esse o BLOQUEIA mais repetido da primeira
busca (cinco vezes, sempre nos mesmos dois fatos).

Fato sem `Escopo` preenchido: o teto é o verbo do campo `O que fiz`, e a
pergunta "a entrega foi sua, você conduziu, ou fez parte?" entra na rodada
única do Passo 3 do `/nova-vaga`.

## Métricas

Toda métrica vem do campo `Resultado` ou `Escala` do fato. Nenhuma é calculada,
arredondada para cima ou estimada aqui.

**O número viaja com unidade, período, recorte e status — copiados, nunca
reinterpretados.** As palavras em volta do número se traduzem para a vaga
(R6); o número e o que o qualifica, não. Cada exemplo abaixo foi um BLOQUEIA
real da primeira busca:

| No perfil | Escrito no currículo | O erro |
|---|---|---|
| `−10%` em NPS detrator | "−10 p.p." | Unidade: variação relativa virou pontos percentuais |
| `~171,5 mil atendimentos` | "~171,5 mil atendimentos/ano" | Período inventado |
| TMC da zona SUL 1: −15,3% (projeção) | "−15,3% no tempo médio" | Recorte generalizado e projeção lida como resultado |
| projeto em aprovação | "piloto aprovado" | Status alterado |
| reuniões com o diretor de operações | "reuniões com a diretoria" | Escopo ampliado |

**Frase do anúncio não é fato.** "Orientando a decisão para geração de valor
e mitigação de riscos" copiado da vaga e pregado num bullet é afirmação sem
lastro, mesmo em volta de um número verdadeiro.

Categorias válidas — **não** apenas financeiras (R6):

| Categoria | Exemplo |
|---|---|
| Financeira | valor recuperado, custo reduzido, receita |
| Escala | registros processados, usuários, unidades, praças |
| Tempo | horas economizadas, de X para Y, frequência |
| Qualidade | erros, retrabalho, reclamações, disponibilidade |
| Adoção | áreas usuárias, recorrência de uso |
| Liderança | pessoas conduzidas, áreas articuladas |

**`Escala` e `Resultado` são independentes.** Um fato pode ter escala confirmada
e resultado desconhecido. Nesse caso o bullet **usa a escala** e marca só o
resultado:

> Construí um painel de indicadores de entrega para a operação, adotado por 40
> usuários recorrentes. `[FALTA MÉTRICA]`

Descartar a escala junto com o resultado joga fora informação verdadeira e
enfraquece o bullet sem necessidade.

Faltando a métrica: escreva o bullet com o que existe e marque ao final
`[FALTA MÉTRICA]`. Nunca invente, nunca use "significativo", "expressivo",
"considerável" — advérbio não é métrica.

## Resumo profissional

Três linhas. Quatro só se a quarta ganhar espaço de outra seção.

- Linha 1: quem você é profissionalmente + o que a vaga procura
- Linha 2: as duas ou três provas mais fortes, com números
- Linha 3: para onde você está indo / o que busca

Sem adjetivo sobre si mesmo sem prova ao lado. "Altamente analítico" não diz
nada; "reduzi o fechamento de 3 dias para 4 horas" diz.

**O resumo não pode ser eco dos bullets.** O número pode se repetir; a frase,
não. Se a linha 2 do resumo repete palavra por palavra o bullet que vem logo
abaixo, o leitor lê a mesma prova duas vezes em 6 segundos e sai com uma prova
só — e num currículo de 5 bullets isso desperdiça metade do documento.

O resumo **destila**: diz o que a pessoa faz acontecer, e usa o número como
evidência resumida. O bullet **narra**: traz o como, a escala e o contexto.
Registros diferentes, mesma verdade.

Todo número que aparecer aqui sai do perfil-mestre, como em qualquer bullet —
o resumo não é área livre.

## Vocabulário (R6)

O vocabulário vem da **vaga**, não do histórico. Antes de escrever, liste 5 a 8
termos que a vaga usa para nomear as coisas e use esses termos.

Uma vaga de varejo diz ruptura, giro, sell-out, praça. Uma de tecnologia diz
latência, deploy, incidente, SLA. Uma de saúde diz desfecho, adesão, protocolo.
O mesmo fato é contado no idioma de quem lê.

### Vocabulário não é domínio

Aqui mora a única tensão real entre R6 e R1, e ela derruba currículo:

> Adotar o vocabulário da vaga é reescrever **um fato que existe** com as
> palavras de quem lê. Não é afirmar experiência num domínio que o perfil não
> tem.

O teste é uma pergunta só: **se o recrutador disser "me conta sobre isso", há
um fato no perfil para responder?**

- ✅ O perfil diz "painel de indicadores de entrega para a operação"; a vaga
  fala em acompanhamento. Escrever "painel de acompanhamento da operação" é
  tradução — muda o nome, o fato é o mesmo.
- ❌ O mesmo perfil não diz que efeito o painel teve. Escrever "painel usado
  na decisão da operação" afirma um resultado que não está confirmado.
  **Traduz-se o objeto e o destinatário do fato, nunca o efeito** (decisão de
  17/10/2026): efeito só entra com `Resultado` confirmado.
- ❌ O perfil não tem nenhum fato de Supply, estoque ou giro. Escrever
  "Analista de Dados | Supply" na headline é reivindicar um domínio inexistente
  — e a primeira pergunta da entrevista fica sem resposta.

Isto vale em dobro para a **headline**: ela é a primeira coisa lida e a mais
fácil de inflar.

**A headline só usa títulos que o candidato ocupou** (decisão de 16/10/2026).
Um título ocupado é um cargo do perfil-mestre, inteiro ou uma das partes do
nome ("Analista de Dados & Inteligência Operacional" sustenta "Analista de
Dados"), sem a senioridade. Se a vaga se chama "Analista de BI" e o candidato
nunca teve esse cargo, a headline usa o título que ele teve e mais próximo da
vaga — o vocabulário de BI entra nos bullets, onde há fato, e não no título.
"Nomes diferentes para a mesma função" não é lastro: o recrutador lê o título
como cargo ocupado, e a pergunta "quando você foi Analista de BI?" fica sem
resposta.

A headline também **não** pode anexar uma área, um setor ou um domínio que
nenhum fato sustenta.

**Nunca leia as pastas em `perfil/candidato.md` → Fora do sistema.**
Currículos antigos arrastam o jargão do ramo em que foram escritos para uma
vaga de outro setor.

## Estrutura do documento

Ordem fixa, nomes fixos (R3):

1. Nome
2. Headline (só títulos ocupados — ver "Vocabulário não é domínio")
3. Linha de contato: cidade · telefone · e-mail · LinkedIn · GitHub
4. `RESUMO PROFISSIONAL`
5. `EXPERIÊNCIA PROFISSIONAL`
6. `FORMAÇÃO ACADÊMICA`
7. `COMPETÊNCIAS`

O **cargo dentro da experiência nunca muda** para agradar a vaga. Só a headline
do topo se adapta.
