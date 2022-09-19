import math

hipotenusa = float(input('hipotenusa? '))
cateto = float(input('cateto? '))

cateto2 = math.sqrt(hipotenusa**2 - cateto**2)
print(f'hipotenusa: {hipotenusa:.2f}')
print(f'cateto 1: {cateto:.2f}')
print(f'cateto 2: {cateto2:.2f}')
