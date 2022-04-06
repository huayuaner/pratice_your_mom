# 给定三个字符串 s1、s2、s3，请判断 s3 能不能由 s1 和 s2 交织（交错） 组成。
#
# 两个字符串 s 和 t 交织 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：
#
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# 交织 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
# 提示：a + b 意味着字符串 a 和 b 连接。

# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出：true
# 示例 2：
#
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出：false
# 示例 3：
#
# 输入：s1 = "", s2 = "", s3 = ""
# 输出：true
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dfs
        # i,j 代表字符串s1, s2的下标，pos代表s3的下标

        # m, n = len(s1), len(s2)
        # if len(s3)!=m+n:
        #     return False
        # # 还是有重复的
        # @functools.lru_cache(None)
        # def dfs(i,j, pos):
        #     if i == m and j == n and pos == m+n:
        #         nonlocal ans
        #         ans = True
        #         return
        #     if i<m:
        #         if s3[pos] == s1[i]:
        #             dfs(i+1,j,pos+1)
        #     if j<n:
        #         if s3[pos] == s2[j]:
        #             dfs(i, j+1, pos+1)
        # ans = False
        # dfs(0,0,0)
        # return ans

        # 动规
        # dp[i][j]代表s1前i个和s2前j个能和s3前i+j个匹配上
        m, n = len(s1), len(s2)
        if len(s3) != m + n:
            return False
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        dp[0][0] = True

        # 预处理
        # 当s2为空时的匹配
        for i in range(1, m + 1):
            if s1[i - 1] == s3[i - 1]:
                # print(dp)
                dp[i][0] = dp[i - 1][0]
        # 当s1为空时的匹配
        for j in range(1, n + 1):
            if s2[j - 1] == s3[j - 1]:
                dp[0][j] = dp[0][j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # i=1,j=1 时 s3 是前两个 下标为 1+1-1
                if s1[i - 1] == s3[i + j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif s1[i - 1] == s3[i + j - 1] and s2[j - 1] != s3[i + j - 1]:
                    dp[i][j] = dp[i - 1][j]
                elif s1[i - 1] != s3[i + j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]



