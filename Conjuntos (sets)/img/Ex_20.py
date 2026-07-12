conj1 = {1, 2, 3, 4,}
conj2 = {3, 4, 5, 6,}

print("Primeiro conjunto: ", conj1)
print("Segundo conjunto: ", conj2)

uniao =conj1.union(conj2)
intersecção = conj1.intersection(conj2)
diferença = conj1.difference(conj2)
simetrica = conj1.symmetric_difference(conj2)

print("União dos conjuntos: ", uniao)
print("Intersecção dos conjuntos: ", intersecção)
print("Diferença entre os conjuntos: ", diferença)
print("Diferença simetrica entre os conjuntos: ", simetrica)

