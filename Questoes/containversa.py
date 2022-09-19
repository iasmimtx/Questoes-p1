palavra = input()

soma = 0
for i in range(len(palavra)):
    if palavra[i] == palavra[len(palavra)-i-1]:
        soma += 1
print(f'A palavra {palavra} contém {soma} caractere(s) coincidente(s) com a sua inversa.' )


