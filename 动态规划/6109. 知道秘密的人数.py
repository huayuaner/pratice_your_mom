# 在第 1 天，有一个人发现了一个秘密。
#
# 给你一个整数 delay ，表示每个人会在发现秘密后的 delay 天之后，每天 给一个新的人 分享 秘密。同时给你一个整数 forget ，表示每个人在发现秘密 forget 天之后会 忘记 这个秘密。一个人 不能 在忘记秘密那一天及之后的日子里分享秘密。
#
# 给你一个整数 n ，请你返回在第 n 天结束时，知道秘密的人数。由于答案可能会很大，请你将结果对 109 + 7 取余 后返回。

MOD = 10 ** 9 + 7


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # 动态规划
        # dp[i] 第i天新增知道的人数
        # 第i天新增的知道的人数是前面知道了没忘，到知道了能讲的人
        # dp[i] = sum(dp[i-forget+1 : i-delay+1])

        # 前缀和 优化
        # pre_sum[i] = 0 + ... + i
        pre_Sum = [0] * (n + 1)
        pre_Sum[1] = 1
        # 第一天知道1个人
        # dp[1] = 1
        for i in range(2, n + 1):
            # pre_Sum[max(0, i-delay)] - pre_Sum[max(0,i-forget)] 表示的是[i-forget+1:i-delay+1]的和
            # 为了保证前缀和的性质 需要 + pre_Sum[i-1]
            pre_Sum[i] += (pre_Sum[max(0, i - delay)] - pre_Sum[max(0, i - forget)] + pre_Sum[i - 1]) % MOD
        # print(pre_Sum)

        return (pre_Sum[-1] - pre_Sum[n - forget]) % MOD

