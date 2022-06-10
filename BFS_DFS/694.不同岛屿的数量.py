# 给定一个非空 01 二维数组表示的网格，一个岛屿由四连通（上、下、左、右四个方向）的 1 组成，你可以认为网格的四周被海水包围。
#
# 请你计算这个网格中共有多少个形状不同的岛屿。两个岛屿被认为是相同的，当且仅当一个岛屿可以通过平移变换（不可以旋转、翻转）和另一个岛屿重合。
#
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # dfs + 路径聚合
        m, n = len(grid), len(grid[0])

        def dfs(i, j, roads, dirs):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return
            grid[i][j] = 0
            roads.append(dirs)
            dfs(i - 1, j, roads, '1')
            dfs(i + 1, j, roads, '2')
            dfs(i, j + 1, roads, '3')
            dfs(i, j - 1, roads, '4')
            roads.append('-' + dirs)

        island = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    roads = []
                    dfs(i, j, roads, '0')
                    # print(roads)
                    island.add(''.join(roads))
        return len(island)
