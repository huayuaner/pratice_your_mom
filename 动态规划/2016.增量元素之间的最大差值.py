# 给你一个下标从 0 开始的整数数组 nums ，该数组的大小为 n ，请你计算 nums[j] - nums[i] 能求得的 最大差值 ，其中 0 <= i < j < n 且 nums[i] < nums[j] 。
#
# 返回 最大差值 。如果不存在满足要求的 i 和 j ，返回 -1 。

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # 单调栈
        # 记录弹出的最小值
        # min_ = float("inf")
        # ans = -1
        # stack = []
        # for num in nums:
        #     if stack and num > stack[-1]:
        #         min_ = min(min_, stack.pop())
        #     stack.append(num)
        #     ans = max(ans, num-min_)
        # return ans

        # 维护遍历过的最小值
        min_, ans = nums[0], -1
        for i in range(1, len(nums)):
            if nums[i] > min_:
                ans = max(ans, nums[i] - min_)
            else:
                min_ = nums[i]

        return ans