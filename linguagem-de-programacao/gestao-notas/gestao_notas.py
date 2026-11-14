# Sistema de gestão de notas de alunos

def adicionar_notas():
    """Lê as notas digitadas pelo usuário e as guarda em uma lista."""
    notas = []                                   # lista que armazena as notas
    while True:                                  # repetição: continua até o usuário digitar 'fim'
        entrada = input("Digite uma nota (0 a 10) ou 'fim' para encerrar: ")
        if entrada.lower() == "fim":             # condição de parada
            break
        try:
            nota = float(entrada.replace(",", "."))   # aceita vírgula ou ponto
        except ValueError:                       # trata texto inválido
            print("Valor inválido! Digite um número.")
            continue
        if 0 <= nota <= 10:                      # valida o intervalo da nota
            notas.append(nota)                   # adiciona a nota na lista
        else:
            print("Nota fora do intervalo! Use valores entre 0 e 10.")
    return notas


def calcular_media(notas):
    """Retorna a média das notas (0 se a lista estiver vazia)."""
    if len(notas) == 0:                          # evita divisão por zero
        return 0
    return sum(notas) / len(notas)


def determinar_situacao(media):
    """Retorna 'Aprovado' se média >= 7; caso contrário, 'Reprovado'."""
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


def exibir_relatorio(notas, media, situacao):
    """Mostra o relatório final: notas, média e situação."""
    print("\n===== RELATÓRIO FINAL =====")
    print("Notas inseridas:", end=" ")
    for nota in notas:                           # repetição para exibir cada nota
        print(f"{nota:.1f}", end="  ")
    print(f"\nMédia: {media:.2f}")
    print(f"Situação: {situacao}")
    print("===========================")


def main():
    notas = adicionar_notas()
    if len(notas) == 0:
        print("Nenhuma nota foi inserida.")
        return
    media = calcular_media(notas)
    situacao = determinar_situacao(media)
    exibir_relatorio(notas, media, situacao)


main()
