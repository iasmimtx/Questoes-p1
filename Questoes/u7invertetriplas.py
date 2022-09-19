def inverte3a3(s):
    invertidas = ''
    for i in range(len(s)-3,-1,-3):
        invertidas += s[i] + s[i+1] + s[i+2]
    return invertidas

assert inverte3a3("abcdef") == "defabc"
assert inverte3a3("abcdefghijkl") == "jklghidefabc"