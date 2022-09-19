def busca_matriz(m,e):
    tem = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if matriz[i][j] == e:
                tem.append((i,j))
    return tem

matriz = [
    [2, 3, 5, 3, 1],
    [3, 2, 1, 5, 6],
    [1, 2, 3, 2, 1],
]

print(busca_matriz(matriz, 3))
#assert busca_matriz(matriz, 4) == []
#assert set(busca_matriz(matriz, 3)) == set( [(0,1), (0,3), (1,0), (2,2)] )