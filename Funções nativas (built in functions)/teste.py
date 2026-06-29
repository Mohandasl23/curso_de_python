# def calcular_media(notas): 
#     media = sum(notas) / len(notas) 
#     return media 

# Exemplo 1

# notas_aluno = [7.5, 8.0, 6.5, 9.0]

# resultado = calcular_media(notas_aluno)

# print(f"Média do aluno: {resultado:.2f}")

# Exemplo 2

# gastos = [50.00, 75.50, 32.90, 60.00]

# media_gastos = calcular_media(gastos)

# print(f"Gasto médio: R$ {media_gastos:.2f}")

# Exemplo 3

# def calcular_desconto(preco, porcentagem):
#     desconto = preco * (porcentagem / 100)
#     preco_final = preco - desconto
#     return preco_final

# preco_produto = 1000
# preco_com_desconto = calcular_desconto(preco_produto, 10)

# print(f"Preço com desconto: R$ {preco_com_desconto:.2f}")

# Exemplo 4

# def calcular_desconto(preco):
#     if preco >= 200:
#         desconto = 20
#     elif preco >= 100:
#         desconto = 10
#     else:
#         desconto = 5

#     preco_final = preco - (preco * desconto / 100)
#     return preco_final

# print(calcular_desconto(50))   # pouco desconto
# print(calcular_desconto(150))  # médio desconto
# print(calcular_desconto(250))  # alto desconto

idade = int(input("Digite sua idade: "))


if idade < 18:
  print("Você é menor de idade.")
elif idade >= 18 and idade < 65:
  print("Você é adulto(a).")
else:
  print("Você é idoso(a).")
    
     