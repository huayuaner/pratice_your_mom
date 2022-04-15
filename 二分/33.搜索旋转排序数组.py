# 整数数组 nums 按升序排列，数组中的值 互不相同 。
#
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
#
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
#
#  
#
# 示例 1：
#
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
# 示例 2：
#
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
# 示例 3：
#
# 输入：nums = [1], target = 0
# 输出：-1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            # 找单调区间
            if nums[0] <= nums[m]:
                if nums[0] <= target <= nums[m]:
                    r = m
                else:
                    l = m + 1
            # 其中包含旋转点
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m
        return l if nums[l] == target else -1
