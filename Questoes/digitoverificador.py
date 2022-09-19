n = input()

soma = 0
for i in range(len(n)):
    soma += int(n[i])

print(f'{n}-{(soma % 11):02d}')


