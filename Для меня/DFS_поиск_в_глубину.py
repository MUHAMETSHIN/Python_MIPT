n, m = map(int, input().split())
lists = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    lists[u].append(v)
    lists[v].append(u)

#дфс
def dfs(u, components):
    visited[u] = True
    components.append(u)
    for v in lists[u]:
        if visited[v] == False:
            dfs(v, components)
visited = [False] * n

count = 0

#вывод компонент связности
for u in range(n):
    if not visited[u]:
        components = []
        count += 1
        dfs(u, components)
        print()
        print(*components)
       
print()
print(count)        
        


