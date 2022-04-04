# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
#
# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
#
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
#
#  
#
# 示例 1：
#
# 输入：text1 = "abcde", text2 = "ace"
# 输出：3
# 解释：最长公共子序列是 "ace" ，它的长度为 3 。
# 示例 2：
#
# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc" ，它的长度为 3 。
# 示例 3：
#
# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0 。

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 动态规划
        # dp[i][j]代表text1,text2前i,j个的公共子序列长度
        # m, n = len(text1), len(text2)
        # dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        # # print(dp)
        # for i in range(m):
        #     for j in range(n):
        #         if text1[i] == text2[j]:
        #             dp[i+1][j+1] = dp[i][j] + 1
        #         else:
        #             dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        # # print(dp)
        # return dp[-1][-1]

        # 滚动数组
        m, n = len(text1), len(text2)
        dp = [0 for _ in range(n + 1)]
        for i in range(m):
            pre = 0
            for j in range(n):
                tmp = dp[j + 1]
                if text1[i] == text2[j]:
                    dp[j + 1] = pre + 1
                else:
                    dp[j + 1] = max(dp[j + 1], dp[j])
                pre = tmp
        return dp[-1]
