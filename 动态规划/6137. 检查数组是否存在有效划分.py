# 给你一个下标从 0 开始的整数数组 nums ，你必须将数组划分为一个或多个 连续 子数组。
#
# 如果获得的这些子数组中每个都能满足下述条件 之一 ，则可以称其为数组的一种 有效 划分：
#
# 子数组 恰 由 2 个相等元素组成，例如，子数组 [2,2] 。
# 子数组 恰 由 3 个相等元素组成，例如，子数组 [4,4,4] 。
# 子数组 恰 由 3 个连续递增元素组成，并且相邻元素之间的差值为 1 。例如，子数组 [3,4,5] ，但是子数组 [1,3,5] 不符合要求。
# 如果数组 至少 存在一种有效划分，返回 true ，否则，返回 false 。

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        # 我写的版本就可以
        n = len(nums)
        dp = [False] * (n+1)
        dp[0] = True # 空数组置为True
        for i in range(1,n):
            if nums[i-1]==nums[i]:
                dp[i+1] = dp[i+1] or dp[i-1]
            if i > 1 and (nums[i-2]==nums[i-1]==nums[i] or nums[i]==nums[i-1]+1==nums[i-2]+2):
                dp[i+1] = dp[i+1] or dp[i-2]
        return dp[-1]


