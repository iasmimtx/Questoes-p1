def multiplica_lista(n, lista):
    nova_lista = []
    for i in range(n):
        if n == 0:
            nova_lista = []
        nova_lista += lista
    return nova_lista
l = ['joao', 'pedro']
assert multiplica_lista(2,l) == ['joao', 'pedro', 'joao', 'pedro']