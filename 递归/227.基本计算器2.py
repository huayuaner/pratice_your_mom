# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
#
# 整数除法仅保留整数部分。
# 示例 1：
#
# 输入：s = "3+2*2"
# 输出：7
# 示例 2：
#
# 输入：s = " 3/2 "
# 输出：1
# 示例 3：
#
# 输入：s = " 3+5 / 2 "
# 输出：5

class Solution:
    def calculate(self, s: str) -> int:
        #默认第一个为正数
        presign = "+"
        stack = []
        num = 0
        n = len(s)
        for i in range(n):
            #暂存数字
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            #当遍历到最后或者遇到运算符进入
            if i == n - 1 or s[i] in '+-*/':
                #加减直接append
                if presign == "+":
                    stack.append(num)
                if presign == "-":
                    stack.append(-num)
                #乘除append计算后的数字
                if presign == "/":
                    stack.append(int(stack.pop() / num))
                if presign == "*":
                    stack.append(stack.pop() * num)
                #更新presign
                presign = s[i]
                num = 0
        return sum(stack)

