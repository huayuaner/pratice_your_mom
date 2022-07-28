# 根据 逆波兰表示法，求该后缀表达式的计算结果。
#
# 有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
#
#  
#
# 说明：
#
# 整数除法只保留整数部分。
# 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack = []
        # for t in tokens:
        #     if t.isdigit() or t[1:].isdigit():
        #         stack.append(int(t))
        #     else:
        #         # print(stack, t)
        #         cur = stack.pop()
        #         pre = stack.pop()
        #         if t == '+':
        #             res = pre + cur
        #         elif t=='-':
        #             res = pre- cur
        #         elif t=='*':
        #             res = pre * cur
        #         else:
        #             res = int(pre / cur)
        #         stack.append(res)
        #     # print(stack)
        # return stack[0]

