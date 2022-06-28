# 如果一个二进制字符串，是以一些 0（可能没有 0）后面跟着一些 1（也可能没有 1）的形式组成的，那么该字符串是 单调递增 的。
#
# 给你一个二进制字符串 s，你可以将任何 0 翻转为 1 或者将 1 翻转为 0 。
#
# 返回使 s 单调递增的最小翻转次数。
#
#  
#
# 示例 1：
#
# 输入：s = "00110"
# 输出：1
# 解释：翻转最后一位得到 00111.
# 示例 2：
#
# 输入：s = "010110"
# 输出：2
# 解释：翻转得到 011111，或者是 000111。
# 示例 3：
#
# 输入：s = "00011000"
# 输出：2
# 解释：翻转得到 00000000。

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        # n = len(s)
        # # dp[i][0]表示下标i 为 0 最小反转次数
        # # dp[i][1]表示下标i 为 1 的最小反转次数
        # dp = [[0 for _ in range(2)] for _ in range(n)]
        # if s[0] == '1':
        #     dp[0][0] = 1
        # else:
        #     dp[0][1] = 1
        # for i in range(1,n):
        #     # 当前位置为 0 的话，前面的数一定要为0
        #     dp[i][0] = dp[i-1][0] + int(s[i] == '1')
        #     # 当前位置为1 前面的数可以为 0 也可以为 1
        #     dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + int(s[i] == '0')
        # return min(dp[-1][0],dp[-1][1])

        # 动态规划 + 滚动数组
        # n = len(s)
        # if s[0] == '1':
        #     idx_0 = 1
        #     idx_1 = 0
        # else:
        #     idx_0 = 0
        #     idx_1 = 1
        # for i in range(1,n):
        #     idx_1 = min(idx_1, idx_0) + int(s[i]=='0')
        #     idx_0 = idx_0 + int(s[i] == '1')
        # return min(idx_0, idx_1)

        # 前缀和
        preSum = [0]
        n = len(s)
        for c in s:
            val = preSum[-1]
            if c == '1':
                val += 1
            preSum.append(val)
        # print(preSum)
        # print([preSum[i] + n-i - (preSum[-1]-preSum[i]) for i in range(len(s)+1)])
        return min([preSum[i] + n - i - (preSum[-1] - preSum[i]) for i in range(n + 1)])

















