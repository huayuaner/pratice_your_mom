# 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。
#
#  
#
# 示例:
#
# 输入: a = 1, b = 1
# 输出: 2

class Solution:
    def add(self, a: int, b: int) -> int:
        # 位运算
        x = 0xffffffff
        # a,b 32位以上的值置0
        a, b = a&x, b&x
        while b :
            c = (a&b)<<1
            a = a^b
            b = c & x
        # 0x7fffffff代表了最大正数的补码
        return a if a<=0x7fffffff else ~(a^x)