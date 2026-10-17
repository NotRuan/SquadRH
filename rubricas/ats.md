# Rubrica ATS

Origem: prompt #2, adaptado. Removido: seções em inglês (contraria R3).

Revisto em 27/08/2026: a regra de formato tinha sido descartada como "datada",
e os dados de 2026 dizem o contrário. Ver "Qual arquivo enviar", abaixo.

## Extração de keywords da vaga

Separe em três listas:

1. **Obrigatórias** — a vaga diz "requisito", "obrigatório", "é necessário",
   ou repete o termo mais de uma vez.
2. **Desejáveis** — "diferencial", "será um plus", "desejável".
3. **De contexto** — o vocabulário do setor e do produto (R6): como a empresa
   chama seus processos, clientes e métricas.

Registre sigla **e** nome por extenso quando ambos existirem
(`ETL (Extract, Transform, Load)`), porque o filtro pode procurar qualquer um
dos dois.

## Classificação de cada keyword

Antes de inserir qualquer termo, classifique-o contra o perfil-mestre:

| Classe | Critério | O que fazer |
|---|---|---|
| **Presente** | Já aparece no currículo | Nada |
| **Real, não escrito** | Existe um fato no perfil-mestre que comprova | Inserir |
| **Ausente** | Nenhum fato no perfil comprova | **Não inserir.** Reportar como gap |

A terceira linha é a aplicação de R1 ao ATS. "Parece que ele sabe" não é
critério. Se nenhum fato do perfil sustenta o termo, ele não entra — vira gap
no relatório, para o candidato decidir se vale aplicar assim mesmo.

**A citação é obrigatória.** Ao classificar algo como "real, não escrito", cite
o fato do perfil que comprova, pelo título. Sem citação, a classe correta é
"ausente" — por definição, não por dúvida.

## Inserção aditiva

A inserção **acrescenta** a um bullet existente; não o reescreve.

Permitido:
- Acrescentar o termo dentro da frase, preservando o verbo inicial e a
  estrutura.
- Acrescentar uma ferramenta a uma lista já existente.
- Acrescentar o termo na seção `COMPETÊNCIAS`.

Proibido:
- Trocar o verbo do bullet.
- Reordenar as partes da frase.
- Reescrever o bullet "para encaixar melhor".
- Acrescentar ou remover qualquer número.

Exemplo:

> Antes: Reduzi o fechamento de relatórios de 3 dias para 4 horas ao
> substituir a apuração manual por rotinas em Python agendadas.
>
> Depois: Reduzi o fechamento de relatórios de 3 dias para 4 horas ao
> substituir a apuração manual por rotinas em Python agendadas **orquestradas
> em Airflow**.

O verbo, os números e a estrutura permaneceram idênticos.

## Formato legível por máquina

- Coluna única. Sem tabelas, caixas de texto, colunas, gráficos ou imagens.
- Sem cabeçalho e rodapé — parte dos analisadores ignora essas áreas.
- Seções com os nomes fixos de R3.
- Datas sempre no mesmo formato: `mês/ano` (`abr/2026 – atual`).
- Bullets como lista de verdade, não como caractere `•` digitado.
- Hard skills antes de soft skills em `COMPETÊNCIAS`.

## Qual arquivo enviar

Geramos os dois. Quando o formulário aceitar ambos, **envie o `.docx`**.

A taxa de falha de parsing é materialmente diferente: o DOCX de coluna única é
o formato que os analisadores leem melhor, e o PDF é onde a extração de texto
falha com mais frequência — sobretudo quando o gerador desenha o texto em
posições absolutas em vez de fluxo. Layout de coluna única também é lido com
mais precisão que o de duas colunas, o que a regra de formato abaixo já cobre.

Envie `.pdf` quando o formulário só aceitar PDF, quando o destinatário for uma
pessoa (e-mail direto ao recrutador, anexo de mensagem) ou quando a fidelidade
visual importar mais que a extração.

Isto **não** é licença para editar o `.docx` à mão (R5). Os dois continuam
sendo derivados regeneráveis do markdown.

## Uma vez basta

Os filtros modernos pontuam relevância no contexto, não frequência. Repetir o
mesmo termo para "reforçar" **derruba** o score nas ferramentas que fazem
match semântico, e é lido como manipulação por quem revisa à mão.

Um termo, uma vez, no lugar onde ele tem lastro. Se ele já está num bullet, não
precisa também estar em `COMPETÊNCIAS` — e vice-versa.

Pelo mesmo motivo: nunca texto branco, nunca fonte tamanho 1, nunca bloco de
keywords escondido. Os analisadores marcam isso como manipulação, e o
recrutador que enxerga descarta na hora.

## As perguntas eliminatórias

O filtro que mais descarta candidatura **não é** o de currículo. São as
perguntas do formulário — pretensão salarial, modelo de trabalho,
disponibilidade, inglês, formação exigida, CNH, PCD.

Uma resposta em branco ou fora da faixa elimina antes de qualquer leitura, por
melhor que o currículo esteja. Nenhum revisor do painel enxerga esse campo,
porque ele não está no documento.

Ao ler a vaga, liste quais dessas perguntas ela sinaliza. As respostas padrão
ficam no `perfil-mestre.md`, seção "Respostas de formulário" — e valem a mesma
regra de todo o resto: são fatos, vêm do candidato, não se inventam.

## Score de match

Aritmética explícita, recomputável — nunca uma impressão:

```
score = (obrigatórias_presentes / obrigatórias_totais) * 70
      + (desejáveis_presentes  / desejáveis_totais)  * 20
      + (contexto_presentes    / contexto_totais)    * 10
```

Se uma das listas estiver vazia, redistribua o peso dela proporcionalmente
entre as outras duas.

**"Presente" aqui significa presente no currículo entregue** — não no perfil.
Uma keyword classificada como "real, não escrita" e ainda não inserida não
conta. O score mede o documento, não o potencial.

Leitura do resultado:

| Faixa | Significado |
|---|---|
| 85-100 | Forte. Enviar |
| 70-84 | Bom. Enviar, com os gaps declarados no relatório |
| 55-69 | Fraco. Vale rever a seleção de fatos antes de enviar |
| < 55 | A vaga pede algo que o perfil não tem. Decisão do candidato |

Reporte sempre o score **com a conta aberta** — quantas obrigatórias de
quantas, quais faltaram e por quê.

**Um score alto não é meta.** Ele é consequência de o perfil bater com a vaga.
Se a única forma de subir o score for inserir um termo sem lastro, o score fica
baixo — é informação verdadeira sobre a aderência, e serve para o candidato decidir
onde investir o tempo dele.
