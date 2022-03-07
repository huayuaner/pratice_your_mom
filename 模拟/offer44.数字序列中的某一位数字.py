# 数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。
#
# 请写一个函数，求任意第n位对应的数字。
#
#  
#
# 示例 1：
#
# 输入：n = 3
# 输出：3
# 示例 2：
#
# 输入：n = 11
# 输出：0

class Solution:
    def findNthDigit(self, n: int) -> int:
        start, digit,cnt = 1, 1, 0
        while n>cnt:
            n -= cnt
            cnt = 9*start*digit
            start *= 10
            digit += 1
        #print(n,start, digit)
        num = start//10 + (n-1)//(digit-1)
        #print(num)
        idx = n - (num-start//10)*(digit-1)
        #print(idx)
        return int(str(num)[idx-1])
