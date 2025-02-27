n, m = map(int, input().split())
lists = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    lists[u].append(v)
    lists[v].append(u)
def dfs(u, p):
    global is_cycle_found
    global current_v
    visited[u] = True
    for v in lists[u]:
        if is_cycle_found:
            break
        if visited[v] == False:
            dfs(v, u)
        elif v != p:    #если сосед уже посещен, то цикл
            current_v = v
            is_cycle_found = True
    if is_cycle_found:
        print(u, end = ' ')   
    if u == current_v:
        exit()

visited = [False] * n
is_cycle_found = False
current_v = -1
for u in range(n):
    if not visited[u]:
        dfs(u, -1)  