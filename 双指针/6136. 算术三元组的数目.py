# 给你一个下标从 0 开始、严格递增 的整数数组 nums 和一个正整数 diff 。如果满足下述全部条件，则三元组 (i, j, k) 就是一个 算术三元组 ：
#
# i < j < k ，
# nums[j] - nums[i] == diff 且
# nums[k] - nums[j] == diff
# 返回不同 算术三元组 的数目。
#
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # 时间 N 空间 N
        # s = set()
        # ans = 0
        # for num in nums:
        #     if num-diff in s and num-2*diff in s:
        #         ans += 1
        #     s.add(num)
        # return ans

        # 时间 N 空间 1
        ans = 0
        i, j = 0, 1
        for num in nums:
            while nums[j] + diff < num:
                j += 1
            if nums[j] + diff != num:
                continue
            while nums[i] + diff < nums[j]:
                i += 1
            if nums[i] + diff == nums[j]:
                ans += 1
        return ans
