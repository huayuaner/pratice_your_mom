# 给你一个房屋数组houses 和一个整数 k ，其中 houses[i] 是第 i 栋房子在一条街上的位置，现需要在这条街上安排 k 个邮筒。
#
# 请你返回每栋房子与离它最近的邮筒之间的距离的 最小 总和。
#
# 答案保证在 32 位有符号整数范围以内。
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        medsum = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                medsum[i][j] = medsum[i + 1][j - 1] + houses[j] - houses[i]
        # dp = [[float('inf') for _ in range(k+1)] for _ in range(n+1)]
        #
        # for j in range(k+1):
        #     dp[0][j] = 0
        # for i in range(1,n+1):
        #     dp[i][1] = medsum[0][i-1]
        #     for j in range(2, min(k,i)+1):
        #         for left in range(1, i):
        #             dp[i][j] = min(dp[i][j], dp[left][j-1] + medsum[left][i-1])
        # return dp[-1][-1]

        # 滚动数组优化
        dp = [0] + medsum[0]
        for _ in range(k - 1):
            for i in range(n, 0, -1):
                for left in range(1, i):
                    # dp[left]是随着left增加变大的，medsum[left][i-1]随着left增加变小
                    dp[i] = min(dp[i], dp[left] + medsum[left][i - 1])
        return dp[-1]
