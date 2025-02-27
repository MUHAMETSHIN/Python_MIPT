n, m = map(int, input().split())
lists = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    lists[u].append(v)
    lists[v].append(u)
visited = []
colors = [0] * n
def dfs(u):
    colors[u] = 1
    for v in lists[u]:
        if colors[v] == 0:
            dfs(v)
        elif colors[v] == 1:
            print('yes')
            exit()
    colors[u] = 2
