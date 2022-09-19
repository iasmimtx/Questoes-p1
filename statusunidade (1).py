minitestes = int(input())
notas= []
soma = 0
for i in range(minitestes):
    nota = float(input())
    notas.append(nota)
    soma += nota

media = soma / minitestes

if minitestes == 1:
    print(media)
    print('Aluno ainda não aprovado na unidade')
elif minitestes == 2:
    if media < 6.0:
        print(media)
        print('Aluno ainda não aprovado na unidade')
    elif media >= 6.0:
        print(media)
        print('Aluno aprovado na unidade')
elif minitestes > 2:
    media = media - (0.5*(minitestes-2))
    if media < 6.0:
        print(media)
        print('Aluno ainda não aprovado na unidade')
    elif media >= 6.0:
        print(media)
        print('Aluno aprovado na unidade')