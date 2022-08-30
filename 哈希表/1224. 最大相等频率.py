# 给你一个正整数数组 nums，请你帮忙从该数组中找出能满足下面要求的 最长 前缀，并返回该前缀的长度：
#
# 从前缀中 恰好删除一个 元素后，剩下每个数字的出现次数都相同。
# 如果删除这个元素后没有剩余元素存在，仍可认为每个数字都具有相同的出现次数（也就是 0 次）。
#
#  
#
# 示例 1：
#
# 输入：nums = [2,2,1,1,5,3,3,5]
# 输出：7
# 解释：对于长度为 7 的子数组 [2,2,1,1,5,3,3]，如果我们从中删去 nums[4] = 5，就可以得到 [2,2,1,1,3,3]，里面每个数字都出现了两次。
# 示例 2：
#
# 输入：nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
# 输出：13
from collections import Counter


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        # 双哈希
        # 记录每个字符出现的次数
        cnts1 = Counter()
        # 记录每个字符出现次数的次数
        cnts2 = Counter()
        # 记录每个字符出现的最大次数
        max_cnt = ans = 0
        for i, num in enumerate(nums):
            cnts1[num] += 1
            max_cnt = max(max_cnt, cnts1[num])
            # if cnts1[num] > 1:
            # 更新出现次数
            cnts2[cnts1[num] - 1] -= 1
            cnts2[cnts1[num]] += 1
            # print(cnts1, cnts2,max_cnt,(cnts2[max_cnt-1]*(max_cnt), i+1-max_cnt))
            if max_cnt == 1 or (cnts2[max_cnt - 1] * (max_cnt - 1) == i + 1 - max_cnt) or (
                    cnts2[max_cnt] * max_cnt == i and cnts2[1] == 1):
                ans = i + 1
        return ans









