# Iasmim Maria Freire da Silva Torres
# UFCG - Programação 1 2021.1e
# Checa Sequência de Dígitos

digitos = input()
limite = int(input())

i = 0
soma = 0
impares_seguidos = 0
while(i < len(digitos) and soma <= limite and impares_seguidos < 6):
    soma += int(digitos[i])    
    if (int(digitos[i]) % 2 == 1):
        impares_seguidos += 1
    else:
        impares_seguidos = 0
    i += 1

print(f'soma: {soma}')
print(f'números lidos: {i} de {len(digitos)}')

if impares_seguidos == 6:
    print('critério de parada: 6 ímpares')
elif (soma > limite):
    print('critério de parada: limite')
else:
    print('critério de parada: final da sequência')