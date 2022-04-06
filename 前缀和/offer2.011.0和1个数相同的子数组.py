# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
#
#  
#
# 示例 1:
#
# 输入: nums = [0,1]
# 输出: 2
# 说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。
# 示例 2:
#
# 输入: nums = [0,1,0]
# 输出: 2
# 说明: [0, 1] (或 [1, 0]) 是具有相同数量 0 和 1 的最长连续子数组。

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 前缀和
        dic = dict()
        dic[0] = -1
        pre = 0
        ans = 0
        for idx, num in enumerate(nums):
            pre += (1 if num == 1 else -1)
            if pre in dic:
                ans = max(ans, idx - dic[pre])
            else:
                dic[pre] = idx
        return ans


