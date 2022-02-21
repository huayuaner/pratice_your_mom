# 给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
# 假设你总是可以到达数组的最后一个位置。
#
#  
#
# 示例 1:
#
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 示例 2:
#
# 输入: nums = [2,3,0,1,4]
# 输出: 2

class Solution:
    def jump(self, nums: List[int]) -> int:
        # bfs
        # pq = [(0,0)]
        # visited = {0}
        # step = 0
        # n = len(nums)
        # while pq:
        #     idx, step = pq.pop(0)
        #     if idx == n-1:
        #         return step
        #     step += 1
        #     for i in range(nums[idx]+1):
        #         if idx + i < n and (idx+i) not in visited:
        #             pq.append((idx+i, step))
        #             visited.add(idx+i)
        #     #print(idx)
        
        # 动态规划
        # 找在nums[i]可以的可以走的范围内，能够到达的最远位置
        # n = len(nums)
        # # maxpos是下步到达的最远位置，end为目前能到达的最远位置
        # maxPos, end, step = 0, 0, 0
        # # 因为总是能达到数组的最后一个位置，所以当遍历到n-1时肯定已经足够到达末尾了
        # for i in range(n-1):
        #     # maxPos一直在更新
        #     maxPos = max(maxPos, i+nums[i])
        #     # 当i遍历到当前能达到的最远距离，就使用maxPos更新能到达二最远距离，并增加一步
        #     if i == end:
        #         end = maxPos
        #         step += 1
        # return step

        # 从后往前找
        pos = len(nums) - 1
        step = 0
        while pos!=0:
            # 从左往右找保证了是距离最远的一步
            for i in range(pos):
                if i+nums[i] >= pos:
                    pos = i
                    step += 1
                    break
        return step