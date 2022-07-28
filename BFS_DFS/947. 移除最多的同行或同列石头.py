# n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。
#
# 如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。
#
# 给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子 的最大数量。
#
from collections import defaultdict


class UF:
    def __init__(self) -> None:
        self.father = dict()
        # 记录连通集的数量
        self.cnt = 0

    def find(self, x):
        # 如果x不在self.father里，说明是新的一个集合
        if x not in self.father:
            self.father[x] = x
            self.cnt += 1
        # 如果在
        elif self.father[x] != x:
            # 递归+路径压缩
            self.father[x] = self.find(self.father[x])
        return self.father[x]

    def merge(self, x1, x2):
        if x1 == x2:
            return
        x1_f, x2_f = self.find(x1), self.find(x2)
        if x1_f != x2_f:
            self.father[x1_f] = x2_f
            # 由于融合了，连通集数量-1
            self.cnt -= 1


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = UF()
        for x, y in stones:
            uf.merge(x, y + 10001)
        print(uf.father)
        return n - uf.cnt
        # dfs
        # n = len(stones)
        # graph = defaultdict(list)
        # for i,(x1,y1) in enumerate(stones):
        #     for j, (x2,y2) in enumerate(stones):
        #         if x1 == x2 or y1 == y2:
        #             graph[i].append(j)
        # def dfs(i):
        #     vis.add((i))
        #     for nex in graph[i]:
        #         if nex not in vis:
        #             dfs(nex)
        # vis = set()
        # num = 0
        # for i in range(n):
        #     if i not in vis:
        #         num += 1
        #         dfs(i)
        # return n-num

        # n = len(stones)
        # edge = collections.defaultdict(list)
        # rec = collections.defaultdict(list)
        # for i, (x, y) in enumerate(stones):
        #     rec[x].append(i)
        #     rec[y + 10001].append(i)
        # # print(rec)
        # for vec in rec.values():
        #     k = len(vec)
        #     for i in range(1, k):
        #         edge[vec[i - 1]].append(vec[i])
        #         edge[vec[i]].append(vec[i - 1])
        # def dfs(i):
        #     vis.add((i))
        #     for nex in edge[i]:
        #         if nex not in vis:
        #             dfs(nex)
        # vis = set()
        # num = 0
        # for i in range(n):
        #     if i not in vis:
        #         num += 1
        #         dfs(i)
        # return n-num
        # print(edge)









