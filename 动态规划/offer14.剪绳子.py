# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
#
# 示例 1：
#
# 输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1
# 示例 2:
#
# 输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

class Solution:
    def cuttingRope(self, n: int) -> int:
        # if n==2:
        #     return 1
        # if n==3:
        #     return 2
        # tmp = 4
        # i = 4
        # while i<n:
        #     if tmp%2 != 0:
        #         tmp = tmp//3 *4
        #     else:
        #         tmp = tmp + tmp // 2
        #     i += 1
        # return tmp

        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return int(math.pow(3, a))
        if b == 1:
            return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)

