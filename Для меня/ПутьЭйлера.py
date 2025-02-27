n, m = map(int, input().split())
lists = [[] for i in range(n)]

    
#проверка на критерий эйлервого пути
degs = [0] * n
ver = 0
for i in range(m):
    u, v = map(int, input().split())
    lists[u].append(v)
    lists[v].append(u)
    if i == 0:
        ver = u
    degs[u] += 1
    degs[v] += 1
special = []
count = 0
for i in range(n):
    if degs[i]%2 != 0:
        count += 1
        special.append(i)
def dfss(u, components):
    visiteds[u] = True
    components.append(u)
    for v in lists[u]:
        if visiteds[v] == False:
            dfss(v, components)
visiteds = [False] * n
components = []
dfss(ver, components)

#поиск этого пути:
if count == 2 and len(components) == n:
    answer = []
    def way(cur):
        while lists[cur]:
            cur_new = lists[cur].pop()
            lists[cur_new].remove(cur)
            way(cur_new)
        answer.append(cur)
    way(special[0])
    print(answer)
else:
    print('no way')

