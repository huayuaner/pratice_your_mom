# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # stack = [-1]
        # ans = 0
        # for i,c in enumerate(s):
        #     if c == '(':
        #         stack.append(i)
        #     else:
        #         stack.pop()
        #         if stack:
        #             length = i - stack[-1]
        #             ans = max(ans,length)
        #         else:
        #             stack.append(i)
        # return ans

        # 动态规划
        # if not s:
        #     return 0
        # n = len(s)
        # dp = [0]*n
        # for i in range(1,n):
        #     if s[i] == ')':
        #         if s[i-1] == '(':
        #             dp[i] = (dp[i-2] + 2 if i>1 else 2)
        #         elif s[i]==")" and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=="(":
        #             dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
        #     # print(dp)
        # return max(dp)


        # 空间 1
        def helper(reverse, s):
            left = right = 0
            ans = 0
            s = s[::-1] if reverse else s
            for c in s:
                if c == '(':
                    left += 1
                else:
                    right += 1
                if left == right:
                    ans = max(ans, right * 2)
                elif (left > right and reverse == True) or (left < right and reverse == False):
                    left = right = 0
            return ans
        return max(helper(True, s), helper(False,s))
