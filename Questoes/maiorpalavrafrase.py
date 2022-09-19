def soma_diminui_vizinhos(valores):
    valor = 0
    for i in range(len(valores)):
        if valores == []:
            valor = 0
        if valores[i] % 3 == 0:
            valor -= valores[i]
        else:
            valor += valores[i]
    return valor

lista = [1, 2, 3]
print(soma_diminui_vizinhos(lista))
 