class Node:
    def __init__(self):
        self.childrens = {}  #ключи - буквы, значения - вершины
        self.flag = False
class Bor:
    def __init__(self):
        self.root = Node()
    def add(self, word):
        cur = self.root
        for s in word:
            if s in cur.childrens:
                cur = cur.childrens[s]
            else:
                new_cur = Node()
                cur.childrens[s] = new_cur
                cur = new_cur
        cur.flag = True
    def search(self, word):
        cur = self.root
        for s in  word:
            if s not in cur.childrens:
                return False
            cur = cur.childrens[s]
        return cur.flag
    def delete(self, word):
        cur = self.root
        parents = []
        for s in  word:
            if s not in cur.childrens:
                print("This word not in Bor")
                return
            parents.append((cur, s))
            cur = cur.childrens[s]
        if not cur.flag:
            print("This word not in Bor")
            return
        cur.flag = False #этот узел больше не конец слова, если у этого узла еще есть дети, то просто снимаем метку что это конец бора, если нет детей, то:
        if len(cur.childrens) == 0:
            for i in range(len(parents)-1, -1, -1):
                v, s = parents[i]
                if len(v.childrens[s].childrens) == 0 and not v.childrens[s].flag:
                    v.childrens.pop(s)
                else:
                    break
words = input().split()
bor = Bor()
for i in words:
    bor.add(i)
# bor.delete('Hello')
print(bor.search(words[0]))
    


   

