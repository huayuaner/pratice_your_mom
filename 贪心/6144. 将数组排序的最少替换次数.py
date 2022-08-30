# 给你一个下表从 0 开始的整数数组 nums 。每次操作中，你可以将数组中任何一个元素替换为 任意两个 和为该元素的数字。
#
# 比方说，nums = [5,6,7] 。一次操作中，我们可以将 nums[1] 替换成 2 和 4 ，将 nums 转变成 [5,2,4,7] 。
# 请你执行上述操作，将数组变成元素按 非递减 顺序排列的数组，并返回所需的最少操作次数。
#
#  
#
# 示例 1：
#
# 输入：nums = [3,9,3]
# 输出：2
# 解释：以下是将数组变成非递减顺序的步骤：
# - [3,9,3] ，将9 变成 3 和 6 ，得到数组 [3,3,6,3]
# - [3,3,6,3] ，将 6 变成 3 和 3 ，得到数组 [3,3,3,3,3]
# 总共需要 2 步将数组变成非递减有序，所以我们返回 2 。
# 示例 2：
#
# 输入：nums = [1,2,3,4,5]
# 输出：0
# 解释：数组已经是非递减顺序，所以我们返回 0 。
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        # 1. 无法拆出更大的数，否则无法递增
        # 2. 数字不能变大，只能不变或者变小
        # 3. 最后一个数一定是最大的！
        # 4. 最后一个数需要拆吗？ 没必要
        # 5. 往前遍历
        #   维护当前拆出的最小值
        #   如果大于当前最小值，必须拆分
        # 6. 拆分要求：
        #     1)最大值 <= 当前最小值（cur_m）
        #           假设nums[i]拆分成x份
        #           nums[i] = n1+n2+...+nx <= cur_m + cur_m +...+ cur_m  =>  nums[i] <= x*cur_m => x要尽量小(操作数尽量小) x = nums[i]/cur_m(向上取整)
        #     2)最小值 尽量大
        #           尽可能分的均匀 nums[i] // x
        #     操作次数 x-1
        # 贪心
        # cur_min = nums[-1]
        # ans = 0
        # n = len(nums)
        # for i in range(n-2, -1, -1):
        #     if nums[i] <=cur_min:
        #         cur_min = nums[i]
        #     else:
        #         x = (nums[i] + cur_min - 1) // cur_min
        #         ans += x-1
        #         cur_min = nums[i]//x
        # return ans

        m = nums[-1]
        ans = 0
        for n in reversed(nums):
            k = (n-1)//m
            ans += k
            m = n//(k+1)
        return ans

