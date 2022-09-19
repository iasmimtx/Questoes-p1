def noves_fora(lista):
    lista1 = []
    somou = []
    fora = 0
    for i in lista:
        lista1.append(i)
    for numero in range(len(lista1)-1):
        somou.append((lista[numero] + lista[numero+1]))
        fora = somou[0] - 9
        


        
    return somou, fora

print(noves_fora([9, 7, 5, 4, 3, 1]))



'''

assert noves_fora([9, 7, 5, 4, 3, 1]) == (2, [[9, 7, 5, 4, 3, 1], 
                                              [7, 5, 4, 3, 1], 
                                              [4, 3, 3, 1], 
                                              [7, 3, 1], 
                                              [1, 1], 
                                              [2]])
assert noves_fora([4]) == (4, [[4]])
assert noves_fora([9]) == (0, [[9], [0]])
assert noves_fora([9, 9]) == (0, [[9, 9], [0]])'''