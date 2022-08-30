# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
#
# 注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。
#
#  
#
# 示例 1：
#
# 输入：s = "1 + 1"
# 输出：2
# 示例 2：
#
# 输入：s = " 2-1 + 2 "
# 输出：3
# 示例 3：
#
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23
class Solution:
    def calculate(self, s: str) -> int:
        tot = 0
        sign = 1
        stack = []
        i = 0
        n = len(s)
        while i < n:
            if s[i].isdigit():
                num = int(s[i])
                while i + 1 < n and s[i + 1].isdigit():
                    num = num * 10 + int(s[i + 1])
                    i += 1
                tot += num * sign
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append(tot)
                stack.append(sign)
                tot = 0
                sign = 1
            elif s[i] == ')':
                tot *= stack.pop()
                tot += stack.pop()
            # print(stack)
            i += 1
        return tot
        # stack = []
        # n = len(s)
        # num = 0
        # presign = '+'
        # for i,c in enumerate(s):
        #     if c==' ' and i!=n-1:
        #         continue

        #     if c.isdigit():
        #         # print(c)
        #         num = num*10 + int(c)
        #         # print(num)
        #     # print(i,num)
        #     if c in '+-' or i == n-1 or c==')':
        #         # print(num,n,i)
        #         if presign == '+':
        #             stack.append(num)
        #         else:
        #             stack.append(-num)
        #         # print(stack,i)
        #         presign = c
        #         num = 0
        #     if c=='(':
        #         stack.append(presign)
        #         stack.append(c)
        #         presign = '+'
        #     if c==')':
        #         # print(stack)
        #         tmp = 0
        #         while stack[-1]!='(':
        #             tmp += stack.pop()
        #         stack.pop()
        #         sign = stack.pop()
        #         if sign == '-':
        #             tmp = -tmp

        #         stack.append(tmp)

        # # print(stack)
        # return sum(stack)
