
# O comando WHILE (enquanto)

# Sintaxe geral:

# <inicialização>
# Aqui você define a variável de controle antes do loop começar
contador = 0

# while <condição de parada>:
# O loop continuará executando ENQUANTO a condição for verdadeira
while contador < 5:
    
    # <linha de código 1>
    print("Contador:", contador)
    
    # <linha de código 2>
    # Você pode adicionar quantas instruções quiser aqui
    
    # ...
    # (várias outras linhas podem existir dentro do loop)
    
    # <atualização var. control.>
    # Muito importante! Atualiza a variável para evitar loop infinito
    contador += 1