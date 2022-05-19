# 给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
#
# 请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
#
# 假设每一种面额的硬币有无限个。 
#
# 题目数据保证结果符合 32 位带符号整数。
#
#  
#
# 示例 1：
#
# 输入：amount = 5, coins = [1, 2, 5]
# 输出：4
# 解释：有四种方式可以凑成总金额：
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 示例 2：
#
# 输入：amount = 3, coins = [2]
# 输出：0
# 解释：只用面额 2 的硬币不能凑成总金额 3 。
# 示例 3：
#
# 输入：amount = 10, coins = [10]
# 输出：1
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i][j]表示前 i 个能凑成 j的方案数
        n = len(coins)
        # dp = [[0 for _ in range(amount+1)]for _ in range(n+1)]
        # for i in range(n+1):
        #     dp[i][0] = 1
        # for i in range(1,n+1):
        #     for j in range(amount+1):
        #         dp[i][j] = dp[i-1][j]
        #         if j>=coins[i-1]:
        #             dp[i][j] += dp[i][j-coins[i-1]]
        # # print(dp)
        # return dp[-1][-1]

        dp = [0]*(amount+1)
        dp[0] = 1
        for i in range(n):
            for j in range(coins[i], amount+1):
                dp[j] += dp[j-coins[i]]
        return dp[-1]