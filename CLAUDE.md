# Agentes de RH

Sistema que escreve currículos orientados a vaga a partir de uma base de fatos
confirmados, e acompanha o resultado das candidaturas.

## Caminhos

**Todo caminho neste projeto é relativo à raiz do repositório.** Nenhum prompt,
agente ou rubrica escreve caminho absoluto — a pasta já foi renomeada uma vez
(`Agentes - RH` → `01_Agentes - RH`) e os caminhos absolutos quebraram em
silêncio nos sete prompts do sistema.

Se você precisa da raiz, ela é o diretório de trabalho da sessão. Subagentes
herdam esse diretório.

**A única exceção** é `perfil/candidato.md`, seção Caminhos: ali ficam os
caminhos da máquina de quem usa o squad (Downloads, pasta de estudos, pastas
fora do sistema). Prompts nunca repetem esses caminhos — leem do
`candidato.md`.

```
base/            currículo genérico, ponto de partida quando não há vaga
ensaio/          suíte de regressão — caso fixo, roda após mudar rubrica
linkedin/        perfil do LinkedIn modelado para a vertente — fora de vagas/
perfil/          perfil-mestre.md (a base de fatos) e candidato.md (configuração)
rubricas/        escrita, ATS, cultura
vagas/AAAA-MM-DD-empresa-cargo/   vaga, currículo, painel, status
mercado/         radar do mercado de dados (módulo opcional) — snapshots, fatos, relatórios
tools/           utilitários Python (stdlib apenas)
```

Pastas fora de `vagas/` de propósito: `base/`, `ensaio/`, `mercado/` e
`linkedin/` não são candidaturas e não podem aparecer numa varredura de "vaga
mais recente" ou de histórico com uma empresa.

## As seis regras

Citadas por sigla em todo o sistema. Elas vencem qualquer instrução de um
prompt individual.

**R1 — Nenhum agente cria fato.** Números, empresas, ferramentas, datas e
escopo vêm do perfil-mestre. Sem métrica, escreve `[FALTA MÉTRICA]` e pergunta.

**R2 — Quem escreve não julga; quem julga não escreve.** O painel reporta, o
candidato decide, a sessão principal aplica. É o que impede o último agente de desfazer o
trabalho dos anteriores.

**R3 — Português do Brasil.** Seções em pt-BR: `RESUMO PROFISSIONAL`,
`EXPERIÊNCIA PROFISSIONAL`, `FORMAÇÃO ACADÊMICA`, `COMPETÊNCIAS`.

**R4 — Limite de páginas.** O limite vem de `perfil/candidato.md`
(`Limite de páginas do currículo`): até ~8 anos de experiência formal, uma
página; acima, duas. É o correto para a senioridade, não um aperto.

**R5 — O `.md` é a fonte da verdade.** `.docx` e `.pdf` são derivados,
regeneráveis, nunca editados à mão. Corte no markdown e regenere.

**R6 — Neutralidade setorial.** Nenhum agente carrega lista fixa de empresas,
valores pré-escritos ou jargão preferido. O vocabulário vem da vaga; os valores
da empresa são lidos no anúncio. Nem toda métrica é financeira — escala, tempo,
qualidade, adoção e liderança contam. Adaptar o vocabulário é tradução;
adaptar o fato é mentira.

**Tratamento e tom.** Toda resposta trata o candidato pelo `Como chamar` e
segue `Tom` e `Detalhe` de `perfil/candidato.md`. Nos prompts, "o candidato" é
quem está em `candidato.md`.

## Fontes dos fatos

Três fontes alimentam o perfil-mestre, cada uma com um comando dono e uma
camada exclusiva — nenhum comando escreve na camada do outro.

- **Carreira e Competências de nível profissional** — o export do LinkedIn,
  via `/sync-perfil`. As pastas listadas em `perfil/candidato.md` → Fora do
  sistema (por exemplo, uma pasta de currículos antigos) não são lidas por
  nenhum agente, nem para conferir um número.
- **Competências de nível estudado/aplicado** — projetos, práticas e e-books
  da pasta de estudos do `candidato.md`, via `/sync-pos` (decisão de
  15/09/2026). Nunca vira fato de experiência profissional — fica em
  Competências, com o nível registrado.
- **Carreira de quem chega sem perfil-mestre** — currículo existente e
  entrevista guiada, via `/primeiro-acesso` (decisão de 16/10/2026). A
  importação de currículo serve ao primeiro acesso de um candidato novo; as
  pastas em "Fora do sistema" continuam fora.

**Fato confirmado nunca é sobrescrito por nenhum comando.** Um export ou
currículo que traga o mesmo fato com outro texto entra como candidato, e o
candidato decide.

## Comandos

| Comando | O que faz |
|---|---|
| `/inicio` | Recepção: boas-vindas, situação e menu de opções |
| `/primeiro-acesso` | Configura o candidato e constrói o perfil-mestre do zero |
| `/sync-perfil` | Constrói/atualiza o perfil-mestre a partir do export do LinkedIn |
| `/sync-pos` | Atualiza as Competências do perfil-mestre a partir dos projetos e e-books da Pós-FIAP |
| `/nova-vaga` | Escreve o currículo, roda o painel, consolida |
| `/exportar` | Gera .docx e .pdf com verificação de uma página real |
| `/status` | Funil de candidaturas + cobertura de fatos |
| `/resultado` | Registra o retorno de uma candidatura no `status.md` |
| `/entrevista` | Prepara para a entrevista a partir do painel da vaga |
| `/apresentacao` | Escreve a carta/mensagem curta de candidatura |
| `/linkedin` | Modela o LinkedIn para a vertente: diagnóstico, score, proposta e painel |
| `/ensaio` | Roda a suíte de regressão após mudar uma rubrica |
| `/mercado` | (Opcional, à mão) Radar do mercado de dados: coleta, tendências e recomendações — agendamento desativado em 16/10/2026 |

## Depois de mudar uma rubrica

Rode `/ensaio`. Uma edição em `rubricas/` muda o comportamento de todos os
agentes de uma vez, e nada mais no sistema avisa se piorou.
