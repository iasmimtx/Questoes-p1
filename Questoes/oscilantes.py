codigo = input()

verificacao = ''
for i in range(len(codigo)-1):
        if int(codigo[i]) % 2 == 0 == int(codigo[i + 1]) % 2 == 0 or int(codigo[i])% 2 != 0  == int(codigo[i + 1]) % 2 != 0 :
            verificacao += 'falso'
            break
        else:
            verificacao += 'verdadeiro'
            break
print(f'{verificacao}: {len(codigo)} algarismos.')
