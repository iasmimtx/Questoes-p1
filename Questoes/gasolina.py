pos_inicial = float(input())
litros_inicial = float(input())
pos_final = float(input())
litros_final = float(input())

dist = pos_final - pos_inicial
delta_consumo = litros_inicial - litros_final
final = dist / delta_consumo

print (f'{final:.1f}')
                         
