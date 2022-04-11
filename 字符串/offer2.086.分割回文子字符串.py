# 给定一个字符串 s ，请将 s 分割成一些子串，使每个子串都是 回文串 ，返回 s 所有可能的分割方案。
#
# 回文串 是正着读和反着读都一样的字符串。
#
#  
#
# 示例 1：
#
# 输入：s = "google"
# 输出：[["g","o","o","g","l","e"],["g","oo","g","l","e"],["goog","l","e"]]
# 示例 2：
#
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
# 示例 3：
#
# 输入：s = "a"
# 输出：[["a"]]

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # n = len(s)
        # ans = []
        # def check(s):
        #     return True if s == s[::-1] else False

        # def dfs(pos, lis):
        #     if pos == n:
        #         nonlocal ans
        #         ans.append(lis[:])
        #         return
        #     for i in range(pos, n):
        #         if check(s[pos:i+1]):
        #             lis.append(s[pos:i+1])
        #             dfs(i+1, lis)
        #             lis.pop()
        # dfs(0, [])
        # return ans

        # 动态规划+dfs
        n = len(s)
        # dp[i][j]表示字符串i:j+1为回文
        dp = [[True for _ in range(n)] for _ in range(n)]
        for j in range(n):
            for i in range(j):
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
        tmp = []
        ans = []

        def dfs(pos):
            if pos == n:
                ans.append(tmp[:])
            for i in range(pos, n):
                if dp[pos][i]:
                    tmp.append(s[pos:i + 1])
                    dfs(i + 1)
                    tmp.pop()

        dfs(0)
        return ans
