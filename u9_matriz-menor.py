#def matriz_menor(m1, m2):
'''m1 = [[1,2,3],
    [13,14,15],
    [7,8,9]]

m2= [[10,11,12],
         [4,5,6],
         [7,8,9]]'''
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

M1 = [[1,2,3],
          [13,14,15],
          [7,8,9]]
M2= [[10,11,12],
         [4,5,6],
         [7,8,9]]

M3= [[1,2,3],
         [0,0,0],
         [7,8,9]]

assert matriz_menor(M1, M2) == [[1,2,3],[4,5,6],[7,8,9]]
assert matriz_menor(M1, M3) == [[1,2,3],[0,0,0],[7,8,9]]