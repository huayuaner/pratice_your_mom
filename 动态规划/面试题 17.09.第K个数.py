# 有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，5，7，9，15，21。

class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        if k == 1:
            return 1
        dp = [0]*(k+1)
        dp[1] = 1
        p3, p5, p7 = 1, 1,1
        for i in range(2, k+1):
            num3, num5, num7 = dp[p3]*3, dp[p5]*5, dp[p7]*7
            dp[i] = min(num3, num5, num7)
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
            if dp[i] == num7:
                p7 += 1
        return dp[-1]
