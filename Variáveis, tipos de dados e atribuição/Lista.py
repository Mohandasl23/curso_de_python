lista_compras = []

print("📝 CRIAR LISTA DE COMPRAS")
print("Digite 'sair' para finalizar\n")

while True:
    produto = input("Produto: ")

    if produto.lower() == "sair":
        break

    lista_compras.append({
        "nome": produto,
        "preco": 0,
        "quantidade": 0
    })

print("\nLista criada com sucesso!")

def moeda(valor):
    return f"R$ {valor:.2f}".replace(".", ",")

def ler_preco(msg):
    texto = input(msg)
    texto = texto.replace("R$", "").replace(" ", "").replace(",", ".")
    return float(texto)

total = 0

print("\n🛒 AGORA VAMOS ÀS COMPRAS\n")

for item in lista_compras:
    print(f"\nProduto: {item['nome']}")

    try:
        preco = ler_preco("Preço: R$ ")
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("⚠️ Valor inválido! Pulando item...")
        continue

    item["preco"] = preco
    item["quantidade"] = quantidade

    subtotal = preco * quantidade
    total += subtotal

    print(f"Subtotal: {moeda(subtotal)}")

    print("\n" + "="*30)
print("🧾 RESUMO DA COMPRA")
print("="*30)

for item in lista_compras:
    sub = item["preco"] * item["quantidade"]
    print(f"{item['nome']} ({item['quantidade']}x) - {moeda(sub)}")

print("="*30)
print(f"💰 TOTAL FINAL: {moeda(total)}")
print("="*30)