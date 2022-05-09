# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
#
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
#
#  
#
# 示例 1：
#
# 输入：nums = [10,2]
# 输出："210"
# 示例 2：
#
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"

from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def rule(num1, num2):
            a, b = num1 + num2, num2 + num1
            if a > b:
                return -1
            elif a < b:
                return 1
            else:
                return 0

        nums_c = [str(num) for num in nums]

        nums_c.sort(key=functools.cmp_to_key(rule))

        # print(nums_c)
        return ''.join(nums_c) if nums_c[0] != '0' else '0'



