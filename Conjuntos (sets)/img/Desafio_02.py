"""
=====================================================
                ESTUDOS SOBRE SETS
=====================================================

Set (conjunto) é uma coleção que:
✔ Não permite elementos repetidos.
✔ Não possui ordem.
✔ É mutável (pode adicionar e remover elementos).

"""

# ==========================================
# Criando um conjunto
# ==========================================

grupo1 = {"Carlos", "Josiel", "Jandira", "Aline"}
grupo2 = {"Aline", "Carlos", "Jaqueline", "Altair"}

print("=" * 50)
print("CONJUNTOS")
print("=" * 50)

print("Grupo 1:", grupo1)
print("Grupo 2:", grupo2)


# ==========================================
# União
# ==========================================

print("\nUNIÃO (union)")
print(grupo1.union(grupo2))
print(grupo1 | grupo2)


# ==========================================
# Interseção
# ==========================================

print("\nINTERSEÇÃO (intersection)")
print(grupo1.intersection(grupo2))
print(grupo1 & grupo2)


# ==========================================
# Diferença
# ==========================================

print("\nDIFERENÇA (difference)")
print(grupo1.difference(grupo2))
print(grupo1 - grupo2)


# ==========================================
# Diferença Simétrica
# ==========================================

print("\nDIFERENÇA SIMÉTRICA")
print(grupo1.symmetric_difference(grupo2))
print(grupo1 ^ grupo2)


# ==========================================
# Quantidade de elementos
# ==========================================

print("\nQUANTIDADE")

print("Grupo 1:", len(grupo1))
print("Grupo 2:", len(grupo2))
print("Total sem repetir:", len(grupo1.union(grupo2)))


# ==========================================
# Verificando existência
# ==========================================

print("\nVERIFICAÇÃO")

print("Carlos" in grupo1)
print("Maria" in grupo1)

print("Maria" not in grupo1)


# ==========================================
# Adicionando elementos
# ==========================================

print("\nADD")

grupo3 = grupo1.copy()

grupo3.add("Maria")
print(grupo3)


# ==========================================
# Adicionando vários elementos
# ==========================================

print("\nUPDATE")

grupo3.update({"José", "Pedro"})

print(grupo3)


# ==========================================
# Removendo elementos
# ==========================================

print("\nREMOVE")

grupo4 = grupo3.copy()

grupo4.remove("Pedro")

print(grupo4)


# ==========================================
# DISCARD
# ==========================================

print("\nDISCARD")

grupo4.discard("João")

print(grupo4)


# ==========================================
# POP
# ==========================================

print("\nPOP")

grupo5 = grupo4.copy()

elemento = grupo5.pop()

print("Elemento removido:", elemento)
print(grupo5)


# ==========================================
# CLEAR
# ==========================================

print("\nCLEAR")

grupo6 = grupo5.copy()

grupo6.clear()

print(grupo6)


# ==========================================
# COPY
# ==========================================

print("\nCOPY")

copia = grupo1.copy()

print(copia)


# ==========================================
# ISSUBSET
# ==========================================

print("\nISSUBSET")

a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))


# ==========================================
# ISSUPERSET
# ==========================================

print("\nISSUPERSET")

print(b.issuperset(a))


# ==========================================
# ISDISJOINT
# ==========================================

print("\nISDISJOINT")

x = {10, 20}
y = {30, 40}

print(x.isdisjoint(y))


# ==========================================
# Percorrendo um Set
# ==========================================

print("\nFOR")

for pessoa in grupo1:
    print(pessoa)


# ==========================================
# Converter Lista em Set
# ==========================================

print("\nLISTA -> SET")

lista = [1, 2, 2, 3, 3, 4, 4, 5]

novo_set = set(lista)

print(novo_set)


# ==========================================
# Converter Set em Lista
# ==========================================

print("\nSET -> LISTA")

lista2 = list(novo_set)

print(lista2)