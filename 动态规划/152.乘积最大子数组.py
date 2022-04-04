# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
# 测试用例的答案是一个 32-位 整数。
#
# 子数组 是数组的连续子序列。
#
#  
#
# 示例 1:
#
# 输入: nums = [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 示例 2:
#
# 输入: nums = [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_dp = [0]*n
        min_dp = [0]*n
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        for i in range(1, n):
            # 问题在于正负号的情况
            # 所以使用了两个dp，一个存最大，一个存最小，为了防止[-2,3,-5]的情况
            max_dp[i] = max(max_dp[i-1]*nums[i], min_dp[i-1]*nums[i], nums[i])
            min_dp[i] = min(max_dp[i-1]*nums[i], min_dp[i-1]*nums[i], nums[i])
        # print(max_dp, min_dp)
        return max(max_dp)# max(,max(min_dp))