# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 target，返回 [-1, -1]。
#
# 进阶：
#
# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
#  
#
# 示例 1：
#
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 示例 2：
#
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 示例 3：
#
# 输入：nums = [], target = 0
# 输出：[-1,-1]
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        n = len(nums)
        # 双 二分
        l, r = 0, len(nums)
        # 找左边
        while l<r:
            m = l + (r-l)//2
            if nums[m] >= target:
                r = m
            else:
                l = m+1
        if not 0<=l<n or nums[l] != target:
            return [-1,-1]
        left = l
        r = len(nums)
        while l<r:
            m = l + (r-l)//2
            if nums[m] > target:
                r = m
            else:
                l = m+1
        right = r-1
        return [left, right]

