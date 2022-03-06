# 求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
#
#  
#
# 示例 1：
#
# 输入: n = 3
# 输出: 6
# 示例 2：
#
# 输入: n = 9
# 输出: 45

class Solution:
    def __init__(self):
        self.ans = 0
    def sumNums(self, n: int) -> int:
        # 用了递归用了if会不合法
        # 这句代替if
        # 当n>1时后面的递归会继续执行
        # 当n=1时这句话不再执行，进行下方的self.ans += n
        n>1 and self.sumNums(n-1)
        self.ans += n
        return self.ans