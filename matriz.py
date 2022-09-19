def matriz_menor(m1,m2):
    matriz = []
    for i in range(len(m1)):
        linha = []
        for j in range(len(m1[i])):
            if m1[i][j] < m2[i][j]:
                linha.append(m1[i][j])
            else:
                linha.append(m2[i][j])
        matriz.append(linha) 
    return matriz 
