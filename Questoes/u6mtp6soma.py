# Iasmim Maria Freire da Silva Torres
# UFCG - Programação 1 2021.1e

def soma_simetricos(valores):
    resultado = []
    for i in range(len(valores)//2):
        resultado.append(valores[i] + valores[-i-1])
    if (len(valores) % 2 != 0):
        resultado.append(valores[len(valores)//2])
    return resultado