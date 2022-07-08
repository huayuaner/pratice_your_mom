# 给你一个由数字和运算符组成的字符串 expression ，按不同优先级组合数字和运算符，计算并返回所有可能组合的结果。你可以 按任意顺序 返回答案。
#
# 生成的测试用例满足其对应输出值符合 32 位整数范围，不同结果的数量不超过 104 。
#
memo = dict()


class Solution:
    # def __init__(self) -> None:

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression in memo:
            return memo[expression]
        if expression.isdigit():
            return [int(expression)]
        ans = []
        for i, c in enumerate(expression):
            if c in '+-*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])

                for l in left:
                    for r in right:
                        if c == '+':
                            ans.append(l + r)
                        elif c == '-':
                            ans.append(l - r)
                        elif c == '*':
                            ans.append(l * r)
        memo[expression] = ans
        return ans