# Sistema de gestão de notas de alunos

Programa em Python que cadastra notas, calcula a média, define a situação do aluno e exibe um relatório final.

## Funcionalidades

- `adicionar_notas()` – lê as notas em um laço `while` até o usuário digitar `fim`, validando cada entrada.
- `calcular_media(notas)` – soma a lista e divide pela quantidade.
- `determinar_situacao(media)` – média maior ou igual a 7 gera "Aprovado"; menor, "Reprovado".
- `exibir_relatorio(...)` – mostra as notas, a média e a situação.

## Como executar

Cole o conteúdo de `gestao_notas.py` em uma célula do Google Colab e execute. Digite uma nota por vez e encerre com `fim`.

## Recursos praticados

Funções, listas, estruturas condicionais (`if`/`else`), laços (`while` e `for`) e tratamento de exceções (`try`/`except`).
