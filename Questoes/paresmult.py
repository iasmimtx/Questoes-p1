n1 = input().split(' ')
n2 = int(input())
resultado = []
cont = 0
for i in range(len(n1)-1):
    if int(n1[i]) * n2 == int(n1[i + 1]) or int(n1[i]) == int(n1[i + 1]) * n2:
        cont += 1
        resultado.append(f'{n1[i]} {n1[i + 1]}') 
print(f'{cont} par(es)')
for j in resultado:
    print(j)

