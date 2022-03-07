# 统计一个数字在排序数组中出现的次数。
#
#  
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: 0
#  


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分
        # l, r = 0, len(nums)-1
        # while l<=r:
        #     m = l + (r-l)//2
        #     if nums[m]<target:
        #         l = m + 1
        #     elif nums[m] > target:
        #         r = m - 1
        #     else:
        #         if nums[r]!=target:
        #             r -= 1
        #         if nums[l]!= target:
        #             l += 1
        #         if nums[l] == nums[r] == target:
        #             return r-l+1
        # return 0

        # 二分 一次找左边界一次找右边界
        # 找右边界+1的位置
        # l, r = 0, len(nums)-1
        # while l<=r:
        #     m = l + (r - l)//2
        #     if nums[m] <= target:
        #         l = m + 1
        #     else:
        #         r =  m - 1
        # right = l
        # # 这个判断语句提前判断了有没有target存在于数组中
        # if (right > 0 and nums[right-1]!=target):
        #     return 0
        # # 不用重新设置r是因为左边界必在右边界左边，所以不用改变
        # l = 0
        # # 找左边界-1的位置
        # while l<=r:
        #     m = l + (r - l)//2
        #     if nums[m] >= target:
        #         r = m-1
        #     else:
        #         l = m+1
        # left = r
        # return right - left - 1


        # 设置函数返回tar的右边界
        def helper(tar):
            l, r = 0, len(nums)-1
            while l<=r:
                m = l + (r-l)//2
                if nums[m] <= tar:
                    l = m+1
                else:
                    r = m-1
            return l
        # tar-1的右边界就是tar的第一个数
        return helper(target)- helper(target-1)