# 给定一个整数 n ，返回 n! 结果中尾随零的数量。
#
# 提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
#
#  
#
# 示例 1：
#
# 输入：n = 3
# 输出：0
# 解释：3! = 6 ，不含尾随 0
# 示例 2：
#
# 输入：n = 5
# 输出：1
# 解释：5! = 120 ，有一个尾随 0
# 示例 3：
#
# 输入：n = 0
# 输出：0

class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans

