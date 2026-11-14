# Atividades da Faculdade

Repositório com as atividades práticas do curso de **Análise e Desenvolvimento de Sistemas** (Anhanguera).

## Análise e Modelagem de Sistemas

| Atividade | Conteúdo | Ferramenta |
|---|---|---|
| [BPMN – Viagens corporativas](analise-e-modelagem-de-sistemas/bpmn-viagens-corporativas/) | Processo de solicitação, aprovação e confirmação de viagens, com 3 raias, 2 decisões e 15 fluxos | bpmn.io |
| [Casos de uso – Controle de hotel](analise-e-modelagem-de-sistemas/casos-de-uso-hotel/) | Sistema de controle de hotel com os atores Hóspede e Funcionário e relações `<<include>>` e `<<extend>>` | Visual Paradigm Online |

## Linguagem de Programação

| Atividade | Conteúdo | Bibliotecas |
|---|---|---|
| [Gestão de notas](linguagem-de-programacao/gestao-notas/) | Cadastro de notas, média, situação do aluno e relatório final | Python puro |
| [Biblioteca](linguagem-de-programacao/biblioteca/) | Classe `Livro`, cadastro, listagem, busca por título e gráfico por gênero | Matplotlib |
| [Análise de vendas](linguagem-de-programacao/analise-vendas/) | Banco SQLite, DataFrame com Pandas, análises e três gráficos | Pandas, Matplotlib, Seaborn |
| [Machine Learning – Iris](linguagem-de-programacao/machine-learning-iris/) | Rede neural que classifica espécies de flores Iris | TensorFlow, scikit-learn, Pandas |

## O que pratiquei

- Notação **BPMN 2.0**: raias, tarefas, gateways exclusivos, eventos de início e fim e fluxos de sequência.
- Notação **UML**: atores, casos de uso, fronteira do sistema, associações, `<<include>>` e `<<extend>>`.
- **Python**: funções, condicionais, laços, classes, listas e dicionários.
- **Análise de dados**: SQLite, Pandas (`groupby`, `describe`, tratamento de datas) e visualização com Matplotlib e Seaborn.
- **Machine Learning**: pré-processamento, normalização, divisão treino/teste e rede neural com TensorFlow.

## Como executar os scripts de Python

Abra o [Google Colab](https://colab.google/), crie um notebook e cole o conteúdo do arquivo `.py`. Os scripts usam apenas bibliotecas que já vêm instaladas no Colab, com exceção do TensorFlow:

```bash
pip install tensorflow
```

O script de análise de vendas cria o arquivo `dados_vendas.db` na primeira execução.

## Observação

Todos os códigos foram escritos e comentados por mim para as aulas práticas da disciplina. Os scripts foram testados no Google Colab.
