"""
=====================================================
            ESTUDOS SOBRE DICIONÁRIOS (dict)
=====================================================

Um dicionário armazena informações no formato:

chave : valor

Exemplo:

produto = {
    "id": 1,
    "nome": "Mouse",
    "preco": 80.00
}

"""

# ==========================================
# Criando um dicionário
# ==========================================

produto = {
    "id": 1,
    "nome": "Mouse",
    "preco": 80.00
}

print("=" * 50)
print("DICIONÁRIO")
print("=" * 50)

print(produto)


# ==========================================
# Acessando valores
# ==========================================

print("\nACESSANDO VALORES")

print(produto["nome"])
print(produto["preco"])


# ==========================================
# Alterando valores
# ==========================================

print("\nALTERANDO")

produto["preco"] = 95.00

print(produto)


# ==========================================
# Adicionando uma nova chave
# ==========================================

print("\nADICIONANDO")

produto["estoque"] = 20

print(produto)


# ==========================================
# keys()
# ==========================================

print("\nKEYS")

print(produto.keys())

for chave in produto.keys():
    print(chave)


# ==========================================
# values()
# ==========================================

print("\nVALUES")

print(produto.values())

for valor in produto.values():
    print(valor)


# ==========================================
# items()
# ==========================================

print("\nITEMS")

print(produto.items())

for chave, valor in produto.items():
    print(chave, "->", valor)


# ==========================================
# pop()
# ==========================================

print("\nPOP")

produto2 = produto.copy()

estoque = produto2.pop("estoque")

print("Valor removido:", estoque)

print(produto2)


# ==========================================
# popitem()
# ==========================================

print("\nPOPITEM")

produto3 = produto.copy()

ultimo = produto3.popitem()

print("Removido:", ultimo)

print(produto3)


# ==========================================
# update()
# ==========================================

print("\nUPDATE")

produto4 = produto.copy()

produto4.update({
    "preco":120,
    "marca":"Logitech"
})

print(produto4)


# ==========================================
# clear()
# ==========================================

print("\nCLEAR")

produto5 = produto.copy()

produto5.clear()

print(produto5)


# ==========================================
# len()
# ==========================================

print("\nLEN")

print(len(produto))


# ==========================================
# fromkeys()
# ==========================================

print("\nFROMKEYS")

novo = dict.fromkeys(
    ["nome","idade","cidade"],
    "Não informado"
)

print(novo)


# ==========================================
# setdefault()
# ==========================================

print("\nSETDEFAULT")

produto6 = {
    "nome":"Teclado"
}

produto6.setdefault("preco",150)

print(produto6)


# ==========================================
# Verificando existência
# ==========================================

print("\nIN")

print("nome" in produto)
print("marca" in produto)


# ==========================================
# Percorrendo o dicionário
# ==========================================

print("\nFOR")

for chave, valor in produto.items():
    print(f"{chave}: {valor}")