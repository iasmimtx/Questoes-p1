def conta_alertas_acude(medicoes):
    soma = 0
    for i in range(len(medicoes)):
        if medicoes[i] < 17 and (i == 0 or abs(medicoes[i] - medicoes[i-1]) < 10):
            soma += 1    
    return soma


medicoes = [50, 50, 50, 23, 21, 17, 15, 60, 65, 15, 15]
#assert conta_alertas_acude(medicoes) == 2

print(conta_alertas_acude([50, 50, 50, 23, 21, 17, 15, 60, 65, 15, 15]))
