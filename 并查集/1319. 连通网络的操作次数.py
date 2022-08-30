class UF:
    def __init__(self, N):
        self.fa = list(range(N))
        # 记录集合数量
        self.cnt = N
    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]
    def merge(self, x, y):
        fa_x,fa_y = self.find(x),self.find(y)
        if fa_x == fa_y:
            return
        self.fa[fa_x] = fa_y
        # 合并时集合数量-1
        self.cnt -= 1
        return
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # 思路错了，我本想着未联通的电脑都是独立的，没想到未联通的电脑可以是联通的，像是一个个孤岛
        # 所以这题并不是bfs，而是并查集，需要修改的操作数是集合数-1
        length = len(connections)
        if length < n-1:
            return -1
        uf = UF(n)
        for a,b in connections:
            uf.merge(a,b)
        # print(uf.fa)
        for i in range(n):
            uf.find(i)
        return uf.cnt - 1