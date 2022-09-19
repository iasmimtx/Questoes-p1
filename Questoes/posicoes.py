v = input()
valores = input().split(' ')
achou = ''
for numero in range(len(valores)):
    if v == valores[numero]:
        achou += str(numero) + ' '

if achou != '':
    print(achou.rstrip())
else:
    print('-1')
