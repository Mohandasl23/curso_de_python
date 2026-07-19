# crie um programa para simular uma calculador.
# O programa deve ter as seguintes funcionalidades:
# - Adição
# - Subtração
# - Multiplicação
# - Divisão
# - O usuário deve inserir os números e a operação deve ser realizada entre dois números.
# - Crie um menu para o usuário escolher a operação matematica que deseja usar.

# 1. def mostrar_menu():
#     print("\n--- Calculadora Simples ---")
#     print("1. Adição (+)")
#     print("2. Subtração (-)")
#     print("3. Multiplicação (*)")
#     print("4. Divisão (/)")
#     print("5. Sair")
#     opcao = input("Escolha uma operação: ")
#     return opcao

def mostrar_menu():
    print("\n--- Calculadora Simples ---")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Sair")
    opcao = input("Escolha uma operação: ")
    return opcao

def adicao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1 + num2

def subtracao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1 - num2

def multiplicacao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1 * num2

def divisao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1 / num2

def calculadora():
    while True:
        opcao = mostrar_menu()
        if opcao in ["1", "2", "3", "4"]:
            if opcao == "1":
                resultado = adicao()
            elif opcao == "2":
                resultado = subtracao()
            elif opcao == "3":
                resultado = multiplicacao()
            elif opcao == "4":
                resultado = divisao()
            
            # Mostra como inteiro se não houver parte decimal, caso contrário formata para 2 casas com vírgula
            if resultado.is_integer():
                resultado_formatado = str(int(resultado))
            else:
                resultado_formatado = f"{resultado:.2f}".replace('.', ',')
            print("Resultado:", resultado_formatado)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

calculadora()
