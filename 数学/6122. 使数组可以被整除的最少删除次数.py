# 给你两个正整数数组 nums 和 numsDivide 。你可以从 nums 中删除任意数目的元素。
#
# 请你返回使 nums 中 最小 元素可以整除 numsDivide 中所有元素的 最少 删除次数。如果无法得到这样的元素，返回 -1 。
#
# 如果 y % x == 0 ，那么我们说整数 x 整除 y 。
#
#  
#
# 示例 1：
#
# 输入：nums = [2,3,2,4,3], numsDivide = [9,6,9,3,15]
# 输出：2
# 解释：
# [2,3,2,4,3] 中最小元素是 2 ，它无法整除 numsDivide 中所有元素。
# 我们从 nums 中删除 2 个大小为 2 的元素，得到 nums = [3,4,3] 。
# [3,4,3] 中最小元素为 3 ，它可以整除 numsDivide 中所有元素。
# 可以证明 2 是最少删除次数。
# 示例 2：
#
# 输入：nums = [4,3,6], numsDivide = [8,2,6,10]
# 输出：-1
# 解释：
# 我们想 nums 中的最小元素可以整除 numsDivide 中的所有元素。
# 没有任何办法可以达到这一目的。
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        # nums.sort()
        n_d = len(numsDivide)
        n = len(nums)
        gcd_num = reduce(gcd, numsDivide)
        # gcd_num = numsDivide[0]
        # for i in range(1,n_d):
        #     gcd_num = gcd(gcd_num, numsDivide[i])

        # for i,num in enumerate(nums):
        #     if  gcd_num % num==0:
        #         return i
        #     elif num>gcd_num:
        #         break
        # return -1
        # 上面这块代码等价于
        # return next((i for i,num in enumerate(nums) if gcd_num%num==0),-1)
        min_val = min((num for num in nums if gcd_num % num == 0), default=-1)
        if min_val == -1:
            return -1
        return sum(num < min_val for num in nums)
