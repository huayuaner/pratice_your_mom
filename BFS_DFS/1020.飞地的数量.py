# 给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。
#
# 一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。
#
# 返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。
#
# 输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：3
# 解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # # BFS
        # ans = 0
        # n,m = len(grid), len(grid[0])
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j] == 1:
        #             tmp = 1
        #             flag = True
        #             pq = [(i,j)]
        #             grid[i][j] = 0
        #             while pq:
        #                 x, y = pq.pop(0)
        #                 for nx, ny in [(x-1,y), (x+1, y), (x, y-1), (x, y+1)]:
        #                     if 0<=nx<n and 0<=ny<m and grid[nx][ny] == 1:
        #                         pq.append((nx,ny))
        #                         grid[nx][ny] = 0
        #                         tmp += 1
        #                 if x == n-1 or x == 0 or y == m-1 or y == 0:
        #                     flag = False
        #             ans = ans+tmp if flag else ans
        # #print(grid)
        # return ans 

        # dfs
        n, m = len(grid), len(grid[0])
        def dfs(x,y):
            if x<0 or x>=n or y<0 or y>=m or grid[x][y] == 0:
                return
            grid[x][y] = 0
            for nx, ny in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                dfs(nx,ny)
        # 将四周的陆地都遍历  
        for i in range(n):
            dfs(i,0)
            dfs(i,m-1)
        for j in range(m):
            dfs(0, j)
            dfs(n-1, j)
        return sum(grid[i][j] for i in range(1,n-1) for j in range(1,m-1))


