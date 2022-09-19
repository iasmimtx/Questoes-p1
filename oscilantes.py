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

        
'''Escreva um programa que receba um código gerado para acesso a um formulário online e verifica se ele é "verdadeiro" ou "falso".
 Um código verificado como "verdadeiro" é composto por uma sequência de dígitos que se alternam entre pares e ímpares ou entre ímpares e pares.
Não são admitidos dígitos pares ou ímpares juntos.
 Por exemplo, o código 7852 é verificado como verdadeiro, porque 7 é ímpar; 8 é par; 5 é ímpar e 2 é par.'''