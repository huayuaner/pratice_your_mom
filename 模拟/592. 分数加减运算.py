# 给定一个表示分数加减运算的字符串 expression ，你需要返回一个字符串形式的计算结果。 
#
# 这个结果应该是不可约分的分数，即最简分数。 如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1。所以在上述例子中, 2 应该被转换为 2/1。
#
#  
#
# 示例 1:
#
# 输入: expression = "-1/2+1/2"
# 输出: "0/1"
#  示例 2:
#
# 输入: expression = "-1/2+1/2+1/3"
# 输出: "1/3"
# 示例 3:
#
# 输入: expression = "1/3-1/2"
# 输出: "-1/6"

import math
class Solution:
    def fractionAddition(self, expression: str) -> str:
        pre = '0/1'
        idx = 0
        n = len(expression)
        def calculate(num1, num2,sign):
            # print(num1, num2)
            up1, down1 = map(int, num1.split('/'))
            up2, down2 = map(int, num2.split('/'))
            # down1,down2 = down1*down2, down1*down2
            up1, up2 = up1 * down2, up2*down1
            newup = up1 - up2 if sign =='-' else up1+up2
            newdown = down1*down2
            gcd = math.gcd(newup,newdown)
            newup //= gcd
            newdown //= gcd
            return str(newup) + '/' + str(newdown)
        while idx<n:
            # cur = ''
            if expression[idx] in '+-':
                sign = expression[idx]
                # 往后找下一个分数
                start = end = idx + 1
            else:
                sign = '+'
                start = end = idx
            while end<n and expression[end] not in '+-':
                end += 1
            cur = expression[start: end]
            pre = calculate(pre,cur, sign)
            idx = end
        return pre







