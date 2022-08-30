用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。

网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。

给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。 
# class UF:
#     def __init__(self, N):
#         self.fa = list(range(N))
#         # 记录集合数量
#         self.cnt = N
#     def find(self, x):
#         if self.fa[x] != x:
#             self.fa[x] = self.find(self.fa[x])
#         return self.fa[x]
#     def merge(self, x, y):
#         fa_x,fa_y = self.find(x),self.find(y)
#         if fa_x == fa_y:
#             return
#         self.fa[fa_x] = fa_y
#         # 合并时集合数量-1
#         self.cnt -= 1
#         return
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # 思路错了，我本想着未联通的电脑都是独立的，没想到未联通的电脑可以是联通的，像是一个个孤岛
        # 所以这题并不是bfs，而是并查集，需要修改的操作数是集合数-1
        # length = len(connections)
        # if length < n-1:
        #     return -1
        # uf = UF(n)
        # for a,b in connections:
        #     uf.merge(a,b)
        # # print(uf.fa)
        # for i in range(n):
        #     uf.find(i)
        # return uf.cnt - 1

        # dfs找连通集
        if len(connections)<n-1:
            return -1
        graph = [[] for _ in range(n)]
        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)

        vis = [False]*n
        def dfs(i):
            for nex in graph[i]:
                if vis[nex] == False:
                    vis[nex] = True
                    dfs(nex)
        ans = 0
        for i in range(n):
            if vis[i] == False:
                ans += 1
                dfs(i)
        return ans - 1
