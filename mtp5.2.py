# Iasmim Maria Freire da Silva Torres
# UFCG - Programação 1 2021.1e

entrada = (input().split())
x = int(entrada[0])
y = int(entrada[1])
    
cont = 0
while True:
    direcao = input().split()
    if direcao[0] == 'X': break
    if direcao[0] == 'B':
        x += int(direcao[1])
    elif direcao[0] == 'C':
        x -= int(direcao[1])
    elif direcao[0] == 'D':
        y += int(direcao[1])
    elif direcao[0] == 'E':
        y -= int(direcao[1])
    cont += int(direcao[1])
    print(x, y)
print(cont)
