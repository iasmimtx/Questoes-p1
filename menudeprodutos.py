def insere_produto(menu, produto, preco):
    for i in range(len(menu)):
        if menu[i][1] >= preco:
            menu.insert(i, (produto, preco)) 


def test_exemplo_1():
    menu = [("expresso", 5.29), ("duplo", 8.09), ("capuccino", 10.59)]
    insere_produto(menu, "latte", 9.59)
    assert menu == [("expresso", 5.29), ("duplo", 8.09), 
                    ("latte", 9.59), ("capuccino", 10.59)]