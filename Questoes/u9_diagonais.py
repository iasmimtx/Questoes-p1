m = [[1,2,3],
     [4,5,6],
     [7,8,9]]


def diagonais(M):
    diagonal = []
    diagonal_sec = []
    for j in range(len(M)):
        diagonal.append(M[j][j])
        diagonal_sec.append(M[j][-(j+1)])
    return [diagonal, diagonal_sec]



















'''matriz = []
for i in range(len(m)):
    linhaP = []
    linhaS = []
    for j in range(len(m)):
        linhaP.append(m[j][j])
        linhaS.append(m[j][len(m)-1-j])
    matriz.append(linhaP)
    matriz.append(linhaS)

print(matriz)
'''