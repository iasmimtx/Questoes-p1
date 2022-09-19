# Iasmim Maria Freire da Silva Torres
# UFCG - Programação 1 2021.1e

def compara_senhas(senha1, senha2):
    compara = 0
    for carac in range(len(senha2)):
            if senha1[carac] != senha2[carac]:
                compara += 1
    return compara

assert compara_senhas('nome123', 'nome') == 0
assert compara_senhas('aaa', 'bbb') == 3
assert compara_senhas('senha', 'Senha') == 1