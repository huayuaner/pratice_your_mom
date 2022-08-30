# 给你一个整数数组 nums 。你可以选定任意的 正数 startValue 作为初始值。
#
# 你需要从左到右遍历 nums 数组，并将 startValue 依次累加上 nums 数组中的值。
#
# 请你在确保累加和始终大于等于 1 的前提下，选出一个最小的 正数 作为 startValue 。
from itertools import accumulate
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # min_val = float('inf')
        # pre_sum = 0
        # for num in nums:
        #     pre_sum += num
        #     min_val = min(min_val, pre_sum)
        # return 1-min_val if min_val < 0 else 1
        return max(1, 1-min(accumulate(nums)))