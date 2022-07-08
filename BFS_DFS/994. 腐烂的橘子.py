# 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
#
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
#
# 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        #bfs
        # 记录新鲜橘子的数量
        fresh_cnt = bad_cnt = 0
        pq = deque()
        # 记录好橘子和坏橘子数量
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_cnt += 1
                elif grid[i][j] == 2:
                    pq.append((i,j,0))
        if fresh_cnt == 0:
            return 0
        # print(pq)
        while pq:
            i,j,time = pq.popleft()
            for ni,nj in (i+1,j),(i-1,j),(i,j-1),(i,j+1):
                if 0<=ni<m and 0<=nj<n and grid[ni][nj] == 1:
                    fresh_cnt -= 1
                    if fresh_cnt == 0:
                        return time+1
                    grid[ni][nj] = 2
                    pq.append((ni,nj,time+1))
            # print(pq)
        return -1
