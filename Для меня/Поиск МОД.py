n, m = map(int, input().split())
lists = [[] for i in range(n)]
for i in range(m):
    u, v, w = map(int, input().split())
    lists[u].append((v,w))
    lists[v].append((u,w))
s = [0]
weight = 0
d = []
for i in range(n-1):
    for u in s:
        min_w = float("inf")
        e = None
        for v, w in lists[u]:
            if v in s:
                continue
            elif w < min_w:
                min_w = w
                e = (u, v, w)
        weight += w
        s.append(e)
        d.append(e)
        
