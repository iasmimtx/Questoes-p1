def soma_diagonais(M):
    soma = 0
    for i in range(len(M)):
        soma += (M[i][i])
        soma += (M[i][-(i+1)])
    if len(M) % 2 == 1:
        index = len(M) // 2
        soma -= M[index][index]
    return soma


M = [[1,4],
     [0,9]]
print(soma_diagonais(M))