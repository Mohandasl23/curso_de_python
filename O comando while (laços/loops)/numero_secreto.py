# import random
# numero_secreto = random.randint(1, 50)

# print("Bem-vindo ao jogo de adivinhação!")
# print("Tente adivinhar o número secreto entre 1 e 50.")
# while True:
#     palpite = int(input("Digite seu palpite: "))
    
#     if palpite < numero_secreto:
#         print("Muito baixo! Tente novamente.")
#     elif palpite > numero_secreto:
#         print("Muito alto! Tente novamente.")        
#     else:
#         print("Parabéns! Você acertou o número secreto!")
#         break  # Sai do loop quando o número for adivinhado corretamente
    
import random

numero_secreto = random.randint(1, 20)
tentativas = 0
limite = 3  # você pode mudar

print("🎮 Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número entre 1 e 20. Você tem 3 tentativas.\n")

while tentativas < limite:
    try:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("🔽 Muito baixo!")
        elif palpite > numero_secreto:
            print("🔼 Muito alto!")
        else:
            print(f"🎉 Acertou em {tentativas} tentativas!")
            break

        # Dica quente/frio
        if abs(palpite - numero_secreto) <= 3:
            print("🔥 Tá MUITO perto!")

        print(f"Tentativas restantes: {limite - tentativas}\n")

    except ValueError:
        print("⚠️ Digite apenas números!")

else:
    print(f"💀 Fim de jogo! O número era {numero_secreto}")