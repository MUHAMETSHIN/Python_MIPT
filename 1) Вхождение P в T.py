t = input('Введите текст:  ')
p = input('Что будем искать?:  ')
#реализуем хэширование:
#считаем два хеша для большей точности
def finder(t, p):
    lp = len(p)
    lt = len(t)
    m1 = 10**18 + 3
    m2 = 2**61 - 1
    p1 = 911382629
    p2 = 357142857
    st1 = [1]*(lt+1)
    st2 = [1]*(lt+1)
    for i in range(1, lt+1):
        st1[i] = (st1[i-1]*p1)%m1
        st2[i] = (st2[i-1]*p2)%m2
    double_p = p + p
    hashes1 = set()

    #хеши сдвигов 
    for i in range(lp):
        h1 = 0
        h2 = 0
        for j in range(lp):
            h1 = (h1 * p1 + ord(double_p[i+j])) % m1
            h2 = (h2 * p2 + ord(double_p[i+j])) % m2
        hashes1.add((h1, h2))

    pref_hashes1 = [0]*(lt+1)
    pref_hashes2 = [0]*(lt+1)
    #хеши префиксов
    for i in range(lt):
        pref_hashes1[i+1] = (pref_hashes1[i] * p1 + ord(t[i])) % m1
        pref_hashes2[i+1] = (pref_hashes2[i] * p2 + ord(t[i])) % m2
    def hash(l, r):
        hash1 = (pref_hashes1[r] - pref_hashes1[l] * st1[r - l] % m1 + m1) % m1
        hash2 = (pref_hashes2[r] - pref_hashes2[l] * st2[r - l] % m2 + m2) % m2
        return (hash1, hash2)
    ans = 0
    for i in range(lt-lp+1):
        cur = hash(i, i+lp)
        if cur in hashes1:
            ans+=1
    return ans
print(finder(t, p))
    
    
    


