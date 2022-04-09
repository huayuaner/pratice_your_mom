# 给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
#
# 字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
#
# 题目数据保证答案符合 32 位带符号整数范围。

# 示例 1：
#
# 输入：s = "rabbbit", t = "rabbit"
# 输出：3
# 解释：
# 如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
# rabbbit
# rabbbit
# rabbbit
# 示例 2：
#
# 输入：s = "babgbag", t = "bag"
# 输出：5
# 解释：
# 如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dfs超时
        # ans = 0
        # n_t = len(t)
        # n_s = len(s)
        # def dfs(pos, l):
        #     if l == n_t:
        #         nonlocal ans
        #         ans += 1
        #         return

        #     for i in range(pos, n_s):

        #         if s[i] == t[l]:
        #             dfs(i+1, l+1)
        # dfs(0,0)
        # return ans

        # 动态规划
        m, n = len(s), len(t)
        if m < n:
            return 0
        # dp[i][j]表示s[i:],t[j:]对应的个数
        # dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # # 当j=n时t为空字符，空字符
        # for i in range(m+1):
        #     dp[i][n] = 1
        # for i in range(m-1, - 1, -1):
        #     for j in range(n-1, -1, -1):
        #         if s[i]==t[j]:
        #             # 当对应位置相同的时候，有两种情况，一个是包含当前值s[i]的情况，这时候的数量与dp[i+1][j+1]的情况一样
        #             # 还有一种情况是不包含s[i]值，这时候的数量和dp[i+1][j]一样
        #             dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
        #         else:
        #             # 当对应位置不相同的时候，一定不包含s[i]，所以是dp[i+1][j]
        #             dp[i][j] = dp[i+1][j]
        # return dp[0][0]

        # 滚动数组
        dp = [0 for _ in range(n + 1)]
        dp[-1] = 1
        for i in range(m - 1, -1, -1):
            pre = dp[-1]
            for j in range(n - 1, -1, -1):
                tmp = dp[j]
                if s[i] == t[j]:
                    # print(pre)
                    dp[j] = pre + dp[j]
                pre = tmp

            # print(dp,i)
        return dp[0]
