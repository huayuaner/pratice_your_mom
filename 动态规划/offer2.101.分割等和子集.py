# 给定一个非空的正整数数组 nums ，请判断能否将这些数字分成元素和相等的两部分。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：nums 可以分割成 [1, 5, 5] 和 [11] 。
# 示例 2：
#
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：nums 不可以分为和相等的两部分

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2:
            return False
        target = total//2
        # dp[i] 表示target为i能否实现
        dp = [False]*(target+1)
        dp[0] = True
        for num in nums:
            for i in range(target, num-1, -1):
                # 转移方程dp[i] 只要dp[i-num]和dp[i]中一个为真即可
                dp[i] = dp[i] or dp[i-num]
        return dp[target]
