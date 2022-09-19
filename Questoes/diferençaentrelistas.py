def diferenca_listas(lista1, lista2):
    for i in range(len(lista1)-1, -1, -1):
        for v in lista2:
            if lista1[i] == v:
                lista1.pop(i)

lista1 = [2, 1, 3, 4]
lista2 = [2]
diferenca_listas(lista1, lista2) == [1, 3, 4]
assert lista1 == [1, 3, 4]