# Iasmim Maria Freire da Silva Torres
# Matrícula: 121110942
# UFCG - Programação 1 2021.1e
# Letras Distintas - programa que calcula letras distintas


palavra1 = input()
palavra2 = input()


soma = 0
for i in range(len(palavra1)):
    aux = False
    for j in range(len(palavra2)):
        if palavra1[i] == palavra2[j]:
            aux = True
    if not aux:
        soma += 1

print(soma)


