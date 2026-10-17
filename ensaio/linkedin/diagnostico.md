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

Lastro do teto: `python`, `power bi`, `analista de dados` (cargo ocupado nas duas
experiências) e `sql` (Competências do perfil). `analista de bi` fora: cargo
não ocupado (decisão de 16/10/2026). Item de completude com fato: formação.

## O que podemos mudar

1. Headline: `Analista de Dados | Python · SQL · Power BI` (título ocupado + três competências com lastro).
2. Sobre: abrir com cargo + a prova mais forte (3 dias → 4 horas).
3. Sobre: demais provas com número e linha de competências.
4. Sênior: bullet de automação com número.
5. Sênior: bullet do painel só com a escala (resultado em aberto).
6. Júnior: bullet da padronização com número.
7. Júnior: bullet da migração com verbo de Contribuição (`participação`).
8. Competências fixadas: SQL, Python, Power BI, Automação de rotinas, Modelagem de indicadores.
9. Tirar "Comunicação" e "Excel": nenhum dos dois é competência do perfil.
10. Configuração: banner, URL, Open to Work com "Analista de Dados", top 5 fixadas.

## Gaps
- `analista de bi` — título não ocupado. Não entra na headline.
- `etl`, `dax`, `databricks` — sem fato no perfil de exemplo.
- Certificações, idiomas, Em destaque — sem fato.

## Pendências do perfil
- **Resultado do painel de entregas** — `[FALTA MÉTRICA — qual foi o efeito no atraso ou na decisão?]`. No perfil público o bullet sai só com a escala.

## Vamos mudar
- 1 a 10 (ensaio: "vamos mudar tudo")
## Fica como está
- —

Score depois 85,50 (`score --perfil ensaio/linkedin/proposta-novo.md --abertura 20 --prova 15`: busca 40,00 · completude 10,50). Não passa do teto.
