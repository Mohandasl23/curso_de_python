lista_produtos = []

for i in range(5):
    produtos={}

    id_produto = i + 1
    produtos["id"] = id_produto

    produtos["nome"] = input("Digite o nome do produto: ")
    preco = input("Digite o preço do produto: ").replace(",", ".")
    produtos["preco"] = float(preco)
    lista_produtos.append(produtos)
    
    faltam = 5 - len(lista_produtos)

    print(f"\nAinda faltam {faltam} cadastro(s).\n")

print("\n===== PRODUTOS CADASTRADOS =====")

for produto in lista_produtos:
    print("-" * 30)
    print(f"ID: {produto['id']}")
    print(f"Nome: {produto['nome']}")
    print(f"Preço: R$ {produto['preco']:.2f}")

print("\nParabéns! Você concluiu o cadastro de todos os produtos.")
    
   