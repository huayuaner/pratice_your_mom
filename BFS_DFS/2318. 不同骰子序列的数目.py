# 给你一个整数 n 。你需要掷一个 6 面的骰子 n 次。请你在满足以下要求的前提下，求出 不同 骰子序列的数目：
#
# 序列中任意 相邻 数字的 最大公约数 为 1 。
# 序列中 相等 的值之间，至少有 2 个其他值的数字。正式地，如果第 i 次掷骰子的值 等于 第 j 次的值，那么 abs(i - j) > 2 。
# 请你返回不同序列的 总数目 。由于答案可能很大，请你将答案对 109 + 7 取余 后返回。
#
# 如果两个序列中至少有一个元素不同，那么它们被视为不同的序列。
#
import functools
import math
MOD = 10 ** 9 + 7
@functools.lru_cache()
def dfs(n, last1, last2):
        # 合法结果
    if n == 0:
        return 1
    res = 0
    for i in range(1,7):
        if i != last1 and i!=last2 and math.gcd(i, last1) == 1:
            res +=  dfs(n-1, i, last1)
    return res%MOD

class Solution:
    def distinctSequences(self, n: int) -> int:
        # dfs

        return dfs(n, 7, 7)