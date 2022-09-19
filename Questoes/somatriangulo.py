def soma_triangulo_superior(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j > i and j < len(matriz[i]) - 1 - i:
                soma += matriz[i][j]
    return soma
