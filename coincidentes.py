n1 = input().split()
n2 = input().split()

coincidentes = 0
if len(n1) < len(n2):
    for i in range(len(n1)):
        if n1[i] == n2[i]:
            coincidentes += 1
            print(f"i = {i}:  {n1[i]}")
elif len(n1) > len(n2):
    for j in range(len(n2)):
        if n2[j] == n1[j]:
            coincidentes += 1
            print(f"i = {j}: {n1[j]}")
else:
    for k in range(len(n1)):
        if n1[k] == n2[k]:
            coincidentes += 1
            print(f"i = {k}: {n1[k]}")

percento = (coincidentes * 100)/(len(n1) + len(n2)) 
print(f"Valores coincidentes: {coincidentes} ({percento:.0f}%)")