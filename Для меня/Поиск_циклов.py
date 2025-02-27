n, m = map(int, input().split())
lists = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    lists[u].append(v)
    lists[v].append(u)
def dfs(u, p):
    visited[u] = True
    for v in lists[u]:
        if visited[v] == False:
            dfs(v, u)
        elif v != p:
            print('YES')
            exit()

visited = [False] * n

for u in range(n):
    if not visited[u]:
        dfs(u, -1)