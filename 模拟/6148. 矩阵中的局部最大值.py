# 给你一个大小为 n x n 的整数矩阵 grid 。
#
# 生成一个大小为 (n - 2) x (n - 2) 的整数矩阵  maxLocal ，并满足：
#
# maxLocal[i][j] 等于 grid 中以 i + 1 行和 j + 1 列为中心的 3 x 3 矩阵中的 最大值 。
# 换句话说，我们希望找出 grid 中每个 3 x 3 矩阵中的最大值。
#
# 返回生成的矩阵。
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(n-2):
            for j in range(n-2):
                grid[i][j] = max(max(row[j:j+3]) for row in grid[i:i+3])
            grid[i].pop()
            grid[i].pop()
        grid.pop()
        grid.pop()
        return grid