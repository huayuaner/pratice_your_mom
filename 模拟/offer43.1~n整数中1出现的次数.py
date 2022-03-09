# 输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
#
# 例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。
#
#  
#
# 示例 1：
#
# 输入：n = 12
# 输出：5
# 示例 2：
#
# 输入：n = 13
# 输出：6

class Solution:
    def countDigitOne(self, n: int) -> int:
        digit, ans = 1, 0
        high, low, cur = n//10, 0, n%10
        while high!=0 or cur !=0:
            if cur == 0:
                ans += high*digit
            elif cur == 1:
                ans += high*digit + low + 1
            else:
                ans += (high+1)*digit
            low += cur*digit
            cur = high%10
            high //= 10
            digit *=10
        return ans

