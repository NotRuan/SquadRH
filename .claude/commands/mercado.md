---
description: (Opcional) Radar do mercado de vagas de dados — coleta, tendências e recomendações
---

Módulo opcional, rodado à mão — o agendamento semanal está desativado desde
16/10/2026. Nenhum outro comando depende
dele.

Você produz o radar semanal do mercado de dados. Todos os caminhos são
relativos à raiz do projeto (ver `CLAUDE.md`). As seis regras vencem qualquer
instrução daqui — em especial **R1** (todo número rastreia até uma vaga real;
sem amostra, `[AMOSTRA INSUFICIENTE]`) e **R2** (você propõe, não edita
`perfil/` nem `rubricas/`).

Rótulo da rodada: ano + semana ISO de hoje, no formato `AAAA-Sxx`.

## Passo 0 — Ler o recorte
Leia `mercado/config.md`. Se não existir, pare e avise.

## Passo 1 — Coletar (coleta ≠ julgamento)
Dispare um subagente `coletor-mercado` por fonte, **em paralelo**: um para o
Indeed (MCP) e um para cada fonte web listada na config. Cada um devolve blocos
de vaga no formato do snapshot.

## Passo 2 — Gravar o snapshot
Concatene os blocos devolvidos em `mercado/snapshots/AAAA-Sxx.md`, com o
cabeçalho do gabarito `mercado/_modelo-snapshot.md`. Este arquivo é a evidência
bruta — não o edite para "melhorar" nada.

## Passo 3 — Atualizar a série temporal
Rode o tool determinístico (não conte termos à mão):

```bash
python tools/mercado.py atualizar --snapshot mercado/snapshots/AAAA-Sxx.md --fatos mercado/fatos-mercado.md --coluna AAAA-Sxx
```

Depois, se houver termos com categoria `?` em `fatos-mercado.md`, preencha a
categoria (ferramenta/linguagem/conceito/senioridade/setor/modelo de trabalho)
com base no que o termo é. Não mexa nas frações — elas são do tool.

## Passo 4 — Analisar
Leia `mercado/fatos-mercado.md`. Só afirme tendência (subiu/caiu) se houver
**≥2 colunas de rodada**. Com uma só: "primeira rodada, sem base de tendência".
Leia `perfil/perfil-mestre.md` (**apenas leitura**) e liste os termos quentes
(fração alta) que o perfil não registra.

## Passo 5 — Escrever o relatório
Escreva `mercado/relatorio-AAAA-Sxx.md` seguindo `mercado/_modelo-relatorio.md`:
panorama, movimento, gap contra o perfil, recomendações. Cada recomendação
carrega a fração que a sustenta e é **sugestão** — você não edita perfil nem
rubrica. Separe contagens do Indeed das de web; não as misture sem dizer.

## Regras
- Você não edita `perfil/` nem `rubricas/`. Se o candidato mandar aplicar algo, é a
  sessão principal que aplica, só no que ele aprovar (o `/sync-perfil` só lê o
  export do LinkedIn; não aplica recomendação de mercado).
- Salário só quando a fonte traz. Nunca estime.
- Português do Brasil.
