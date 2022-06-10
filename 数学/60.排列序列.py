# 给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。
#
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 给定 n 和 k，返回第 k 个排列。
#
#  
#
# 示例 1：
#
# 输入：n = 3, k = 3
# 输出："213"
# 示例 2：
#
# 输入：n = 4, k = 9
# 输出："2314"
# 示例 3：
#
# 输入：n = 3, k = 1
# 输出："123"
from math import factorial


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        valid = [1] * n
        fac = factorial(n - 1)
        ans = list()
        k -= 1
        for _ in range(n):
            order = k // fac + 1
            # print(valid,order)
            for j in range(len(valid)):
                order -= valid[j]
                # print(order)
                if order == 0:
                    ans.append(str(j + 1))
                    valid[j] = 0
                    break

            k %= fac
            fac //= ((n - 1) if n != 1 else 1)
            n -= 1

        return ''.join(ans)
