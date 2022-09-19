      
def posicao_ele(valor, buscar):
    valor = valor
    buscar = buscar
    tem = ''
    for i in range(len(buscar)):
        for numero in int(valor):
            if int(valor[numero] == buscar[i]):
                tem += str(i) + ' '
    return tem.rstrip()
lista = [8, 4, 12, 7, 10, 6] 
assert posicao_ele(7, lista) == '3 2'