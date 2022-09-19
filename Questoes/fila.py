# Iasmim Maria Freire da Silva Torres
# UFCG - Programação 1 2021.1e

sim = 0
nao = 0
while True:
    entrada = input()
    if entrada == '###': break
    i = 0
    seguiu = True
    fim = False
    while (i < len(entrada)):
        if entrada[i] =='a':
            fim = True
        else:
            if fim:
                seguiu = False
                break
        i += 1
    if seguiu:
        sim += 1
    else:
        nao += 1
print(f'sim: {sim}')
print(f'não: {nao}')

