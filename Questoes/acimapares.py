n = int(input())

cont = 0
soma = 0
num = []
for i in range(n):
    entrada = int(input())
    num.append(entrada)
    if entrada % 2 == 0:
        cont += 1
        soma += entrada

        
media = soma / cont
contador = 0
for end in num:
    if end > media:
        contador += 1
print(f'média dos pares: {media:.1f}')
print(f'acima da média: {contador}')




