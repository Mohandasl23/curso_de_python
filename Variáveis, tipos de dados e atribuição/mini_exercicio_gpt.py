# nome = input("Digite o seu nome: ")
# idade = int(input("Digite a sua idade: "))
# cidade = input("Digite a sua cidade: ")
# altura = float(input("Digite a sua altura: "))

# print("\n" + "="*30)
# print("📋 DADOS DO USUÁRIO")
# print("="*30)
# print(f"Nome: {nome}")
# print(f"Idade: {idade}")
# print(f"Cidade: {cidade}")
# print(f"Altura: {altura:.2f} m")
# print("="*30)

nome = input("Digite o seu nome: ")

try:
    idade = int(input("Digite a sua idade: "))
except ValueError:
    print("Idade inválida! Vou considerar como 0.")
    idade = 0

cidade = input("Digite a sua cidade: ")

try:
    altura = float(input("Digite a sua altura: "))
except ValueError:
    print("Altura inválida! Vou considerar como 0.0")
    altura = 0.0

print("\n" + "="*30)
print("📋 DADOS DO USUÁRIO")
print("="*30)
print(f"👤 Nome   : {nome}")
print(f"🎂 Idade  : {idade} anos")
print(f"📍 Cidade : {cidade}")
print(f"📏 Altura : {altura:.2f} m")
print("="*30)