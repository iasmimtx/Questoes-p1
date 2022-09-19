# Iasmim Maria Freire da Silva Torres
# UFCG - Programação 1 2021.1e
# Filtra linhas

cont = 0
invalidas = 0
while True:
    entrada = input()
    lista_dividida = entrada.split(' ')
    if entrada == 'fim': break
    cont += 1 
    par = 0
    impar = 0
    for numero in lista_dividida:
        if int(numero) % 2 == 0:
            par += 1
        else:
            impar += 1
    if impar > par:
        print(f'linha {cont} inválida: {entrada}') 
        invalidas += 1
print(f'sequências lidas: {cont} (inválidas: {invalidas})')

    

