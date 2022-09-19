perder = int(input())
tempo = int(input())
calorias = int(input())

calorias_perder = perder * 7700
calorias_dia = (tempo * 900) + 2000 - calorias

dias = calorias_perder / calorias_dia

print(f'Você precisará de {dias:.2f} dias de dieta')
