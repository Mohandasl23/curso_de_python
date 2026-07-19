def calcula_quadrado(lista):
    for elemento in lista:
        quadrado = elemento ** 2
        print(f"O quadrado de {elemento} é: {quadrado}")

lista_de_inteiros = [1, 2, 3, 4, 5]
calcula_quadrado(lista_de_inteiros)