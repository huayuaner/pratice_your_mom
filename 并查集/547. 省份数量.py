# 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
#
# 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
#
# 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
#
# 返回矩阵中 省份 的数量。
#
from collections import deque


class UF:
    def __init__(self, N) -> None:
        # 使用列表结构完成
        # 初始自己是自己的父亲
        self.father = list(range(N))

    def find(self, x):
        # 如果没有找到头，往下遍历
        # 顺带路径压缩
        if self.father[x] != x: self.father[x] = self.find(self.father[x])
        return self.father[x]

    def merge(self, x1, x2):
        if x1 == x2:
            return
        x1_f, x2_f = self.find(x1), self.find(x2)
        if x1_f != x2_f:
            self.father[x1_f] = x2_f


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UF(n)
        # print(uf.father)
        for i in range(n):
            for j in range(n):
                if i == j: continue
                # print(i,j)
                if isConnected[i][j] == 1:
                    uf.merge(i, j)
        # print(uf.father)

        return sum([int(uf.father[i] == i) for i in range(n)])

        # 类似岛屿
        # n = len(isConnected)
        # vis = [False] * n
        # # graph = [[]*n]
        # ans = 0
        # for i in range(n):
        #     if vis[i]:continue
        #     ans += 1
        #     pq = deque([i])
        #     while pq:
        #         city = pq.popleft()
        #         for nex in range(n):
        #             if city==nex:continue
        #             if isConnected[city][nex] == 1 and vis[nex]==False:
        #                 vis[nex] = True
        #                 pq.append(nex)
        #     # print(vis)
        # return ans

        # 并查集



