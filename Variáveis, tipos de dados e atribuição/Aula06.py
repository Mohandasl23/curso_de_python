idade = 0
altura = 0.0
nome = ""

idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
nome = input("Digite seu nome: ")

print("Idade digitada: ", idade)
print("Altura digitada: ", altura)
print("Nome digitado: ", nome)

# Outras formas de exibir as informações:

# print("Olá, " + nome + "! Sua idade é " + str(idade) + " anos e sua altura é " + str(altura) + " metros.")
# print(f"Olá, {nome}! Sua idade é {idade} anos e sua altura é {altura} metros.")
# print("Olá, {}! Sua idade é {} anos e sua altura é {} metros.".format(nome, idade, altura))
# print("Olá, {0}! Sua idade é {1} anos e sua altura é {2} metros.".format(nome, idade, altura))
# print("Olá, {nome}! Sua idade é {idade} anos e sua altura é {altura} metros.".format(nome=nome, idade=idade, altura=altura))
# print("Olá, %s! Sua idade é %d anos e sua altura é %.2f metros." % (nome, idade, altura))
# print("Olá, " + nome + "! Sua idade é " + str(idade) + " anos e sua altura é " + str(altura) + " metros.")
