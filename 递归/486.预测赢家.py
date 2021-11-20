# 给你一个整数数组 nums 。玩家 1 和玩家 2 基于这个数组设计了一个游戏。
#
# 玩家 1 和玩家 2 轮流进行自己的回合，玩家 1 先手。开始时，两个玩家的初始分值都是 0 。每一回合，玩家从数组的任意一端取一个数字（即，nums[0] 或 nums[nums.length - 1]），取到的数字将会从数组中移除（数组长度减 1 ）。玩家选中的数字将会加到他的得分上。当数组中没有剩余数字可取时，游戏结束。
#
# 如果玩家 1 能成为赢家，返回 true 。如果两个玩家得分相等，同样认为玩家 1 是游戏的赢家，也返回 true 。你可以假设每个玩家的玩法都会使他的分数最大化。
#
#
#
# 示例 1：
#
# 输入：nums = [1,5,2]
# 输出：false
# 解释：一开始，玩家 1 可以从 1 和 2 中进行选择。
# 如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2 ）可选。
# 所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。
# 因此，玩家 1 永远不会成为赢家，返回 false 。

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # 递归
        #
        # if len(nums) <= 1:
        #     return True
        # memory = [[0]* len(nums) for i in range(len(nums))]
        # def func(left, right, tune):
        #     if left==right:
        #         return nums[left]*tune
        #     if memory[left][right]!=0:
        #         return memory[left][right]
        #     else:
        #         pick_left = nums[left]*tune + func(left+1, right, -tune)
        #         pick_right = nums[right]*tune + func(left, right-1, -tune)
        #     if tune==1:
        #         memory[left][right] = max(pick_left,pick_right)
        #         return max(pick_left,pick_right)
        #     elif tune==-1:
        #         memory[left][right] = min(pick_left,pick_right)
        #         return min(pick_left, pick_right)
        # return func(0, len(nums)-1, 1)>=0

        # DP 动态规划
        dp = [[0] * len(nums) for i in range(len(nums))]
        for i in range(len(nums)):
            dp[i][i] = nums[i]
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][len(nums) - 1] >= 0


