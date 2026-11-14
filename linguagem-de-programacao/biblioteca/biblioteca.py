# Sistema de gerenciamento de livros de uma biblioteca
# No Colab, a Matplotlib já vem instalada. Em outro ambiente: pip install matplotlib
import matplotlib.pyplot as plt   # biblioteca para gerar gráficos


class Livro:
    """Representa um livro com título, autor, gênero e quantidade disponível."""
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.titulo} | {self.autor} | {self.genero} | Disponível: {self.quantidade}"


livros = []   # Passo 2: lista vazia que armazena os livros cadastrados


def cadastrar_livro(titulo, autor, genero, quantidade):
    """Cria um Livro e o adiciona à lista."""
    livros.append(Livro(titulo, autor, genero, quantidade))
    print(f"Livro '{titulo}' cadastrado com sucesso!")


def listar_livros():
    """Mostra todos os livros cadastrados."""
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    for livro in livros:
        print(livro)


def buscar_livro(titulo):
    """Busca livros pelo título (sem diferenciar maiúsculas de minúsculas)."""
    encontrados = [l for l in livros if titulo.lower() in l.titulo.lower()]
    if encontrados:
        for livro in encontrados:
            print(livro)
    else:
        print(f"Livro '{titulo}' não encontrado.")


def grafico_por_genero():
    """Gera um gráfico de barras com a quantidade de livros por gênero."""
    contagem = {}
    for livro in livros:                       # soma as quantidades por gênero
        contagem[livro.genero] = contagem.get(livro.genero, 0) + livro.quantidade
    plt.bar(contagem.keys(), contagem.values(), color="#1f77b4")
    plt.title("Quantidade de livros por gênero")
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade")
    plt.show()


# Passo 5: testes do sistema
cadastrar_livro("Dom Casmurro", "Machado de Assis", "Romance", 5)
cadastrar_livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", "Romance", 3)
cadastrar_livro("O Hobbit", "J. R. R. Tolkien", "Fantasia", 4)
cadastrar_livro("Cosmos", "Carl Sagan", "Ciência", 2)
cadastrar_livro("Sapiens", "Yuval Noah Harari", "História", 6)
cadastrar_livro("Duna", "Frank Herbert", "Ficção Científica", 3)
cadastrar_livro("O Senhor dos Anéis", "J. R. R. Tolkien", "Fantasia", 2)

print("\n--- Lista de livros ---")
listar_livros()

print("\n--- Busca por 'hobbit' ---")
buscar_livro("hobbit")

print("\n--- Busca por 'Harry Potter' ---")
buscar_livro("Harry Potter")

print("\n--- Gráfico ---")
grafico_por_genero()
