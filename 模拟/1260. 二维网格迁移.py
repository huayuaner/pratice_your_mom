# 给你一个 m 行 n 列的二维网格 grid 和一个整数 k。你需要将 grid 迁移 k 次。
#
# 每次「迁移」操作将会引发下述活动：
#
# 位于 grid[i][j] 的元素将会移动到 grid[i][j + 1]。
# 位于 grid[i][n - 1] 的元素将会移动到 grid[i + 1][0]。
# 位于 grid[m - 1][n - 1] 的元素将会移动到 grid[0][0]。
# 请你返回 k 次迁移操作后最终得到的 二维网格。
#
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        # ans = [[None for _ in range(n)] for _ in range(m)]

        ans = [[None for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                target_i = (i + (j + k) // n) % m
                target_j = (j + k) % n
                # print(target_i, target_j, grid[i][j])
                ans[target_i][target_j] = grid[i][j]

        return ans