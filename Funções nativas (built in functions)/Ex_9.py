import math
import os

# Exemplos abaixo são referentes a biblioteca math.
x = 16
raiz_quad = math.sqrt(x)

print("Raiz quadrada de", x, "é igual a", raiz_quad)


angulo = 45
seno = math.sin(angulo)
print("O seno de", angulo, "é igual a", seno)

# Exemplos abaixo são referentes a biblioteca os.

diretorio = os.getcwd()
print("O diretotio corrente é", diretorio)

# os.system("cls")

lista = [10, 20, 30]
tam = len(lista)
print("A lista", lista, "tem tamanho", tam)

soma = sum(lista)
print("A lista", lista, "tem um somatorio igual a", soma)
