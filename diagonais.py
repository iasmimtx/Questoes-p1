def diagonais(M):
    diagonal = []
    diagonal_sec = []
    for j in range(len(M)):
        diagonal.append(M[j][j])
        diagonal_sec.append(M[j][-(j+1)])
    return [diagonal, diagonal_sec]
