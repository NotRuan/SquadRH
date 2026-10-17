# Agentes de RH

Sistema que escreve currículos orientados a vaga a partir de uma base de fatos
confirmados, e acompanha o que acontece depois do envio. A regra que sustenta
tudo: **nenhum agente cria fato.**

## Como começar

1. Instale o [Claude Code](https://claude.com/claude-code) e o Python 3 (as
   ferramentas em `tools/` usam só a biblioteca padrão; `pytest` só para os
   testes).
2. Clone este repositório e abra uma sessão do Claude Code na raiz dele.
3. A recepção abre sozinha (gancho em `.claude/settings.json`). Na primeira
   vez, escolha **Começar o primeiro acesso** — ou digite `/primeiro-acesso`.
   Ele cria `perfil/candidato.md` e o seu `perfil/perfil-mestre.md`.
4. Depois, cole uma vaga com `/nova-vaga`.

Seus dados ficam só na sua máquina: o `.gitignore` já deixa de fora o
perfil, as candidaturas, o LinkedIn modelado e os exports. Para ver o sistema
funcionando antes de usar com os seus dados, rode `/ensaio` — ele usa um
perfil fictício (`perfil/_exemplo/`).

Dependências por comando:
- `/exportar` gera .docx e .pdf com a skill `docx` do Claude.
- `/mercado` (opcional) coleta vagas por um conector de vagas configurado na
  sua conta do Claude; sem ele, ajuste o agente `coletor-mercado` às fontes
  que você tiver.

## Comandos

| Comando | Quando usar |
|---|---|
| `/inicio` | A qualquer momento — o menu. Abre sozinho em toda sessão nova |
| `/primeiro-acesso` | Na primeira vez — configura e constrói o perfil-mestre |
| `/sync-perfil` | Quando chegar um export novo do LinkedIn |
| `/sync-pos` | Quando entrar projeto ou e-book novo na pasta de estudos (opcional) |
| `/nova-vaga` | A cada vaga — cola o texto e o sistema escreve, revisa e consolida |
| `/exportar` | Quando o texto estiver aprovado — gera .docx e .pdf |
| `/apresentacao` | Quando o formulário pedir carta ou "apresente-se" |
| `/linkedin` | Quando mudar de vertente, entrar fato forte novo, ou a cada ~90 dias |
| `/entrevista` | Quando chamarem para entrevista |
| `/resultado` | A cada retorno de empresa — `/resultado cielo entrevista` |
| `/status` | De tempos em tempos — o funil e o que ele ensina |
| `/ensaio` | Depois de mudar qualquer rubrica ou revisor |
| `/mercado` | Opcional, à mão — radar do mercado de dados. Sem agendamento desde 16/10/2026 |

## Como funciona

1. **Antes de escrever**: calcula o teto de aderência da vaga contra o perfil —
   uma vaga que o perfil não atende é descoberta em três minutos, não depois de
   quatro revisores. E procura, no export do LinkedIn, quem você já conhece na
   empresa.
2. **Escrita** (sessão principal): lê a vaga, seleciona fatos do perfil,
   pergunta o que falta numa rodada só, escreve, insere palavras-chave de forma
   aditiva — uma vez cada, nunca repetindo para "reforçar".
3. **Painel** (4 revisores em paralelo): Fatos, Consistência, ATS e
   Recrutador leem o resultado e reportam — o Recrutador devolve também a
   seção Cultura. Nenhum deles edita.
4. **Consolidação**: você decide o que aplicar.
5. **Re-auditoria**: a sessão principal reconfere, sozinha, só os bullets que
   corrigiu — é o documento que você envia, e até então ninguém o tinha lido
   depois da correção.

## Onde as coisas ficam

- `CLAUDE.md` — as seis regras e a convenção de caminhos. Todo caminho no
  projeto é relativo à raiz.
- `perfil/perfil-mestre.md` — a base de fatos, mais as respostas às perguntas
  eliminatórias de formulário. Você edita este arquivo à mão.
- `perfil/candidato.md` — nome, tom, vertente, caminhos e módulos de quem usa
  o squad. Muda por pedido em linguagem livre.
- `rubricas/` — os critérios de escrita, ATS, cultura e LinkedIn.
- `linkedin/` — o perfil modelado para a vertente: diagnóstico, proposta,
  painel e o que foi publicado. Fora de `vagas/` de propósito.
- `vagas/AAAA-MM-DD-empresa-cargo/` — uma pasta por vaga: a vaga, o currículo,
  o painel e o **status**.
- `base/` — currículo genérico, ponto de partida quando não há vaga.
- `ensaio/` — a suíte de regressão. Caso fixo, perfil fictício, asserções em
  `esperado.md`.

## A trava

Um número que não existe no perfil-mestre **bloqueia** a entrega. Ou você
confirma que ele é real, ou ele sai do currículo. É o único erro que queima
numa entrevista.

## O que o sistema mede

Cada candidatura tem um `status.md`, aberto pelo `/nova-vaga`, com o canal
perguntado pelo `/exportar` e o retorno gravado pelo `/resultado`. É a única memória de resultado que existe:
sem ela o squad melhora currículo sem nunca saber se melhorou resposta. O
`/status` consolida o funil, cruza canal e score contra quem respondeu, e mostra
quais fatos do perfil nunca foram ao mercado.

Duas coisas que os benchmarks de mercado deixam claras — o funil próprio
ainda não tem amostra para confirmá-las — e que o currículo não resolve sozinho:
**indicação converte em outra ordem de grandeza que portal**, e **a maior parte
das rejeições rápidas vem das perguntas do formulário**, não do documento. Por
isso o `/nova-vaga` procura conexões e o `/exportar` fecha com o checklist
eliminatório.

## Fonte dos fatos

Três fontes, cada uma com um comando dono e uma camada exclusiva do
perfil-mestre:

- **Carreira** (experiência, formação, competências profissionais) — o export
  do LinkedIn, via `/sync-perfil`.
- **Estudo** (competências estudadas ou aplicadas em projeto acadêmico) — os
  projetos e e-books da pasta de estudos, via `/sync-pos`. Nunca vira fato
  de experiência profissional.
- **Primeiro acesso** (currículo existente e entrevista guiada) — para quem
  chega sem perfil-mestre, via `/primeiro-acesso`.

Pastas listadas em `perfil/candidato.md` → Fora do sistema (por exemplo,
currículos antigos) nunca são lidas por nenhum agente.
