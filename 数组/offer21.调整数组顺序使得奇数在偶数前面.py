# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。
#
#  
#
# 示例：
#
# 输入：nums = [1,2,3,4]
# 输出：[1,3,2,4]
# 注：[3,1,2,4] 也是正确的答案之一。
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        l,r = 0, len(nums)-1
        while l<r:
            while l<r and nums[l] % 2 == 1:
                l += 1
            while r>l and nums[r] % 2 ==0:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums
