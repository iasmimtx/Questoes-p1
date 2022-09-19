# Iasmim Maria Freire da Silva Torres
# UFCG - Programação 1 2021.1e
# Filtra linhas- programa que exibe linhas inválidas,
# ou seja, mostra as linhas que tem mais números impares 
# que números pares e no final da a quantidade de linhas lidas e 
# quantidade de linhas inválidas.

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

    


