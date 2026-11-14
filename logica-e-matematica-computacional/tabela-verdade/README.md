# Tabela verdade e classificação de proposições

Construção de tabelas verdade para proposições simples e compostas e classificação como tautologia, contradição ou contingência.

## Proposições analisadas

### a) Negação ¬P

| P | ¬P |
|---|---|
| V | F |
| F | V |

### b) Implicação P → Q

| P | Q | P → Q |
|---|---|---|
| V | V | V |
| V | F | F |
| F | V | V |
| F | F | V |

A implicação é falsa em apenas uma linha: quando P é verdadeiro e Q é falso.

### c) Proposição composta (P ∧ Q) ∨ (¬P)

| P | Q | P ∧ Q | ¬P | (P ∧ Q) ∨ (¬P) |
|---|---|---|---|---|
| V | V | V | F | V |
| V | F | F | F | F |
| F | V | F | V | V |
| F | F | F | V | V |

## Classificação

Todas as três proposições são **contingências**: apresentam resultados verdadeiros e falsos, dependendo dos valores de P e Q.

## Respostas

1. **Tautologia** é a proposição composta verdadeira em todas as linhas da tabela verdade.
2. **P → Q** é falsa apenas quando P é V e Q é F.
3. **(P ∧ Q) ∨ (¬P)** é uma contingência e equivale logicamente a P → Q.

## Como executar

Cole o conteúdo de `tabela_verdade.py` em uma célula do Google Colab e execute. O script gera as combinações com `itertools.product`, monta as tabelas e classifica cada proposição.
