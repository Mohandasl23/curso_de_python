
contador = 0

limite = int(input("Digite até qual número o contador deve contar: "))

while contador <= limite:

    print(f"Contador: {contador}")

    if contador == limite:

        opcao = input(
            "Digite 'continue' para continuar contando "
            "ou 'break' para encerrar: "
        ).lower()

        if opcao == "continue":
            contador += 1
            limite += 1
            continue

        elif opcao == "break":
            print("Programa encerrado 🚪")
            break

        else:
            print("Comando inválido.")
            break

    contador += 1