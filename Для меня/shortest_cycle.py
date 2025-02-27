from queue import Queue
n, m, start = map(int, input().split())
neib = [set() for j in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    neib[v].add(u)
    neib[u].add(v)


def BFS(start):
    used = [False] * n
    d = [float('inf')] * n
    d[start] = 0
    q = Queue()
    q.put(start)
    while not q.empty():
        u = q.get()
        for v in neib[u]:
            if  used[v] == True:
                print(d[v] + 1)
                exit()


            if d[v] == float('inf'):
                used[v] == True
                d[v] = d[u] + 1
                q.put(v)
BFS(start)