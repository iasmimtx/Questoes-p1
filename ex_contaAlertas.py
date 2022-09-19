def conta_alertas_acude(medicoes):
    soma = 0
    for i in range(len(medicoes)):
        if medicoes[i] < 17 and (i == 0 or abs(medicoes[i] - medicoes[i-1]) < 10):
            soma += 1    
    return soma


medicoes = [50, 50, 50, 23, 21, 17, 15, 60, 65, 15, 15]
#assert conta_alertas_acude(medicoes) == 2

print(conta_alertas_acude([50, 50, 50, 23, 21, 17, 15, 60, 65, 15, 15]))
'''O critério para descartar medições não confiáveis é que a diferença (em módulo) de uma medição e a
anterior seja maior ou igual a 10. Assim, por exemplo, se a n-ésima medição for 15 e a (n+1)-ésima for 60,
pode-se assumir que a medição é não confiável e que, portanto, o alarme não deveria ter sido emitido.'''
