def soma_diminui_vizinhos(valores):
    valor = 0
    for i in range(len(valores)):
        if (i+1) % 3 == 0:
            valor -= valores[i]
        else:
            valor += valores[i]
    return valor
