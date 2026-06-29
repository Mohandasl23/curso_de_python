# print("Olá, seja bem-vindo(a)")

# print(f"O valor inteiro em decimal é: {10: d}")
# print(f"O valor inteiro em binário é: {10: b}")

# print(f"O valor de Pi é: {3.14159265: f}")
# print(f"O valor de Pi é: {3.14159265: .2f}")


# Desafio: Formatação de Saída

# Exemplo 1

nome = "João"
idade = 41
salario = 5000.00
pais = "Brasil"

print(f"Nome:\t\t{nome}")
print(f"Idade:\t\t{idade}")
print(f"Salário:\t{salario:.2f}")
print(f"País:\t\t{pais}\n")

# Exemplo 2

nome = "João"
idade = 41 
salario = 5000.00
pais = "Brasil"

print(f"{'Campo':<10} | {'Valor':<10}")
print("-" * 27)

print(f"{'Nome':<10} | {nome:<15}")
print(f"{'Idade':<10} | {idade:<15}")
print(f"{'Salário':<10} | R$: {salario:<15.2f}")
print(f"{'País':<10} | {pais:<15}")