from queue import Queue
M, N = map(int, input().split())
G = {}

for i in range(M):
    v1,v2,w = map(int, input().split())
    if v1 in G:
        G[v1][v2] = w
    else:
        G[v1] = {v2:w}
    if v2 in G:
        G[v2][v1] = 0
    else:
        G[v2] = {v1:0}
#бфс ищем мин поток на мин пути из старта в финиш, сразу сохраняем путь в финиш
def Bfs(G, start, finish, N, M):
    q = Queue()
    parents = {start:-1}
    visited = [False] * N
    flow = {i:0 for i in range(N)}
    flow[start] = float("inf")
    visited[start] = True
    q.put(start)
    while not q.empty():
        u = q.get()
        for v in G[u]:
            if not visited[v] and G[u][v] > 0:
                visited[v] = True
                parents[v] = u
                flow[v] = min(flow[u], G[u][v])
                if v == finish:
                    return flow[finish], parents
                q.put(v)
    return 0, None
#увеличиваем возможный поток и перестаиваем ост сеть
def ford_fulkerson(G,start,finish):
    res = 0
    while True:
        flow, par = Bfs(G, start, finish, N, M)
        if flow == 0:
            break
        res += flow
        cur = finish
        while cur != start:
            u = par[cur]
            G[u][cur] -= flow
            G[cur][u] += flow
            cur = u
    return res

print(ford_fulkerson(G, 0, 3))