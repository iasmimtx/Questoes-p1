def divisor(num, lista):
    for i in range(len(lista)):
        if lista[i] % num == 0:
            return i
    return -1
