def z2str(z, alphabet):
    n = len(z)
    s = [None] * n
    s[0] = alphabet[0]# все равно не сможем его определить так что пусть он первый из алфавита
    continued = [set(s[0]) for _ in range(n)]#будем отслеживать какие буквы нельзя ставить на iом месте чтобы случайно не увеличить z функцию 
    for i in range(1, n):
        if z[i] > 0:
            for j in range(z[i]):
                s[i + j] = s[j]
            if i+z[i] < n:
                continued[i+z[i]].add(s[j+1])
        else:
            # Выбираем минимальный разрешённый символ
            for c in alphabet:
                if c not in continued[i]:
                    s[i] = c
                    break
    return "".join(s)
#ananas:
z = [0, 0, 0, 1, 4, 0, 0, 1]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(z2str(z,alphabet))






