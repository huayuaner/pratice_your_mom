# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp[i][j]存以(i,j)右下角可以形成的正方形的最大边长
        # dp 转移是 当dp[i][j] == 1： 左 左上 上 三个位置最小+1
        m, n = len(matrix), len(matrix[0])
        # 初始化
        dp = [[0 for _ in range(n)] for _ in range(m)]
        max_sq = 0
        for i in range(m):

            # dp[i][0] = (1 if matrix[i][0] == '1' else 0)
            if matrix[i][0] == '1':
                dp[i][0] = 1
                max_sq = 1

            # print(matrix[i][0], dp[i][0])
        for j in range(n):
            # dp[0][j] = (1 if matrix[0][j] == '1' else 0)
            if matrix[0][j] == '1':
                dp[0][j] = 1
                max_sq = 1

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    # print(dp)
                    if dp[i][j] > max_sq:
                        max_sq = dp[i][j]

        return max_sq * max_sq