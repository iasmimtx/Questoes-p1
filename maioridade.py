def maioridade_penal(nomes, idades):
    lista_nomes = nomes.split(' ')
    lista_idades = idades.split(' ')
    maioridade = ''
    for i in range(len(lista_idades)):
        if int(lista_idades[i]) >= 18:
            if maioridade != '':
                maioridade += ' '
            maioridade += lista_nomes[i]
    return maioridade
    

assert maioridade_penal("Jansen Italo Ana","14 21 60") == "Italo Ana"
assert maioridade_penal("Jansen Italo Ana","14 21 60") == "Italo Ana"