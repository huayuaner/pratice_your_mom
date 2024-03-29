# 给你一个长度为 n 的整数数组，每次操作将会使 n - 1 个元素增加 1 。返回让数组所有元素相等的最小操作次数。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：3
# 解释：
# 只需要3次操作（注意每次操作会增加两个元素的值）：
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
# 示例 2：
#
# 输入：nums = [1,1,1]
# 输出：0
class Solution:
    def minMoves(self, nums: List[int]) -> int:

        min_val = min(nums)
        gap = 0
        for num in nums:
            gap += num-min_val
        return gap