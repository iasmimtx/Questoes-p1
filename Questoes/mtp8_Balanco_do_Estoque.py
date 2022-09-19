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

d1 = {"manteiga": 10, "biscoito": 20, "chocolate": 30}
d2 = {"manteiga": 10, "gelatina": 40}
assert balanco(d1, d2) == {"manteiga": 20, "biscoito": 20,
"chocolate": 30, "gelatina": 40}
assert d1 == {"manteiga": 10, "biscoito": 20, "chocolate": 30}
assert d2 == {"manteiga": 10, "gelatina": 40}