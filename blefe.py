def blefe(lista):
    if len(lista) == 0:
        return []
    alteracoes = [0]
    for i in range(1, len(lista)):
        if lista[i] > lista[i-1]:
            alteracoes.append(lista[i] - lista[i-1])
            lista[i] = lista[i-1]
        else:
            alteracoes.append(0)
    return alteracoes
