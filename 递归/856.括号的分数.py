# 给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：
#
# () 得 1 分。
# AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
# (A) 得 2 * A 分，其中 A 是平衡括号字符串。
#  
#
# 示例 1：
#
# 输入： "()"
# 输出： 1
# 示例 2：
#
# 输入： "(())"
# 输出： 2
# 示例 3：
#
# 输入： "()()"
# 输出： 2
# 示例 4：
#
# 输入： "(()(()))"
# 输出： 6


class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        # stack = []
        # num = []
        # for c in s:
        #     if c == ")":
        #         while stack[-1]!="(":
        #             num.append(stack.pop())
        #         stack.pop()
        #         if num:
        #             stack.append(2*sum(num))
        #         else:
        #             stack.append(1)
        #         num = []
        #     else:
        #         stack.append(c)
        # return sum(stack)

        ##使用bal计算深度，核心括号对的分数为2^bal
        # ans = bal = 0
        # for i, x in enumerate(s):
        #     if x == '(':
        #         bal += 1
        #     else:
        #         bal -= 1
        #         if s[i-1] == '(':
        #             ans += 1 << bal
        # return ans

        #改进了我的思路，使用了stack存深度
        stack = [0]  # The score of the current frame

        for x in s:
            #遇到"("，增加一个0，即初始分数
            if x == '(':
                stack.append(0)
            #遇到")"，计算该括号的分数
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()


