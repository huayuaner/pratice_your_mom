# 如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。
#
# 例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
# 给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。
#
# 子数组 是数组中的一个连续序列。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3,4]
# 输出：3
# 解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。
# 示例 2：
#
# 输入：nums = [1]
# 输出：0

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # if len(nums)<3:
        #     return 0
        # ans = []
        # cnt = 2
        # for i in range(2, len(nums)):
        #     if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
        #         cnt += 1
        #         if i == len(nums) - 1:
        #             ans.append(cnt)
        #         # ans[-1] = max(ans[-1])
        #     else:
        #         ans.append(cnt)
        #         cnt = 2

        # return sum([(num-1)*(num-2)//2 for num in ans if num>2])

        # 动态规划
        if len(nums) < 3:
            return 0
        cnt = 0
        # dp[i] 表示以i为结尾的等差数列的个数
        dp = [0 for _ in range(len(nums))]
        for i in range(2, len(nums)):
            if nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]:
                dp[i] = dp[i - 1] + 1
                cnt += dp[i]
        return cnt
