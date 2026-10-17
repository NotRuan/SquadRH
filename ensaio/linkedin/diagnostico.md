# Diagnóstico — LinkedIn (ensaio, Fulano de Exemplo)

Score atual 14,50 · teto 85,50 (vertente Dados & BI).
Acima do teto: `analista de bi` — título da família que o Fulano não ocupou; é gap, não texto.

## Conta aberta

`python tools/score_linkedin.py score --vertente ensaio/linkedin/vertente.md --perfil ensaio/linkedin/atual.md --abertura 0 --prova 0`

| Bloco | Atual | Motivo |
|---|---|---|
| Busca | 10,00 / 50 | `analista de dados` e `python` só em Sobre/Experiência (1 cada); `sql`, `power bi`, `analista de bi` ausentes |
| Abertura | 0 / 20 | Headline "Profissional de dados na ACME Log" não nomeia título da vertente (0); início do Sobre sem cargo e sem número (0) |
| Prova | 0 / 15 | 0 de 2 experiências com resultado quantificado |
| Completude | 4,50 / 15 | foto, localidade, formação (3/10) |
| **Total** | **14,50 / 100** | |

Teto: `python tools/score_linkedin.py teto --vertente ensaio/linkedin/vertente.md --perfil ensaio/linkedin/atual.md --lastro "python,power bi,analista de dados,sql" --itens "formação" --abertura 20 --prova 15`
→ busca 40,00 · abertura 20 · prova 15 · completude 10,50 · **total 85,50**.

Lastro do teto: `python` (Automação de relatórios operacionais), `power bi`
(Migração de painéis para Power BI), `analista de dados` (cargo ocupado nas
duas experiências), `sql` (Competências do perfil). `analista de bi` fora:
cargo não ocupado (decisão de 16/10/2026). Itens de completude com fato:
formação. Sem fato: certificações, idiomas, em destaque.

## O que podemos mudar

**Headline**
1. `Analista de Dados | Python · SQL · Power BI` — título ocupado + três competências recorrentes com lastro. Rende busca (+4 termos na headline) e abertura (+10).

**Sobre**
2. Abrir com cargo + a prova mais forte (3 dias → 4 horas). Rende abertura (+10).
3. Acrescentar as outras provas com número (14 relatórios / 6 áreas; 120 mil registros / 35%; 25 painéis, semanal → diária) e a linha de competências.

**Experiência — Sênior**
4. Bullet de automação com número (3 dias → 4 horas; 14 relatórios; 6 áreas). Rende prova.
5. Bullet do painel de entregas só com a escala (40 usuários) — resultado em aberto, ver Pendências.

**Experiência — Júnior**
6. Bullet da padronização com número (120 mil registros; 35%). Rende prova.
7. Bullet da migração para Power BI com verbo de Contribuição (`Escopo: participação`).

**Competências**
8. Fixadas: SQL, Python, Power BI (ordem de recorrência), Automação de rotinas, Modelagem de indicadores.
9. Tirar "Comunicação" e "Excel": nenhum dos dois está nas Competências do perfil (Excel só aparece como origem da migração).

**Configuração**
10. Banner, URL personalizada, Open to Work com "Analista de Dados", top 5 fixadas.

## Gaps
- `analista de bi` — título não ocupado. Não entra na headline.
- `etl`, `dax`, `databricks` — sem fato no perfil de exemplo.
- Certificações, idiomas, Em destaque — sem fato.

## Pendências do perfil
- **Resultado do painel de entregas** — o perfil tem `[FALTA MÉTRICA — qual foi o efeito no atraso ou na decisão?]`. No perfil público o bullet sai só com a escala.

## Vamos mudar
- 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 (ensaio: "vamos mudar tudo")
## Fica como está
- —

Score depois 85,50 (`score --perfil ensaio/linkedin/proposta-novo.md --abertura 20 --prova 15`: busca 40,00 · completude 10,50). Não passa do teto.
