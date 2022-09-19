acumulador = 0
while True:
    entrada = input()
    if entrada == '-': break
    i = 0
    faltas = 0
    while i < len(entrada):
        if entrada[i] == 'f':
            faltas += 1
        i += 1 
    if faltas > 8:
        acumulador += 1 
print(f'{acumulador} aluno(s) reprovado(s) por falta.')
