M, N = map(int, input().split())

G = {}

for i in range(M):
    v1,v2 = input().split()
    if v1 in G:
        G[v1].add(v2)
    else:
        G[v1] = {v2}
    if v2 in G:
        G[v2].add(v1)
    else:
        G[v2] = {v1}


def dfs(G,visited,matching,start):
    if start in visited:
        return False
    visited.add(start)
    for i in G[start]:
        if not matching[i] or dfs(G,visited,matching,matching[i]):
            matching[i] = start
            matching[start] = i
            return True            
    return False

def Kuhn(G):
    matching = {i:None for i in G}
    for i in G:
        print(matching)
        visited = set()
        if not matching[i]:
            dfs(G,visited,matching,i)
    return matching

matching = Kuhn(G)
edges= set()
for u, v in matching.items():
    if u < v:
        edges.add((u, v))
unedges = {v for v in G if matching[v] is None}
for u in unedges:
    for v in G[u]:
        if (v, u) not in edges and (u, v) not in edges:
            edges.add((u, v))
            break 
print(edges)



        