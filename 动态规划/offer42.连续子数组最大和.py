# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
#
# 要求时间复杂度为O(n)。
#
#  
#
# 示例1:
#
# 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        ans = float("-inf")
        for num in nums:
            # 之后加入当前值或者从当前值开始两种情况
            pre = max(tmp+num, num)
            ans = max(ans,tmp)
        return ans
