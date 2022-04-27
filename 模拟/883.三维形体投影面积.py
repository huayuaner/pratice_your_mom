# 在 n x n 的网格 grid 中，我们放置了一些与 x，y，z 三轴对齐的 1 x 1 x 1 立方体。
#
# 每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。
#
# 现在，我们查看这些立方体在 xy 、yz 和 zx 平面上的投影。
#
# 投影 就像影子，将 三维 形体映射到一个 二维 平面上。从顶部、前面和侧面看立方体时，我们会看到“影子”。
#
# 返回 所有三个投影的总面积 。

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        # top = 0
        # x = 0
        # y = []
        # n = len(grid)
        # for i in range(n):
        #     top += sum([grid[i][j]!=0 for j in range(n)])
        #     x += max(grid[i])
        #     if i == 0:
        #         y = grid[i]
        #     else:
        #         y = [max(y[j], grid[i][j]) for j in range(n)]
        # return x+top+sum(y)
        xyArea = sum(v > 0 for row in grid for v in row)
        yzArea = sum(map(max, zip(*grid)))  # 注意这里为 O(n) 空间复杂度，改为下标枚举则可以 O(1)
        zxArea = sum(map(max, grid))
        return xyArea + yzArea + zxArea