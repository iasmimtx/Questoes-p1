p1 = input().split()
p2 = input().split()

print('Letras coincidentes')

cont = 0
coincidentes = 0
if p1 < p2:
    for i in range(len(p1)):
        if p1[i] == p2[cont]:
            coincidentes += 1
            print(f"'{p1[i]}' na posição {i+1}")
        cont += 1
elif p1 > p2:
    for j in range(len(p2)):
        if p2[j] == p1[cont]:
            coincidentes += 1
            print(f"'{p1[j]}' na posição {j+1}")
        cont += 1
else:
    for k in range(len(p1)):
        if p1[k] == p2[cont]:
            coincidentes += 1
            print(f"'{p1[k]}' na posição {k+1}")
        cont += 1

#Total de letras coincidentes
percento = (coincidentes * 100)/(len(p1) + len(p2)) 
print(f"Total de letras coincidentes: {coincidentes} ({percento:.0f}%)")