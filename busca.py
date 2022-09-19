def busca_matriz(m,e):
    tem = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if busca_matriz[i][j] == e:
                 tem.append((i,j))
    return tem
