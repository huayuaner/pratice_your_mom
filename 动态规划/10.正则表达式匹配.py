# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
#  
# 示例 1：
#
# 输入：s = "aa", p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
# 示例 2:
#
# 输入：s = "aa", p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 示例 3：
#
# 输入：s = "ab", p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # # 动态规划
        # m, n = len(s), len(p)
        # # dp[i][j]代表字符串s的前i和字符串p的前j个能否匹配上
        # dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        # dp[0][0] = True
        # # 预处理，当*换成0个字符时是否是空串
        # for i in range(n):
        #     if p[i] == '*' and dp[0][i-1]:
        #         dp[0][i+1]=True
        
        # for i in range(m):
        #     for j in range(n):
        #         if s[i] == p[j] or p[j]=='.':
        #             dp[i+1][j+1] = dp[i][j]
        #         elif p[j] == '*':
        #             # *将前一个消除了
        #             if s[i] != p[j-1] and p[j-1]!='.':
        #                 if j>0:
        #                     dp[i+1][j+1] = dp[i+1][j-1]
        #             # *前一个字母相同
        #             else:
                        
        #                 dp[i+1][j+1] = dp[i+1][j+1] or dp[i][j+1] #变成多个
        #                 dp[i+1][j+1] = dp[i+1][j+1] or dp[i+1][j] #变成一个
        #                 if j>0:
        #                     dp[i+1][j+1] = dp[i+1][j+1] or dp[i+1][j-1] #变成0个
        # #print(dp)
        # return dp[m][n]
        @functools.lru_cache(None)
        def dfs(i, j):
            print(i,j)
            # if (i,j) in memo:
            #     return memo[(i,j)]
            if i<0 or j<0:
                return False
            if i == 0 and j==0:
                return True
            if j == 0 and i!=0:
                return False
            if i == 0 and p[j-1]=='*' and dfs(0,j-2):
                return True
            
            
            if s[i-1] == p[j-1] or p[j-1] == '.':
                return dfs(i-1,j-1)
            elif p[j-1] == "*":
                if s[i-1] != p[j-2] and p[j-2]!='.':
                    return dfs(i,j-2)
                else:
                    return dfs(i-1,j) or dfs(i,j-1) or dfs(i,j-2)
            return False
        return dfs(len(s),len(p))