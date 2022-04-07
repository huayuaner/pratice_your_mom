给定一个含有 n 个正整数的数组和一个正整数 target 。

# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
#
#  
#
# 示例 1：
#
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
# 示例 2：
#
# 输入：target = 4, nums = [1,4,4]
# 输出：1
# 示例 3：
#
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 滑窗
        l, r = 0, 0
        total = 0
        n = len(nums)
        ans = float("inf")
        while r < n:
            total += nums[r]
            # 这个设计使得l最多比r大1
            while total >= target:
                ans = min(ans, r - l + 1)
                total -= nums[l]
                l += 1
            r += 1

            # print(l, r, total)
        return ans if ans != float("inf") else 0
