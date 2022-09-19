def reducoes(seq):
    lista = []
    for i in range(len(seq)-1):
        if seq[i] - seq[i+1] < 0:
            lista.append(0)
        elif seq == [] or len(seq) == 1:
            lista = []
        else:
            lista.append(seq[i] - seq[i+1])
    return lista
        
print(reducoes([4, 2, 0, 6, 3, 4]))
print(reducoes([3, 0, 3, 6, 1]))