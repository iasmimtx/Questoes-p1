def soma_intervalo(a, b):
    soma = 0
    if a <= b:
        for numero in range(a, b + 1):
            soma += numero
    elif a == b:
        return a
    return soma
        

assert soma_intervalo(5,15) == 110
assert soma_intervalo(10,10) == 10