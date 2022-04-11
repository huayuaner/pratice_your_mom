# 给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
#
# 两个相邻元素间的距离为 1 。

from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # def bfs(i,j):
        #     pq = deque()
        #     vis = set()
        #     pq.append((i,j))
        #     vis.add((i,j))
        #     while pq:
        #         x, y = pq.popleft()
        #         # print(x,y)
        #         if mat[x][y] == 0:
        #             return abs(x-i)+abs(y-j)
        #         for nx,ny in [(x-1,y), (x+1, y), (x, y-1), (x, y+1)]:
        #             if 0<=nx<m and 0<=ny<n and (nx,ny) not in vis:
        #                 vis.add((nx,ny))
        #                 pq.append((nx,ny))
        #     return -1
        # m, n = len(mat), len(mat[0])
        # ans = []
        # for i in range(m):
        #     row = []
        #     for j in range(n):
        #         if mat[i][j] == 0:
        #             row.append(0)
        #         else:
        #             row.append(bfs(i,j))
        #     ans.append(row)
        # return ans

        # 多源广度优先
        # m, n = len(mat), len(mat[0])
        # ans = [[0 for _ in range(n)]for _ in range(m)]
        # zeros_pos = [(i,j) for i in range(m) for j in range(n) if mat[i][j]==0]
        # pq = deque(zeros_pos)
        # vis = set(zeros_pos)
        # while pq:
        #     x, y = pq.popleft()
        #     for nx,ny in [(x-1,y), (x+1, y), (x, y-1), (x, y+1)]:
        #         if 0<=nx<m and 0<=ny<n and (nx,ny) not in vis:
        #                 vis.add((nx,ny))
        #                 pq.append((nx,ny))
        #                 ans[nx][ny] = ans[x][y] + 1
        # return ans

        # 动态规划
        INF = 10 ** 9
        m, n = len(mat), len(mat[0])
        dist = [[INF for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
        # 左上
        # 其最短距离是下面和右边的+1 和 原本的值比
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        print(dist)
        for i in range(m):
            for j in range(n):
                if i - 1 > -1:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j - 1 > -1:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        return dist



