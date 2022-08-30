# 偶数 个人站成一个圆，总人数为 num_people 。每个人与除自己外的一个人握手，所以总共会有 num_people / 2 次握手。
#
# 将握手的人之间连线，请你返回连线不会相交的握手方案数。
#
# 由于结果可能会很大，请你返回答案 模 10^9+7 后的结果。
#
mod = 10**(9)+7
class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        # dp[i]表示i对人的情况
        hand = numPeople//2
        dp = [0]*(hand+1)
        dp[0]=1
        dp[1] = 1
        for i in range(2, hand+1):
            for j in range(i):
                dp[i] +=  dp[j]*dp[i-j-1]
                dp[i] %= mod
        # print(dp)
        return dp[-1]

