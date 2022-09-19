def rotesq(array):
    if len(array) > 0:
        aux = array[0]
        for i in range(len(array) - 1):
            array[i] = array[i+1]
        array[-1] = aux
