# 给你一个整数数组 nums ，请你将数组按照每个值的频率 升序 排序。如果有多个值的频率相同，请你按照数值本身将它们 降序 排序。 
#
# 请你返回排序后的数组。
#
from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnts = Counter(nums)
        nums.sort(key = lambda x: (cnts[x], -x))
        return nums