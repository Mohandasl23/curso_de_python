
# Pedindo os dados ao usuário

id = int(input("Digite o seu ID: "))
nome = input("Digite o seu nome: ")
salario = float(input("Digite o seu salário: "))
brasileiro = input("Você é brasileiro? (sim/não): ")

# Convertendo para booleano
brasileiro = True if brasileiro.lower() == "sim" else False

# Exibindo os dados com f-strings

# print("\n📋 Dados cadastrados:")
# print(f"ID: {id}")
# print(f"Nome: {nome}")
# print(f"Salário: R$ {salario:.2f}")
# print(f"Brasileiro: {brasileiro}")

print("\n" + "="*30)
print("📋 CADASTRO DO USUÁRIO")
print("="*30)
print(f"ID: {id}")
print(f"Nome: {nome}")
print(f"Salário: R$ {salario:.2f}")
print(f"Brasileiro: {'Sim' if brasileiro else 'Não'}")
print("="*30)