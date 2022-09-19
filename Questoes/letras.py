n = int(input())
cont = 0
igual = ''
nao_igual = ''
for i in range(n):
    entrada = input()
    encontrou = False
    for j in range (len(entrada)-1):
        if entrada[j] == entrada[j + 1] and not encontrou:
            encontrou = True
            cont += 1
            if igual != '':
                igual += '\n'
            igual += entrada
    if not encontrou:
        if nao_igual != '':
            nao_igual += '\n'
        nao_igual += entrada    
         
print(f'{cont} palavra(s) com letras dobradas:' )
if igual != '':
    print(igual)
print('---')
print(f'{n - cont} palavra(s) sem letras dobradas:')
if nao_igual != '':
    print(nao_igual)


    

