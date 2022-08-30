# 给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
#
#  
#
# 示例 1：
#
# 输入：nums = [3,0,1]
# 输出：2
# 解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。
# 示例 2：
#
# 输入：nums = [0,1]
# 输出：2
# 解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。
# 示例 3：
#
# 输入：nums = [9,6,4,2,3,5,7,0,1]
# 输出：8
# 解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。
# 示例 4：
#
# 输入：nums = [0]
# 输出：1
# 解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中。
#
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # for i,num in enumerate(nums):
        #     while nums[i] != i and nums[i]!=n:
        #         nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        #         # print(nums)
        # for i, num in enumerate(nums):
        #     if num!=i:
        #         return i
        # return n

        # 位运算
        # xor = 0
        # n = len(nums)
        # for num in nums:
        #     xor ^= num
        # for i in range(n+1):
        #     xor ^= i
        # return xor

        # 位运算优雅写法
        # xor = 0
        # n = len(nums)
        # for i,num in enumerate(nums):
        #     xor ^= i^num
        # xor ^= n
        # return xor

        # 加合法
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)

