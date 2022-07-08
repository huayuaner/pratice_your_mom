# 给你一个整数 n 。你需要掷一个 6 面的骰子 n 次。请你在满足以下要求的前提下，求出 不同 骰子序列的数目：
#
# 序列中任意 相邻 数字的 最大公约数 为 1 。
# 序列中 相等 的值之间，至少有 2 个其他值的数字。正式地，如果第 i 次掷骰子的值 等于 第 j 次的值，那么 abs(i - j) > 2 。
# 请你返回不同序列的 总数目 。由于答案可能很大，请你将答案对 109 + 7 取余 后返回。
#
# 如果两个序列中至少有一个元素不同，那么它们被视为不同的序列。
#
# 动态规划
MOD, MX = 10**9+7, 10**4
dp = [[[0]*6 for _ in range(6)]for _ in range(MX+1)]
dp[2] = [[int(i!=j and math.gcd(i+1, j+1)==1) for j in range(6)] for i in range(6)]
for i in range(2, MX):
    for j in range(6):
        for last in range(6):
            if last != j and math.gcd(last+1,j+1) == 1:
                dp[i+1][j][last] = sum(dp[i][last][last2] for last2 in range(6) if last2!=j)%MOD


class Solution:
    def distinctSequences(self, n: int) -> int:
        return sum(sum(row) for row in dp[n]) % MOD if n > 1 else 6