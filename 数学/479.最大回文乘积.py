# 给定一个整数 n ，返回 可表示为两个 n 位整数乘积的 最大回文整数 。因为答案可能非常大，所以返回它对 1337 取余 。
#
#  
#
# 示例 1:
#
# 输入：n = 2
# 输出：987
# 解释：99 x 91 = 9009, 9009 % 1337 = 987
# 示例 2:
#
# 输入： n = 1
# 输出： 9

class Solution:
    def largestPalindrome(self, n: int) -> int:
        # def check(num):
        # for i in range(2, int(sqrt(num))+1):
        #     tmp = num/i
        #     if num%i==0 and min_val<=tmp<=max_val:
        #         return True
        # return False
        # 只构造回文数字
        if n == 1:
            return 9
        max_val = 10 ** n - 1
        min_val = 10 ** (n - 1) + 1
        for i in range(max_val, -1, -1):
            left = i
            num_p = i
            # 构造回文
            while left:
                num_p = num_p * 10 + left % 10
                left //= 10
            # print(num_p)
            x = max_val
            while x ** 2 >= num_p:
                if num_p % x == 0:
                    return num_p % 1337
                x -= 1



