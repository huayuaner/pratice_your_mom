# 给你一个整数数组 nums ，数组中共有 n 个整数。132 模式的子序列 由三个整数 nums[i]、nums[j] 和 nums[k] 组成，并同时满足：i < j < k 和 nums[i] < nums[k] < nums[j] 。
#
# 如果 nums 中存在 132 模式的子序列 ，返回 true ；否则，返回 false 。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3,4]
# 输出：false
# 解释：序列中不存在 132 模式的子序列。
# 示例 2：
#
# 输入：nums = [3,1,4,2]
# 输出：true
# 解释：序列中有 1 个 132 模式的子序列： [1, 4, 2] 。
# 示例 3：
#
# 输入：nums = [-1,3,2,0]
# 输出：true
# 解释：序列中有 3 个 132 模式的的子序列：[-1, 3, 2]、[-1, 3, 0] 和 [-1, 2, 0] 。
#
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        if len(nums) < 3:
            return False
        stack = []
        max_ = float("-inf")
        #设置反向遍历单调减栈
        for num in reversed(nums):
            #由于是单调减，max_必定小于栈中的某个元素，且这个元素是在max_左边，所以出现了num<max_，返回True
            if num < max_:
                return True
            while stack and num > stack[-1]:
                #如果不满足单调减，则pop且更新max_
                max_ = max(stack.pop(), max_)
            stack.append(num)
        return False






