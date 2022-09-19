# Iasmim Maria Freire da Silva Torres
# UFCG - Programação 1 2021.1e

def compara_senhas(senha1, senha2):
    compara = 0
    for carac in range(len(senha2)):
            if carac < len(senha1) and senha1[carac] != senha2[carac]:
                compara += 1
    return compara
