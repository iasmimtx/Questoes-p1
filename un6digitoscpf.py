def calcula_dv(cpf):
    cont = 2
    soma = 0
    for i in range(len(cpf)-1,-1,-1):
        soma += int(cpf[i]) * cont
        cont += 1
    dv = (soma * 10) % 11
    if dv == 10:
        dv = 0
    return dv

def calcula_digitos_verificacao(cpf):
    dv1 = calcula_dv(cpf)
    dv2 = calcula_dv(cpf + str(dv1))
    return str(dv1) + str(dv2)
assert calcula_digitos_verificacao('153245875') == '40'