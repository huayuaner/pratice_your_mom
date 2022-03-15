# 给你一个整数数组 nums ，请你找出 nums 子集 按位或 可能得到的 最大值 ，并返回按位或能得到最大值的 不同非空子集的数目 。
#
# 如果数组 a 可以由数组 b 删除一些元素（或不删除）得到，则认为数组 a 是数组 b 的一个 子集 。如果选中的元素下标位置不一样，则认为两个子集 不同 。
#
# 对数组 a 执行 按位或 ，结果等于 a[0] OR a[1] OR ... OR a[a.length - 1]（下标从 0 开始）。
#
#  
#
# 示例 1：
#
# 输入：nums = [3,1]
# 输出：2
# 解释：子集按位或能得到的最大值是 3 。有 2 个子集按位或可以得到 3 ：
# - [3]
# - [3,1]
# 示例 2：
#
# 输入：nums = [2,2,2]
# 输出：7
# 解释：[2,2,2] 的所有非空子集的按位或都可以得到 2 。总共有 23 - 1 = 7 个子集。
# 示例 3：
#
# 输入：nums = [3,2,1,5]
# 输出：6
# 解释：子集按位或可能的最大值是 7 。有 6 个子集按位或可以得到 7 ：
# - [3,5]
# - [3,1,5]
# - [3,2,5]
# - [3,2,1,5]
# - [2,5]
# - [2,1,5]

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # dfs
        # 记录计数次数 和 最大值
        # cnt = 0
        # maxval = 0
        # def dfs(pos, orval):
        #     # 当遍历到结尾
        #     if pos == len(nums):
        #         nonlocal cnt, maxval
        #         # 查看当前值和最大值的差别并做相应操作
        #         if orval > maxval:
        #             maxval = orval
        #             cnt += 1
        #         elif orval == maxval:
        #             cnt += 1
        #         # 记得返回
        #         return
        #     #print(pos)
        #     # 下一个有可能选有可能不选
        #     dfs(pos+1, orval|nums[pos])
        #     dfs(pos+1, orval)
        # dfs(0,0)
        # return cnt

        # maxval, cnt = 0, 0
        # n = len(nums)
        # mask = (1<<n)
        # for s in range(mask):
        #     tmp = 0
        #     for i in range(n):
        #         if s&(1<<i):
        #             tmp |= nums[i]
        #     if tmp > maxval:
        #         maxval = tmp
        #         cnt = 1
        #     elif tmp == maxval:
        #         cnt += 1
        # return cnt

        # 记录每个值出现的次数
        dp = Counter([0])
        for num in nums:
            # 防止过程中改变dp，使用了copy
            for k,v in dp.copy().items():
                dp[k|num] += v
        return dp[max(dp)]