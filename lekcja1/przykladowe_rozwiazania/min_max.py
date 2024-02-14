lista = [1, 3, 7, 11, 2, -6, 0]
najmniejsza = lista[0]
najwieksza = lista[0]

for i in lista:
    if najmniejsza > i:
        najmniejsza = i
    if najwieksza < i:
        najwieksza = i

print("najmniejsza liczba to:", najmniejsza)
print("największa liczba to:", najwieksza)
