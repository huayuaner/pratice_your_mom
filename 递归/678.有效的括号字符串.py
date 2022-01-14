给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：
#
# 任何左括号 ( 必须有相应的右括号 )。
# 任何右括号 ) 必须有相应的左括号 ( 。
# 左括号 ( 必须在对应的右括号之前 )。
# * 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
# 一个空字符串也被视为有效字符串。
# 示例 1:
#
# 输入: "()"
# 输出: True
# 示例 2:
#
# 输入: "(*)"
# 输出: True
# 示例 3:
#
# 输入: "(*))"
# 输出: True

class Solution:
    def checkValidString(self, s: str) -> bool:
        #栈方法
        ##计入左括号和星号的位置
        # left, xing = [], []
        # for i in range(len(s)):
        #     if s[i] == "(":
        #         left.append(i)
        #     elif s[i] == "*":
        #         xing.append(i)
            ##遇到右括号，优先用左括号处理，如栈空，用星号处理
        #     elif s[i] == ")":
        #         if left:
        #             left.pop()
        #         elif xing:
        #             xing.pop()
        #         else:
        #             return False
        ##遍历完成星栈和左栈可能不为空，pop：当星号在括号左边，成立，反之返回False
        # while left and xing:
        #     if xing[-1] > left[-1]:
        #         xing.pop()
        #         left.pop()
        #     # 不加这else会一致不pop导致无限循环
        #     else:
        #         return False
        # return not left

        #计数法
        ## l记录左括号最小可能数，r为左括号最大可能数
        # l,r = 0, 0
        # for c in s:
                ##遇到左括号，都+1
        #     if c == "(":
        #         l += 1
        #         r += 1
                ##遇到右括号，都-1
        #     elif c == ")":
        #         l -= 1
        #         r -= 1
        #         l = max(0, l)
        #     elif c == "*":
                ##遇到*号，有可能+1有可能-1有可能不变，所以最小-1最大+1
        #         l -= 1
        #         r += 1
                ## 最小不能为负数
        #         l = max(0, l)
                ## 最大数小于最小值，说明右括号过多，返回False
        #     if l > r:
        #         return False
        # return l == 0

        # 动态规划
        n = len(s)
        # dp[i][j]表示1-i的字符可以处理j个右括号
        dp = [[False] * (n + 1) for i in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            c = s[i - 1]
            for j in range(0, i + 1):
                if c == "(":
                    # 左括号说明之前的子串能处理j-1右括号，因为左括号能处理一个右括号
                    if j - 1 >= 0: dp[i][j] = dp[i - 1][j - 1]
                elif c == ")":
                    # 右括号会抵消一个左括号，所以要求i-1能处理j+1
                    if j + 1 <= i: dp[i][j] = dp[i - 1][j + 1]
                elif c == "*":
                    # 星号，只要三种情况有一种成立即可
                    dp[i][j] = dp[i - 1][j]
                    if j - 1 >= 0: dp[i][j] = dp[i][j] or dp[i - 1][j - 1]
                    if j + 1 <= i: dp[i][j] = dp[i][j] or dp[i - 1][j + 1]
        return dp[n][0]







