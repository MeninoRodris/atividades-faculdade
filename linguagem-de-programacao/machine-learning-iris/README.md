# Machine Learning – Classificação de flores Iris

Rede neural que classifica espécies de flores Iris a partir das medidas de sépalas e pétalas.

## Etapas

1. **Dados:** conjunto Iris do scikit-learn (150 flores, 4 características, 3 espécies).
2. **Pré-processamento:** divisão em 80% treino e 20% teste, estratificada, e normalização com `StandardScaler`.
3. **Modelo:** rede neural sequencial com camada oculta de 16 neurônios (ReLU) e saída de 3 neurônios (softmax).
4. **Treino:** 50 épocas, com 20% dos dados de treino para validação.
5. **Avaliação:** `evaluate()` sobre os dados de teste.
6. **Previsões:** `predict()` nas flores de teste e em três novas flores.

## Resultados

Acurácia de 96,67% nos dados de teste. As três novas flores foram classificadas corretamente.

## Como executar

Cole o conteúdo de `classificacao_iris.py` no Google Colab. O TensorFlow já vem instalado no Colab; se necessário, rode:

```bash
pip install tensorflow
```

## Recursos praticados

Pré-processamento de dados, normalização, TensorFlow/Keras, scikit-learn e avaliação de modelos.
