def conta_alertas_acude(medicoes):
    soma = 0
    for i in range(len(medicoes)):
        if medicoes[i] < 17 and (i == 0 or abs(medicoes[i] - medicoes[i-1]) < 10):
            soma += 1    
    return soma


