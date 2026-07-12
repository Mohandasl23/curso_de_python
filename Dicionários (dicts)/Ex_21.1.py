pessoa ={
    "nome":"Teste",
    "peso":0.0,
    "idade":0
}
print("Dados da pessoa:")
print("Nome: ", pessoa["nome"])
print("Peso: ", pessoa["peso"])
print("Idade: ", pessoa["idade"])
print()

# Aqui eu altero os dados do dicionário pessoa:
pessoa["nome"] = "Texto"
pessoa["peso"] =99.99
pessoa["idade"] =10

print("Dados da pessoa:")
print("Nome: ", pessoa["nome"])
print("Peso: ", pessoa["peso"])
print("Idade: ", pessoa["idade"])
print()

# Aqui o usuario altera os dados do dicionário pessoa:
pessoa["nome"] = input("Digite o nome: ")
pessoa["peso"] = float(input("Digite o peso: "))
pessoa["idade"] =int(input("Digite a idade: "))

print("\nDados da pessoa:")
print("\nNome: ", pessoa["nome"])
print("\nPeso: ", pessoa["peso"])
print("\nIdade: ", pessoa["idade"])
print()
