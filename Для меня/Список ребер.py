n, m = map(int, input().split())
Mx = []
for i in range(m):
    u, v = map(int, input().split())
    Mx.append((u, v))
    Mx.append((v, u))
Mx.sort()
tab = [[-1, -1] for _ in range(n)]
print()
cur = Mx[0][0]#вершинка с минимальным индексом
tab[cur][0] = 0
for i in range(1,2*m):
    if cur != Mx[i][0]:
        tab[cur][1] = i#подписали конец
        cur = Mx[i][0]
        tab[cur][0] = i#подписали начало
tab[cur][1] = 2*m
print(Mx) 
print(tab)     

v = 4
for i in range(*tab[4]):
    print(Mx[i])

