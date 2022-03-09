# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
#
#  
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#  
#
# 示例 1:
#
# 输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
# 输出: 2

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n = len(nums)
        # cnt = Counter(nums)
        # for key in cnt.keys():
        #     if cnt[key] > n//2:
        #         return key

        # nums.sort()
        # n = len(nums)
        # cnt = 0
        # return nums[n//2]

        # 摩尔投票法
        # 本质是记录众数和非众数出现的次数
        # 出现众数+1 非众数-1
        # 由于众数超过 n//2，所以最后会是正值
        # 最后留下的candidate必然是超过一半的众数
        # 就是用众数的出现次数抵消其他数出现的次数
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate