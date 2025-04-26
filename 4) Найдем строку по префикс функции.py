def pref2str(p, alphabet):

    n = len(p)
    s = [None] * n
    s[0] = alphabet[0]
    banned = [set(s[0]) for _ in range(n)]  #аналогично восстановлению строки по z-функции
    
    for i in range(1, n):
        if p[i] > 0:
            for j in range(p[i]):
                s[i - p[i] + j +1] = s[j]
            if i+1 < n:
                banned[i+1].add(s[p[i]])

        else:
            # Выбираем минимальный разрешённый символ
            for c in alphabet:
                if c not in banned[i]:
                    s[i] = c
                    break
            
    return "".join(s)
#ананас
p = [0, 0, 1, 2, 3, 0]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(pref2str(p, alphabet))

