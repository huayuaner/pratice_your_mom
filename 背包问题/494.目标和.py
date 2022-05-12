# 给你一个整数数组 nums 和一个整数 target 。
#
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
#
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# 示例 2：
#
# 输入：nums = [1], target = 1
# 输出：1

from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        该方案由于不确定val+num的范围，所以对于dp列数的定义和迭代比较麻烦，索性直接使用哈希表完成动态规划
        '''
        # dp[i][j] 表示 0-i的数字加减得到j的方案数
        # n = len(nums)
        # dp = defaultdict(int)
        # # 初始化，甚么都不选和为0有1种方案
        # dp[0] = 1
        # for num in nums:
        #     tmp = defaultdict(int)
        #     for val in dp.keys():
        #         tmp[val+num] += dp[val]
        #         tmp[val-num] += dp[val]
        #     dp = tmp
        # return dp[target]

        # 方案2
        # 数学推导优化
        # nums的和为sum，其中取负号的数字的和为neg，取正号数字的的和为 sum-neg
        # 可以简单得到 (sum-neg) - neg = target -> (sum-target)/2 = neg
        # 由于num>=0 -> neg也是非负整数 且 (sum-target)必须为 偶数
        # 所以使用 dp[i][j] 去求 和为neg的组合 转化成了0-1背包问题

        total, n = sum(nums), len(nums)
        if total - target < 0 or (total - target) % 2 == 1:
            return 0
        neg = (total - target) // 2
        # # dp[i][j] 表示前i个数的和为j的方案数
        # # dp = [[0 for _ in range(neg+1)] for _ in range(n+1)]
        # # dp[0][0] = 1
        # # for i in range(1, n+1):
        # #     for j in range(neg+1):
        # #         dp[i][j] = dp[i-1][j]
        # #         if j>=nums[i-1]:
        # #             dp[i][j] += dp[i-1][j-nums[i-1]]
        # # # print(dp)
        # # return dp[-1][-1]

        # # 滚动数组
        dp = [0 for _ in range(neg + 1)]
        dp[0] = 1
        for i in range(n):
            for j in range(neg, nums[i] - 1, -1):
                # if j>=nums[i]:
                dp[j] += dp[j - nums[i]]
            # print(dp)
        return dp[-1]
