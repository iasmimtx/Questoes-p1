def decifra(chave, mensagem):
    palavra = ''
    for c in mensagem:
        palavra += chave[c]
    return palavra