def caixa_registradora(vendas,meta):
    soma = 0
    comissao = 0
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
