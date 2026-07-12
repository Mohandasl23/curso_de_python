lista_pessoas = []

for _ in range(3):
    pessoa={}
    pessoa["nome"] = input("Digite o nome: ")
    pessoa["peso"] = float(input("Digite o peso: "))
    pessoa["idade"] = int(input("Digite a idade: "))
    lista_pessoas.append(pessoa)

print("\nDados das pessoas:")
for pessoa in lista_pessoas:
    print("\nNome: ", pessoa["nome"])
    print("\nPeso: ", pessoa["peso"])
    print("\nIdade: ", pessoa["idade"])
    print()