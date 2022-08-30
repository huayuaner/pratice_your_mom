# 累加数 是一个字符串，组成它的数字可以形成累加序列。
#
# 一个有效的 累加序列 必须 至少 包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
#
# 给你一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是 累加数 。如果是，返回 true ；否则，返回 false 。
#
# 说明：累加序列里的数 不会 以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
#
#  
#
# 示例 1：
#
# 输入："112358"
# 输出：true
# 解释：累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# 示例 2：
#
# 输入："199100199"
# 输出：true
# 解释：累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        #     n = len(num)
            ##双循环找第二个值的头和尾
        #     for seconds in range(1, n-1):
        #         if num[0] == "0" and seconds!=1:
        #             break
        #         for seconde in range(seconds, n-1):
        #             if num[seconds] == "0" and seconds != seconde:
        #                 break
        #             if self.valid(seconds, seconde,num):
        #                 return True
        #     return False
                ##验证是此时的second的头尾是否合法
        # def valid(self, seconds, seconde, num):
        #     firsts, firste = 0, seconds-1
        #     n = len(num)
        #     while seconde < n:
        #         third = self.StringAdd(num, firsts, firste, seconds, seconde)
        #         #print(num[firsts:firste+1], num[seconds:seconde+1], third)
        #         #third_ = eval(num[firsts:firste+1]+"+"+num[seconds:seconde+1])
        #         #print(third, third_,num[firsts:firste+1], num[seconds:seconde+1])
        #         thirds, thirde = seconde+1, seconde+len(third)
        #         if thirde >= n or num[thirds:thirde+1] != third:
        #             return False
        #         if thirde == n-1:
        #             return True
        #         firsts, firste = seconds, seconde
        #         seconds, seconde = thirds, thirde
        #     return False
        ## 字符串加法防止溢出
        # def StringAdd(self, num, firsts, firste, seconds, seconde):
        #     carry = 0
        #     third = []
        #     lenfir, lensec = firste - firsts + 1, seconde - seconds + 1
        #     while lenfir or lensec  or carry:
        #         #print()

        #         sum_ = (int(num[firsts+lenfir-1]) if lenfir>0 else 0 )  + (int(num[seconds+lensec - 1]) if lensec>0 else 0) +carry
        #         #print(sum_)
        #         third.append(str(sum_%10))
        #         carry = sum_//10
        #         lenfir = lenfir - 1 if lenfir else lenfir
        #         lensec = lensec - 1 if lensec else lensec
        #     #print(third)
        #     #print("".join(reversed(third)))
        #     return "".join(reversed(third))

        #用dfs代替了valid里的遍历，并且通过剪枝减少计算量
        def dfs(num, FirstNum, SecondNum):
            if not num:
                return True
            ThirdNum = FirstNum + SecondNum
            Length = len(str(ThirdNum))
            if num[:Length] != str(ThirdNum):
                return False
            else:
                return dfs(num[Length:], SecondNum, ThirdNum)

        n = len(num)
        for i in range(1, n - 1):
            if num[0] == '0' and i > 1:
                return False
            for j in range(i + 1, n):
                if num[i] == '0' and j - i > 1:
                    break
                if dfs(num[j:], int(num[:i]), int(num[i:j])):
                    return True
        return False










