tipo = input()
area = float(input())
quantidade = 0
valor = 0
if tipo == 'Fungicida':
    quantidade += (area * 1)
    valor += (quantidade * 320) / area
elif tipo == 'Herbicida':
    quantidade += area * 0.3
    valor += quantidade * 100
elif tipo == 'Inseticida':
    quantidade += area * 2.5
    valor += quantidade * 400

print(f"{quantidade:.0f} {tipo}(s)\nR$ {valor:.2f}")
                                                                               
                                                                               
                                                                               
