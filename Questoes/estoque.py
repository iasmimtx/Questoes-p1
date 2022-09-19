def balanco(estoque1, estoque2):
    balanco = {}
    for k in estoque1.keys():
        balanco[k] = estoque1[k]
    for k in estoque2.keys():
        if k in balanco:
            balanco[k] += estoque2[k]
        else:
            balanco[k] = estoque2[k]
    return balanco

