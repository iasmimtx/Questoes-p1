def is_substring(str1, str2):
    for i in range(len(str1) - len(str2) + 1):
        i_atual = i
        encontrou = True
        for j in range(len(str2)):
            if str1[i_atual] != str2[j]:
                encontrou = False
                break
            i_atual += 1

        if encontrou:
            return True
    return False


#assert is_substring('boiada','oi')
#assert not is_substring('casorio', 'casa')


'''is_substring('boiada', 'oi')
print(is_substring)'''