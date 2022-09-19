# Iasmim Maria Freire da Silva Torres
# UFCG - Programação 1 2021.1e

cont = []
while True:
    nomes_jogadores = input()
    
    if nomes_jogadores != '-':
        cont.append(nomes_jogadores)
        total = len(cont)
    if nomes_jogadores == '-': break
    
if len(cont) == 11:
    print(f'Modalidade -> Futebol')
elif len(cont) == 7:
    print(f'Modalidade -> Handebol')
elif len(cont) == 6:
    print(f'Modalidade -> Vôlei')
elif len(cont) == 5:
    print(f'Modalidade -> Basquete')
else:
    print('Equipe Inválida')

