# 给你一个整数数组 nums，将 nums 中的的所有偶数元素移动到数组的前面，后跟所有奇数元素。
#
# 返回满足此条件的 任一数组 作为答案。
#
#  
#
# 示例 1：
#
# 输入：nums = [3,1,2,4]
# 输出：[2,4,3,1]
# 解释：[4,2,3,1]、[2,4,1,3] 和 [4,2,1,3] 也会被视作正确答案。
# 示例 2：
#
# 输入：nums = [0]
# 输出：[0]

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0, n-1
        while l<r:
            # if nums[l] % 2 == 0:
            #     l += 1
            #     continue
            # if nums[r] % 2 == 1:
            #     r -= 1
            #     continue
            # if nums[l] % 2:
            #     nums[r], nums[l] = nums[l], nums[r]
            #     r -= 1
            # if nums[r] % 2 == 0:
            #     nums[r], nums[l] = nums[l], nums[r]
            #     l += 1
            while l < r and nums[l] % 2 == 0 :
                l += 1
            while l < r and nums[r] % 2 == 1:
                r -= 1
            if l < r:
                nums[r], nums[l] = nums[l], nums[r]
                r -= 1
                l += 1

        return nums