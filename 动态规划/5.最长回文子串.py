# 给你一个字符串 s，找到 s 中最长的回文子串。
#
#  
#
# 示例 1：
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 示例 2：
#
# 输入：s = "cbbd"
# 输出："bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if len(s)<2:
        #     return s
        # n = len(s)
        # # dp[i][j]代表s[i:j]是回文
        # dp = [[False for _ in range(n)] for _ in range(n)]
        # # 单个字符都是回文
        # for i in range(n):
        #     dp[i][i] = True
        # begin = 0
        # maxlen = 1
        # # 以对角线的形式遍历
        # for gap in range(1,n):
        #     for i in range(n):
        #         j = i+gap
        #         if j>=n:
        #             break
        #         if s[i] == s[j]:
        #             if j-i<3:
        #                 dp[i][j] = True
        #             else:
        #                 dp[i][j] = dp[i+1][j-1]
        #         if dp[i][j] and j-i+1>maxlen:
        #             begin = i
        #             maxlen = j-i+1
        # # print(begin,maxlen)
        # return s[begin:begin+maxlen]

        # 中心扩散法
        n = len(s)
        def expandAroundCenter(left,right):
            while left>=0 and right<n and s[left] == s[right]:
                left -= 1
                right += 1
            return left+1,right-1
        begin = 0
        end = 0
        for i in range(n):
            left1, right1 = expandAroundCenter(i,i)
            left2, right2 = expandAroundCenter(i,i+1)
            # print(left1, right1)
            if right1-left1>end-begin:
    
                begin = left1
                end = right1
            if right2-left2>end-begin:
                begin = left2
                end = right2
            #print(begin, end)
        return s[begin:end+1] 
            
        



        




        
