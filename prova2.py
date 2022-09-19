# Iasmim Maria Freire da Silva Torres
# UFCG - Programação 1 2021.1e
# Ofuscador - programa que troca letras para o código
# ficar mais difícil de ser compreendido por humanos.

def ofuscador(linha):
    string = ''
    linha_dividida = linha.split()
    palavra_atual = 0
    for i in range(len(linha)):
        codigo = ord(linha[i])
        letra = ''
        if codigo >= 65 and codigo <= 90:
            letra = chr(codigo + 32)
        elif codigo >= 97 and codigo <= 122:
            letra = chr(codigo - 32)
        else:
            letra = linha[i]
        if letra == 'A' or letra == 'a':
            string += '4'
        elif letra == 'B' or letra == 'b':
            string += '8'
        elif letra == 'E' or letra == 'e':
            string += '3'
        elif letra == 'G' or letra == 'g':
            string += '6'
        elif letra == 'I' or letra =='i':
            string += '1'
        elif letra == 'L' or letra == 'l':
            string += '7'
        elif letra == 'S' or letra == 's':
            string += '5'
        elif letra == 'O' or letra == 'o':
            string += '0'
        elif letra == ' ':
            for j in range(len(linha_dividida[palavra_atual])):
                string += '*'
            palavra_atual += 1
        else:
            string += letra
    return string
            
def test_1():
    linha2 = "estudo na UFCG"
    assert ofuscador(linha2) == "35TUD0******N4**UFC6"
def test_2():
    linha3 = "Moro em New York!"
    assert ofuscador(linha3) == "m0R0****3M**n3W***y0RK!"
def test_2():
    linha3 = "Pulei de paraquedas!"
    assert ofuscador(linha3) == "pU731*****D3**P4R4QU3D45!"