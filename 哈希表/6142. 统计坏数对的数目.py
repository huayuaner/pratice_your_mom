# 给你一个下标从 0 开始的整数数组 nums 。如果 i < j 且 j - i != nums[j] - nums[i] ，那么我们称 (i, j) 是一个 坏数对 。
#
# 请你返回 nums 中 坏数对 的总数目。

from collections import Counter
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        #  j - i != nums[j] - nums[i] => nums[i] - i != nums[j] - j
        # b[i] = nums[i] - i
        # b[i] != b[j]
        n = len(nums)
        # 总共的对数
        tot = n*(n-1)//2
        good = 0
        cnt = Counter()
        for i,num in enumerate(nums):
            good += cnt[num-i]
            cnt[num-i]+=1
        return tot-good