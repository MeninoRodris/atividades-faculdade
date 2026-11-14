# Análise de vendas do varejo com SQLite, Pandas, Matplotlib e Seaborn
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------- Passo 1: banco de dados SQLite ----------
conexao = sqlite3.connect('dados_vendas.db')      # conecta (ou cria) o banco
cursor = conexao.cursor()                          # cria o cursor
cursor.execute('DROP TABLE IF EXISTS vendas1')     # permite reexecutar o notebook
cursor.execute('''
CREATE TABLE vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
''')
cursor.execute('''
INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
('2023-01-05', 'Produto B', 'Roupas', 350.00),
('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
('2023-03-15', 'Produto D', 'Livros', 200.00),
('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
('2023-04-02', 'Produto F', 'Roupas', 400.00),
('2023-05-05', 'Produto G', 'Livros', 150.00),
('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
('2023-07-20', 'Produto I', 'Roupas', 600.00),
('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
('2023-09-30', 'Produto K', 'Livros', 300.00),
('2023-10-05', 'Produto L', 'Roupas', 450.00),
('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
('2023-12-20', 'Produto N', 'Livros', 250.00);
''')
conexao.commit()                                   # confirma as mudanças

# ---------- Passo 2: explorar e preparar os dados ----------
df_vendas = pd.read_sql_query('SELECT * FROM vendas1', conexao)   # tabela -> DataFrame
print("Primeiras linhas:")
print(df_vendas.head())
print("\nInformações do DataFrame:")
df_vendas.info()
print("\nValores nulos por coluna:")
print(df_vendas.isnull().sum())
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])  # texto -> data
df_vendas['mes'] = df_vendas['data_venda'].dt.month                # coluna auxiliar: mês
print("\nEstatísticas do valor de venda:")
print(df_vendas['valor_venda'].describe().round(2))

# ---------- Passo 3: análise dos dados ----------
total = df_vendas['valor_venda'].sum()
ticket_medio = df_vendas['valor_venda'].mean()
print(f"\nFaturamento total: R$ {total:.2f}")
print(f"Ticket médio: R$ {ticket_medio:.2f}")

por_categoria = (df_vendas.groupby('categoria')['valor_venda']
                 .sum().sort_values(ascending=False).reset_index())
por_categoria['participacao_%'] = (por_categoria['valor_venda'] / total * 100).round(1)
print("\nVendas por categoria:")
print(por_categoria)

por_mes = df_vendas.groupby('mes')['valor_venda'].sum().reset_index()
print("\nVendas por mês:")
print(por_mes)
melhor = por_mes.loc[por_mes['valor_venda'].idxmax()]
pior = por_mes.loc[por_mes['valor_venda'].idxmin()]
print(f"\nMelhor mês: {int(melhor['mes'])} (R$ {melhor['valor_venda']:.2f})")
print(f"Pior mês: {int(pior['mes'])} (R$ {pior['valor_venda']:.2f})")

# ---------- Passo 4: visualização dos dados ----------
sns.set_theme()

# Gráfico 1: faturamento por categoria (Seaborn)
plt.figure(figsize=(7, 4))
sns.barplot(data=por_categoria, x='categoria', y='valor_venda', hue='categoria', palette='Set2')
plt.title('Faturamento por categoria')
plt.xlabel('Categoria')
plt.ylabel('Valor vendido (R$)')
plt.show()

# Gráfico 2: evolução mensal das vendas (Seaborn)
plt.figure(figsize=(8, 4))
sns.lineplot(data=por_mes, x='mes', y='valor_venda', marker='o')
plt.title('Evolução mensal das vendas')
plt.xlabel('Mês')
plt.ylabel('Valor vendido (R$)')
plt.show()

# Gráfico 3: participação de cada categoria (Matplotlib)
plt.figure(figsize=(5, 5))
plt.pie(por_categoria['valor_venda'], labels=por_categoria['categoria'], autopct='%1.1f%%')
plt.title('Participação por categoria no faturamento')
plt.show()

conexao.close()                                    # fecha a conexão
