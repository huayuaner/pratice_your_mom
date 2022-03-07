给你一个大小为 m x n 的二进制矩阵 grid 。

岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

岛屿的面积是岛上值为 1 的单元格的数目。

计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # BFS
        # n,m = len(grid),len(grid[0])
        # def bfs(x,y):
        #     pq = [(x,y)]
        #     ans = 1
        #     grid[x][y] = 0
        #     while pq:
        #         x,y = pq.pop(0)
        #         for nx,ny in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
        #             if 0<=nx<n and 0<=ny<m and grid[nx][ny] == 1:
        #                 pq.append((nx,ny))
        #                 ans += 1
        #                 grid[nx][ny] = 0
        #     return ans
        # ans = 0
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j] == 1:
        #             ans = max(bfs(i,j), ans)
        
        # return ans 

        # DFS
        n,m = len(grid),len(grid[0])
        def dfs(x,y):
            if x<0 or x>=n or y<0 or y>=m or grid[x][y]==0:
                return 0
            ans = 1
            grid[x][y] = 0
            for nx,ny in [(x+1,y),(x-1,y), (x,y-1), (x,y+1)]:
                ans += dfs(nx,ny)
            return ans
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = max(dfs(i,j), ans)
        return ans
