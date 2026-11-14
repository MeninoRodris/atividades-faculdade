# Classificação de espécies de flores Iris com Machine Learning
# No Google Colab, instale o TensorFlow com: pip install tensorflow

# ---------- Passo 1: importar bibliotecas e carregar os dados ----------
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

iris = load_iris()          # conjunto de dados Iris que já vem no scikit-learn
X = iris.data               # características: sépalas e pétalas
y = iris.target             # espécie de cada flor (0, 1 ou 2)
nomes = iris.target_names   # nomes das espécies

print("Formato dos dados:", X.shape)
print("Espécies:", list(nomes))
df = pd.DataFrame(X, columns=iris.feature_names)
df['especie'] = [nomes[i] for i in y]
print("\nPrimeiras linhas:")
print(df.head())
print("\nQuantidade por espécie:")
print(df['especie'].value_counts())

# ---------- Passo 2: pré-processamento ----------
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)   # 80% treino e 20% teste

scaler = StandardScaler()                       # normaliza as características
X_treino = scaler.fit_transform(X_treino)       # aprende a média/desvio só no treino
X_teste = scaler.transform(X_teste)             # aplica a mesma escala no teste
print("\nAmostras de treino:", len(X_treino), "| Amostras de teste:", len(X_teste))

# ---------- Passo 3: construir o modelo ----------
modelo = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(4,)),                        # 4 características de entrada
    tf.keras.layers.Dense(16, activation='relu'),             # camada oculta
    tf.keras.layers.Dense(3, activation='softmax')            # 3 espécies de saída
])
modelo.compile(optimizer='adam',
               loss='sparse_categorical_crossentropy',
               metrics=['accuracy'])
modelo.summary()

# ---------- Passo 4: treinar o modelo ----------
historico = modelo.fit(X_treino, y_treino, epochs=50,
                       validation_split=0.2, verbose=0)
print("\nTreinamento concluído em", len(historico.history['accuracy']), "épocas.")
print(f"Última acurácia de treino: {historico.history['accuracy'][-1]:.4f}")

# ---------- Passo 5: avaliar o modelo ----------
perda, acuracia = modelo.evaluate(X_teste, y_teste, verbose=0)
print(f"\nAcurácia nos dados de teste: {acuracia:.4f} ({acuracia*100:.2f}%)")

# ---------- Passo 6: fazer previsões ----------
previsoes = modelo.predict(X_teste)
classes_previstas = np.argmax(previsoes, axis=1)  # maior probabilidade
print("\nPrevisões para as 10 primeiras flores de teste:")
for i in range(10):
    print(f"Real: {nomes[y_teste[i]]:<12} | Previsto: {nomes[classes_previstas[i]]:<12} "
          f"| Probabilidade: {previsoes[i].max():.2f}")

novas_flores = np.array([[5.1, 3.5, 1.4, 0.2],   # medidas típicas de setosa
                         [6.0, 2.7, 5.1, 1.6],   # medidas típicas de versicolor
                         [6.7, 3.0, 5.2, 2.3]])  # medidas típicas de virginica
novas_flores = scaler.transform(novas_flores)    # mesma normalização do treino
resultado = modelo.predict(novas_flores)
print("\nPrevisões para novas flores:")
for i, p in enumerate(resultado):
    print(f"Flor {i+1}: {nomes[np.argmax(p)]} (probabilidade {p.max():.2f})")

# Gráfico auxiliar: acurácia ao longo das épocas
plt.figure(figsize=(7, 4))
plt.plot(historico.history['accuracy'], label='Treino')
plt.plot(historico.history['val_accuracy'], label='Validação')
plt.title('Acurácia do modelo por época')
plt.xlabel('Época')
plt.ylabel('Acurácia')
plt.legend()
plt.show()
