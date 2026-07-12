nomes1 = {"Carlos", "Josiel", "Jandira", "Aline"}
nomes2 = {"Aline", "Carlos", "Jaqueline", "Altair"}

uniao = nomes1.union(nomes2)
interseccao = nomes1.intersection(nomes2)
diferenca_simetrica = nomes1.symmetric_difference(nomes2)

print("Pessoas presentes nos dois grupos:", interseccao)
print("Quantidade:", len(interseccao))

print("\nPessoas presentes apenas em um grupo:", diferenca_simetrica)
print("Quantidade:", len(diferenca_simetrica))

print("\nTodas as pessoas sem repetir:", uniao)
print("Quantidade:", len(uniao))





