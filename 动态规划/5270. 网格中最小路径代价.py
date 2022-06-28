# 给你一个下标从 0 开始的整数矩阵 grid ，矩阵大小为 m x n ，由从 0 到 m * n - 1 的不同整数组成。你可以在此矩阵中，从一个单元格移动到 下一行 的任何其他单元格。如果你位于单元格 (x, y) ，且满足 x < m - 1 ，你可以移动到 (x + 1, 0), (x + 1, 1), ..., (x + 1, n - 1) 中的任何一个单元格。注意： 在最后一行中的单元格不能触发移动。
#
# 每次可能的移动都需要付出对应的代价，代价用一个下标从 0 开始的二维数组 moveCost 表示，该数组大小为 (m * n) x n ，其中 moveCost[i][j] 是从值为 i 的单元格移动到下一行第 j 列单元格的代价。从 grid 最后一行的单元格移动的代价可以忽略。
#
# grid 一条路径的代价是：所有路径经过的单元格的 值之和 加上 所有移动的 代价之和 。从 第一行 任意单元格出发，返回到达 最后一行 任意单元格的最小路径代价。
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        # dp[i][j]表示到位置i,j的最小路径代价
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        # 初始化
        for j in range(n):
            dp[0][j] = grid[0][j]
        for i in range(1,m):
            for j in range(n):
                for k in range(n):
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + grid[i][j] + moveCost[grid[i-1][k]][j])
        return min(dp[-1])