# 求解一个给定的方程，将x以字符串 "x=#value" 的形式返回。该方程仅包含 '+' ， '-' 操作，变量 x 和其对应系数。
#
# 如果方程没有解，请返回 "No solution" 。如果方程有无限解，则返回 “Infinite solutions” 。
#
# 题目保证，如果方程中只有一个解，则 'x' 的值是一个整数。
#
#  
#
# 示例 1：
#
# 输入: equation = "x+5-3+x=6+x-2"
# 输出: "x=2"
# 示例 2:
#
# 输入: equation = "x=x"
# 输出: "Infinite solutions"
# 示例 3:
#
# 输入: equation = "2x=x"
# 输出: "x=0"

import re
class Solution:
    def solveEquation(self, equation: str) -> str:
        # 优雅写法
        w = b = 0
        i,n,sign = 0, len(equation),1
        while i < n:
            if equation[i] == '=':
                sign = -1
                i += 1
                continue
            s = sign
            if equation[i] == '+':
                i += 1
            elif equation[i] == '-':
                s = -s
                i += 1
            cur,valid = 0, False
            while i<n and equation[i].isdigit():
                valid = True
                cur = cur*10 + int(equation[i])
                i += 1
            if i<n and equation[i] == 'x':
                w += s*cur if valid else s
                i += 1
            else:
                b += cur*s
        if w == 0:
            return  "Infinite solutions" if b == 0 else "No solution"
        return f"x={-b//w}"
        # l,r = equation.split('=')
        # # print(l,r)

        # def caul(s):
        #     cur = ''
        #     idx = 0
        #     # pre_sign = '+' if s[0].isdigit() else '-'
        #     if s[0] in '+-':
        #         idx = 1
        #         pre_sign = s[0]
        #     else:
        #         idx =0
        #         pre_sign = '+'
        #     w = b = 0
        #     n = len(s)
        #     # print(s)
        #     while idx <= n:
        #         if idx == n or s[idx] in '+-':
        #             if 'x' in cur:
        #                 if pre_sign == '+':
        #                     w += int(cur[:-1]) if cur[:-1] else 1
        #                 else:
        #                     w -= int(cur[:-1]) if cur[:-1] else 1
        #             else:
        #                 if pre_sign =='+':
        #                     # print(idx)
        #                     b += int(cur)
        #                 else:
        #                     # print(idx)
        #                     b -= int(cur)
        #             pre_sign = s[idx] if idx < n else -1
        #             cur = ''
        #         else:
        #             cur += s[idx]
        #         idx += 1
        #     return w, b
        # w_l, b_l = caul(l)
        # w_r,b_r = caul(r)
        # # print(w_l, b_l, w_r, b_r)
        # if w_r == w_l  and b_l == b_r:
        #     return "Infinite solutions"
        # elif w_r == w_l  and b_l != b_r:
        #     return "No solution"
        # else:
        #     return f'x={(b_r-b_l)//(w_l-w_r)}'

