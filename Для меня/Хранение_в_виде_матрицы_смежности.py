n, m = map(int, input().split())
M = [[0]*n for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    M[u][v] = 1
    M[v][u] = 1 #не ориентированный граф
    
