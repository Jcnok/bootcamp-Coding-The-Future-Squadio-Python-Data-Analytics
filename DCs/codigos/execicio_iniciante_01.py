# Solicita ao usuário a entrada de um número inteiro positivo
quantidade_passos = int(input())

# Verifica se a quantidade de passos é zero
if quantidade_passos == 0:
    print("Nenhum passo dado na floresta.")
else:
    # Utiliza um laço de repetição para simular os passos do explorador
    for passo in range(1, quantidade_passos + 1):
        if passo == 1:
            print(f"Explorador: {passo} passo")
        else:
            print(f"Explorador: {passo} passos")
