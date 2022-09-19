entrada = float(input())
quebra = entrada / 2
valores = ''
while True:
    sequencia = input().split()
    if sequencia[0] == 'fim': break
    cont = 0
    for ind in sequencia:
        cont += int(ind)
    media2 = cont / len(sequencia)
    if media2 < quebra: break
    if media2 > entrada:
        for i in sequencia:
            if len(sequencia) - 1 == i:
                valores += i
            else:
                valores += i + ' '
print(valores)

