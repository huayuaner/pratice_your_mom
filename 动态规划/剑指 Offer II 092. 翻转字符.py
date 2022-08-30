# 如果一个由 '0' 和 '1' 组成的字符串，是以一些 '0'（可能没有 '0'）后面跟着一些 '1'（也可能没有 '1'）的形式组成的，那么该字符串是 单调递增 的。
#
# 我们给出一个由字符 '0' 和 '1' 组成的字符串 s，我们可以将任何 '0' 翻转为 '1' 或者将 '1' 翻转为 '0'。
#
# 返回使 s 单调递增 的最小翻转次数。
#
#  
#
# 示例 1：
#
# 输入：s = "00110"
# 输出：1
# 解释：我们翻转最后一位得到 00111.
# 示例 2：
#
# 输入：s = "010110"
# 输出：2
# 解释：我们翻转得到 011111，或者是 000111。
# 示例 3：
#
# 输入：s = "00011000"
# 输出：2
# 解释：我们翻转得到 00000000。

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        # dp[i][j]表示当第i为是j的情况需要反转的最小个数
        # dp = [[0 for _ in range(2)] for _ in range(n)]
        # if s[0] == '0':
        #     dp[0][0],dp[0][1] = 0,1
        # else:
        #     dp[0][0],dp[0][1] = 1,0
        # for i in range(1, n):
        #     dp[i][0] = dp[i-1][0] + int(s[i]=='1')
        #     dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + int(s[i]=='0')

        # return min(dp[-1])

        # 滚动数组优化
        dp0 = dp1 = 0
        for c in s:
            dp0New,dp1New = dp0, min(dp0, dp1)
            if c == '0':
                dp1New += 1
            else:
                dp0New += 1
            dp0,dp1 = dp0New, dp1New
        return min(dp0, dp1)