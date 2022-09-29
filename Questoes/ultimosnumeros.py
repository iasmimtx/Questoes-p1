# Iasmim Maria Freire da Silva Torres
# UFCG - Programação 1 2021.1e
# Somando os Ultimos Números

n = int(input())
soma = 0
lista = []
maior = 0
for i in range(n):
    entrada1 = int(input())
    lista.append(entrada1)
    soma += entrada1
    
media = soma / n
for j in range(n-1, -1, -1):
    maior += lista[j]
    if lista[j] >= media: break
    
print(maior)
