
print("=== DESAFIO ===")

numeros = []

while True:
    numero = int(input("Digite um número inteiro (ou 0 para sair): "))
    if numero == 0:
        break
    numeros.append(numero)

    print("\n=== RESULTADO ===")

    print(f"Quantidade de números digitados: {len(numeros)}")
    print(f"Menor número: {min(numeros)}")
    print(f"Maior número: {max(numeros)}")