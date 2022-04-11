# 给你一个整数 n ，统计并返回各位数字都不同的数字 x 的个数，其中 0 <= x < 10n 。
#  
#
# 示例 1：
#
# 输入：n = 2
# 输出：91
# 解释：答案应为除去 11、22、33、44、55、66、77、88、99 外，在 0 ≤ x < 100 范围内的所有数字。
# 示例 2：
#
# 输入：n = 0
# 输出：1

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # if n == 0:
        #     return 1
        # ans = 0
        # while n:
        #     tmp = 1
        #     if n >= 2:
        #         for i in range(n, 0, -1):
        #             if i == n or i==n-1:
        #                 tmp*=9
        #             else:
        #                 tmp*=(10-(n-i))
        #     else:
        #         tmp*=10

        #     ans += tmp
        #     n -= 1

        # return ans
        # 动态规划
        if n == 0:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 10
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + (dp[i - 1] - dp[i - 2]) * (10 - (i - 1))
        return dp[-1]