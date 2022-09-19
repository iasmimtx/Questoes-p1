def inserir(lista, valor, posicao):
    lista.append(lista[-1])
    for i in range(len(lista) - 2, posicao, -1):
        lista[i] = lista[i-1]
    lista[posicao] = valor

def insere_produto(menu, produto, preco):
    inseriu = False
    for i in range(len(menu)):
        if menu[i][1] > preco:
            inserir(menu, (produto, preco), i)
            inseriu = True
            break
    if not inseriu:
        menu.append((produto, preco)) 
