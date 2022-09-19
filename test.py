

while True:
    registro = input()
    if registro == '-': break
    cont = 0
    i = 0
    reprov = 0
    while i < len(registro):
        if registro[i] == 'f':
                cont += i
                if int(cont) >= 3:
                    reprov += 1
        i += 1
        break
    print(reprov)