#если нет кратных то можна использовать сеты
n, m = map(int, input().split())
lists = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    lists[u].append(v)
    lists[v].append(u)
count = 0
for j in range(len(lists)):
    if len(lists[j])%2 != 0:
        count += 1
if count == 2:
   print('yes')