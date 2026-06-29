
numeros = [10, 20, 30]

'''append()

Adiciona UM elemento no final da lista.
'''
numeros.append(40)  # Adiciona o número 40 ao final da lista

print(numeros)  # Imprime a lista atualizada

'''extend()

Adiciona vários elementos de outra lista.'''
numeros.extend([50, 60])  # Adiciona os números 50 e 60 ao final da lista

print(numeros)  # Imprime a lista atualizada

'''insert(posição, elemento)

Insere um elemento em uma posição específica.'''

numeros.insert(1, 99)  # Insere o número 99 na posição 1 (segunda posição)

print(numeros)  # Imprime a lista atualizada

'''remove()

Remove pelo valor.'''

numeros.remove(20)  # Remove o número 20 da lista

print(numeros)  # Imprime a lista atualizada

'''index()

Mostra a posição do elemento.'''

numeros = [10, 20, 30]

print(numeros.index(20))  # Imprime a posição do número 20 na lista

'''pop()

Remove o último elemento.'''

numeros.pop()  # Remove o último elemento da lista

print(numeros)  # Imprime a lista atualizada

'''pop(posição)

Remove um elemento de posição específica.'''

numeros.pop(0)  # Remove o elemento na posição 0 (primeira posição)

print(numeros)  # Imprime a lista atualizada

'''count()

Conta quantas vezes um elemento aparece.'''

numeros = [1, 2, 2, 3, 2]

print(numeros.count(2))  # Imprime quantas vezes o número 2 aparece na lista

'''sort()

Organiza em ordem crescente.'''

numeros = [5, 1, 4, 2]

numeros.sort()  # Organiza a lista em ordem crescente

print(numeros)  # Imprime a lista ordenada

'''reverse()

Inverte a ordem da lista.'''

numeros.reverse()  # Inverte a ordem da lista

print(numeros)  # Imprime a lista invertida

'''clear()

Limpa toda a lista.'''

numeros.clear()  # Limpa toda a lista

print(numeros)  # Imprime a lista vazia

'''len()

Mostra quantos elementos existem.'''

numeros = [10, 20, 30]

print(len(numeros))  # Imprime a quantidade de elementos na lista

'''sum()

Soma todos os números da lista.'''

numeros = [10, 20, 30]

print(sum(numeros))  # Imprime a soma de todos os números na lista




print(" MINI LABORATÓRIO ".center(40, "="))

lista = [1, 2, 3]

lista.append(4)
lista.extend([5, 6])
lista.insert(0, 100)

print("=" * 40)
print("Lista inicial:")
print(lista)

print("=" * 40)
lista.remove(2)

print("Lista após remover o número 2:")
print(lista)

print("=" * 40)
print("Posição do 3:", lista.index(3))

print("=" * 40)
print("Quantidade de 5:", lista.count(5))

print("=" * 40)
lista.sort()

print("Lista ordenada:")
print(lista)

print("=" * 40)
lista.reverse()

print("Lista invertida:")
print(lista)

print("=" * 40)
print("O tamanho da lista é:", len(lista))

print("=" * 40)
print("O resultado da soma é:", sum(lista))

print("=" * 40)
print("Fim do programa 🚀")
print("=" * 40)
