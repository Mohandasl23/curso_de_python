frase = ""

while True:
    palavra = input("Digite uma palavra: ")

    if palavra == "/exit":
        break

    frase += palavra + " "

print("Resultado:")
print(frase.strip())