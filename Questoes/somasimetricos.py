# Iasmim Maria Freire da Silva Torres
# UFCG - Programação 1 2021.1e
# Soma Simétricos- programa que soma o primeiro com último elemento
# da lista, o penúltimo com o segundo elemento da lista e 
# assim por diante.

def soma_simetricos(valores):
    soma = []
    for i in range(len(valores)//2):
        soma.append(valores[i] + valores[-i-1])
    if len(valores) % 2 != 0:
        soma.append(valores[len(valores)//2])
    return soma 

def test_1():
    assert soma_simetricos([2, 3, 6, 7]) == [9, 9]
def test_2():
    assert soma_simetricos([2, 3, 6, 7, 4]) == [6, 10, 6]
