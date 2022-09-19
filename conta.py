def calcula_conta(tabela):
    consumo = 0
    for i in range(1, len(tabela)):
        consumo += tabela[i][1] * tabela[i][2] * tabela[i][3]
    return f'R$ {consumo * 0.28 / 1000:0.2f}'
