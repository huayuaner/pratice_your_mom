# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
#
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
#
# 你可以认为每种硬币的数量是无限的。
#
#  
#
# 示例 1：
#
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
# 示例 2：
#
# 输入：coins = [2], amount = 3
# 输出：-1
# 示例 3：
#
# 输入：coins = [1], amount = 0
# 输出：0
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # dp[i][j]表示 前i个 组合成j的最少硬币个数
        # dp = [[float('inf') for _ in range(amount+1)]for _ in range(n+1)]
        # dp[0][0] = 0
        # for i in range(1,n+1):
        #     for j in range(amount+1):
        #         dp[i][j] = dp[i-1][j]
        #         if j>=coins[i-1]:
        #             dp[i][j] = min(dp[i][j], dp[i][j-coins[i-1]]+1)
        # # print(dp)
        # return dp[-1][-1] if dp[-1][-1] != float('inf') else -1

        # 滚动数组
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(n):
            for j in range(coins[i],amount+1):
                dp[j] = min(dp[j], dp[j-coins[i]]+1)
            # print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1