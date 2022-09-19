cont = 0
while True:
    vogal = 0
    consoante = 0
    vogais = 'AaEeIiOoUu'
    entrada = input()
    for letra in entrada:
        e_vogal = False
        for v in vogais:
            if letra == v:
                e_vogal = True 
                break
        if e_vogal:
            vogal += 1
        else:
            consoante += 1
    cont += 1
    if consoante > vogal: break
print(cont)
