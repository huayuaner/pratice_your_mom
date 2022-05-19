# 有一些不规则的硬币。在这些硬币中，prob[i] 表示第 i 枚硬币正面朝上的概率。
#
# 请对每一枚硬币抛掷 一次，然后返回正面朝上的硬币数等于 target 的概率。
#
#  
#
# 示例 1：
#
# 输入：prob = [0.4], target = 1
# 输出：0.40000
# 示例 2：
#
# 输入：prob = [0.5,0.5,0.5,0.5,0.5], target = 0
# 输出：0.03125
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        # dp[i][j] 表示 前i个硬币正面朝上数量等于j的概率
        n = len(prob)
        # dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
        # # 初始化
        # dp[0][0] = 1

        # for i in range(1,n+1):
        #     for j in range(target+1):
        #         # 由于是求概率，所以是和而不是最大的那个
        #         # 当前置反面的情况
        #         dp[i][j] += dp[i-1][j]*(1-prob[i-1])
        #         # 当前置正面的情况
        #         if j > 0:
        #             dp[i][j] +=  dp[i-1][j-1]*prob[i-1]
        # # print(dp)
        # return dp[-1][-1] # if dp[-1][-1]!=1 else 0

        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(n):
            # lt = dp[0]
            for j in range(target, 0, -1):
                dp[j] = (dp[j] * (1 - prob[i]) + dp[j - 1] * prob[i])

            dp[0] *= (1 - prob[i])

        return dp[-1]