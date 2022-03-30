# 给定一个非负整数 x ，计算并返回 x 的平方根，即实现 int sqrt(int x) 函数。
#
# 正数的平方根有两个，只输出其中的正数平方根。
#
# 如果平方根不是整数，输出只保留整数的部分，小数部分将被舍去。
#
#  
#
# 示例 1:
#
# 输入: x = 4
# 输出: 2
# 示例 2:
#
# 输入: x = 8
# 输出: 2
# 解释: 8 的平方根是 2.82842...，由于小数部分将被舍去，所以返回 2

class Solution:
    def mySqrt(self, x: int) -> int:
        # ans = 0
        # while ans**2<=x:
        #     ans += 1
        # return ans - 1

        # 二分
        l, r = 0, x
        while l<r:
            m = l + (r-l)//2
            if (tmp:=m**2)>x:
                r = m - 1
            else:
                l = m+1
                if l**2>x:
                    return l-1
            # print(l, r)
        return r
