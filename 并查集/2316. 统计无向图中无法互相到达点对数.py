# 给你一个整数 n ，表示一张 无向图 中有 n 个节点，编号为 0 到 n - 1 。同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条 无向 边。
#
# 请你返回 无法互相到达 的不同 点对数目 。
#
from collections import Counter


class UF:
    def __init__(self, N):
        self.father = list(range(N))

    def find(self, x):
        if self.father[x] != x: self.father[x] = self.find(self.father[x])
        return self.father[x]

    def merge(self, x1, x2):
        if x1 == x2:
            return
        x1_f = self.find(x1)
        x2_f = self.find(x2)
        if x2_f != x1_f:
            self.father[x1_f] = x2_f


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for a, b in edges:
            f1, f2 = uf.find(a), uf.find(b)
            if f1 != f2:
                uf.merge(a, b)
        # print(uf.father)
        cnts = Counter()
        for i in range(n):
            cnts[uf.find(i)] += 1
        l = list(cnts.values())
        add = l[-1]
        ans = 0
        for i in range(len(l) - 2, -1, -1):
            ans += add * l[i]
            add += l[i]
        return ans

        # print(uf.father)
