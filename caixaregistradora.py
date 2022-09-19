def caixa_registradora(vendas,meta):
    soma,comissao = 0,0
    lista = []
    lucro = ''
    for i in vendas:
        soma += i
    for i in range(len(vendas)):
        if vendas[i] < 1000.0:
            comissao += vendas[i] * 0.05
        elif vendas[i] >= 1000.0 and vendas[i] < 5000.0:
            comissao += vendas[i] * 0.1
        elif vendas[i] >= 5000.0:
            comissao += vendas[i] * 0.15
    if soma >= meta:
        lucro += 'Lucro'
    else:
        lucro +='Prejuizo'
    lista += soma,comissao,lucro 
    return lista

    
print(caixa_registradora([1000.0, 2000.0, 5000.0, 2500.0, 950.0], 2000.0))

     
