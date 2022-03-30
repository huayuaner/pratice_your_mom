# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
#
#  
# 示例 1：
#
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
# 示例 2：
#
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
# 示例 3：
#
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for num in nums:
            if not d or num>d[-1]:
                d.append(num)
            # 如果我们希望得到最长递增的子序列，那么我们需要每个数之间增加的更少
            # 当遇到小于末尾的数，我们找到第一个小于这个数的d[k]，k+1换成这个数
            # 由于d是严格单增序列，所以可以使用二分
            else:
                l, r = 0, len(d)-1
                # loc = r
                while l<=r:
                    m = l+(r-l)//2
                    if d[m] >= num:
                        loc = m
                        r = m-1
                    else:
                        l = m+1
                d[loc] = num
            # print(d)
        return len(d)