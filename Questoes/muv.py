pos_inicial = float(input('Posição inicial? ')) #metros
v_inicial = float(input('Velocidade inicial? ')) #m/s
tempo = float(input('Tempo? ')) #s
aceleracao = float(input('Aceleração? ')) #m**2

v_final = v_inicial + (aceleracao * tempo)
v_media = (v_inicial + v_final) / 2
pos_final = pos_inicial + (v_inicial * tempo) + ((aceleracao * tempo**2) / 2)

print('\nDados da questão')
print('================')
print(f'   Posição inicial: {pos_inicial:.2f} m')
print(f'Velocidade inicial: {v_inicial:.2f} m/s')
print(f'        Aceleração: {aceleracao:.2f} m/s2')
print(f'             Tempo: {tempo:.2f} s')
print(f'  Velocidade final: {v_final:.2f} m/s')
print(f'  Velocidade média: {v_media:.2f} m/s')
print(f'     Posição final: {pos_final:.2f} m')
