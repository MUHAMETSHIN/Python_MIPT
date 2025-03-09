import math
M = int(input())

G = {}

for i in range(M):
    v1,v2,w = input().split()
    w = float(w)
    if w < 0:
        w = math.log(float(-w))#считаем что курса который обнуляет не существует
    else:
        w = -math.log(float(w))

        
    if v1 in G:
        G[v1][v2] = w
    else:
        G[v1] = {v2:w}
    
def floyd_warshall(G):
    d = {i:{j:float('inf') for j in G} for i in G}
    for i in G:
        d[i][i] = 0
    for node1 in G:
        for node2 in G[node1]:
            d[node1][node2] = G[node1][node2]
    for i in G:
        for j in G:
            for k in G:
                d[j][k] = min(d[j][k],d[j][i]+d[i][k])
    for i in G:
        if d[i][i] < 0:
            return 'found'
    return 'not found'
    
print(floyd_warshall(G))
