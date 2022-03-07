# 给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。
#
# 示例1:
#
# 输入: "2-1-1"
# 输出: [0, 2]
# 解释:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# 示例2:
#
# 输入: "2*3-4*5"
# 输出: [-34, -14, -10, -10, 10]
# 解释:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
memory = {}


def func(expression):
    if (expression[0] + expression[-1]) in memory.keys():
        return memory[expression[0] + expression[-1]]
    if expression.isdigit():
        return [int(expression)]
    res = []
    for i, char in enumerate(expression):
        if char in ['+', '-', '*']:
            left = self.diffWaysToCompute(expression[:i])
            right = self.diffWaysToCompute(expression[i + 1:])

            for l in left:
                for r in right:
                    if char == '+':
                        res.append(l + r)
                    if char == '*':
                        res.append(l * r)
                    if char == '-':
                        res.append(l - r)
    memory[expression[0] + expression[-1]] = res
    return res


return func(expression)

