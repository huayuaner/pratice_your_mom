# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。
# 示例 2：
#
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
#


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # dp[i][j]表示前i个数能否组成和为j的数
        total, n = sum(nums), len(nums)
        if total%2:
            return False
        half = total // 2
        # dp = [[False for _ in range(half+1)] for _ in range(n+1)]
        # # 和为0只要都不选就可以，所以可以初始化为0
        # for i in range(n+1):
        #     dp[i][0] = True
        # for i in range(1,n+1):
        #     for j in range(half+1):
        #         # 不选i 和 选i
        #         dp[i][j] = dp[i-1][j]
        #         if j >= nums[i-1]:
        #             dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]
        #     # print(dp[i])
        # # print(dp)
        # return dp[-1][-1]

        # 滚动数组
        dp = [False for _ in range(half+1)]
        dp[0] = True
        for i in range(n):
            for j in range(half, nums[i]-1, -1):
                dp[j] = dp[j] or dp[j-nums[i]]
        return dp[-1]




