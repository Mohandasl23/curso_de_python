matriz = []

# Preenchendo a matriz
for linha in range(3):
    lista_linha = []

    for coluna in range(4):
        valor = int(input(f"Digite um valor para [{linha}][{coluna}]: "))
        lista_linha.append(valor)

    matriz.append(lista_linha)

# Inicializando com o primeiro elemento da matriz
maior = matriz[0][0]
menor = matriz[0][0]

linha_maior = 0
coluna_maior = 0

linha_menor = 0
coluna_menor = 0

# Percorrendo a matriz
for linha in range(3):
    for coluna in range(4):

        if matriz[linha][coluna] > maior:
            maior = matriz[linha][coluna]
            linha_maior = linha
            coluna_maior = coluna

        if matriz[linha][coluna] < menor:
            menor = matriz[linha][coluna]
            linha_menor = linha
            coluna_menor = coluna

# Exibindo a matriz
print("\nMATRIZ:")
for linha in matriz:
    print(linha)

# Resultado
print(f"\nMaior valor: {maior}")
print(f"Posição: linha {linha_maior}, coluna {coluna_maior}")

print(f"\nMenor valor: {menor}")
print(f"Posição: linha {linha_menor}, coluna {coluna_menor}")