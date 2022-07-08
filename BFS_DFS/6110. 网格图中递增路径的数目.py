# 给你一个 m x n 的整数网格图 grid ，你可以从一个格子移动到 4 个方向相邻的任意一个格子。
#
# 请你返回在网格图中从 任意 格子出发，达到 任意 格子，且路径中的数字是 严格递增 的路径数目。由于答案可能会很大，请将结果对 109 + 7 取余 后返回。
#
# 如果两条路径中访问过的格子不是完全相同的，那么它们视为两条不同的路径。

MOD = 10 ** 9 + 7


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # 返回从i,j出发的方案总数
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i: int, j: int) -> int:
            res = 1
            for ni, nj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > grid[i][j]:
                    res += dfs(ni, nj) % MOD
            return res

        ans = 0
        for i in range(m):
            for j in range(n):
                ans += dfs(i, j) % MOD
        return ans % MOD

