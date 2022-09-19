num_conta = input()
soma = 0
for i in range(len(num_conta)):
    soma += int(num_conta[i])

div = soma % 11
if div == 10:
    print(f'{num_conta}-X')
else:
    print(f'{num_conta}-{div}')