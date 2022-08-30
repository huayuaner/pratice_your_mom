class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # if k == 0 or len(prices) < 2:
        #     return 0
        # n = len(prices)
        # dp = [[0 for _ in range(k*2)] for _ in range(n)]
        # dp[0][0] = -prices[0]
        # for j in range(1,k):
        #     dp[0][j*2] = float('-inf')
        # for i in range(1, n):
        #     dp[i][0] = max(dp[i-1][0], -prices[i])
        #     dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        #     for j in range(1, k):
        #         dp[i][2*j] = max(dp[i-1][2*j], dp[i-1][2*j-1]-prices[i])
        #         dp[i][2*j+1] = max(dp[i-1][2*j+1], dp[i-1][2*j]+prices[i])
        # # print(dp)
        # return max(dp[-1][2*j+1] for j in range(k))

        # 滚动数组
        if k == 0 or len(prices) < 2:
            return 0
        n = len(prices)
        dp = [0 for _ in range(k * 2)]
        dp[0] = -prices[0]
        for j in range(1, k):
            dp[j * 2] = float('-inf')
        for i in range(1, n):
            for j in range(k - 1, 0, -1):
                dp[2 * j + 1] = max(dp[2 * j + 1], dp[2 * j] + prices[i])
                dp[2 * j] = max(dp[2 * j], dp[2 * j - 1] - prices[i])

            dp[1] = max(dp[1], dp[0] + prices[i])
            dp[0] = max(dp[0], -prices[i])

        # print(dp)
        return max(dp)