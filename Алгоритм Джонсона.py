def bellman_ford(lists, start):
    d = {i: float('inf') for i in range(len(lists))}
    d[start] = 0
    
    for _ in range(len(lists) - 1):
        for node1 in range(len(lists)):
            for node2, weight in lists[node1]:
                if d[node2] > d[node1] + weight:
                    d[node2] = d[node1] + weight
    return d


def johnson(lists):
    n = len(lists)
    lists.append([])  # Добавляем новую вершину s

    # Соединяем новую вершину с каждой из существующих с весом 0
    for i in range(n):
        lists[i].append((n, 0))  # Ребра от вершины i к s 
    lists[n] = [(i, 0) for i in range(n)]  # Ребра от s ко всем 

    # Запускаем алгоритм Беллмана-Форда для поиска потенциалов
    f = bellman_ford(lists, n)

    # Пересчитываем веса рёбер
    new_lists = [[] for _ in range(n)]
    for u in range(n):
        for v, weight in lists[u]:
            if v < n:  
                new_weight = weight + f[u] - f[v] 
                new_lists[u].append((v, new_weight))
    def dijkstra(start, new_lists):
        d = [float('inf')] * n
        d[start] = 0
        used = [False] * n

        while True:
            u = -1
            for i in range(n):
                if not used[i] and (u == -1 or d[i] < d[u]):
                    u = i
            if u == -1:
                break
            used[u] = True  
            for v, w in new_lists[u]:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
        return d
    #дейкстру от каждой вершины
    answer_distances = []
    for u in range(n):
        dist = dijkstra(u, new_lists)
        for v in range(n):
            dist[v] = dist[v] - f[u] + f[v]  
        answer_distances.append(dist)


    return answer_distances

n, m = map(int, input().split())
lists = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    lists[u].append((v, w))
distances = johnson(lists)
for d in distances:
    print(*d)