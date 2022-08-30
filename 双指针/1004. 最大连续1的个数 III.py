# 给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# 输出：6
# 解释：[1,1,1,0,0,1,1,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 6。
# 示例 2：
#
# 输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# 输出：10
# 解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 10。
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # 窗口中0的个数小于K
        # 所有这种窗口的宽度的最大值
        # l,r = 0,-1
        # n = len(nums)
        # cnt_0 = 0
        # ans = 0
        # while r < n:
        #     while r<n and cnt_0<=k:
        #         r += 1
        #         if r<n:
        #             cnt_0 += (nums[r] == 0)

        #     # print(l,r)
        #     ans = max(ans, r-l)
        #     while cnt_0 > k:
        #         cnt_0 -= (nums[l] == 0)
        #         l += 1
        # return ans

        # 很优雅的滑窗
        # 将k看作一种资源
        # 窗口只会单调增长
        l = r = 0
        n = len(nums)
        while r < n:
            # 右指针是把当前位包括进去
            # 如果是 0 资源k需要 -1
            if nums[r] == 0:
                k -= 1
            # 右指针 + 1
            r += 1
            # 如果资源用完 k<0
            # 左指针就要动了，要找回资源
            if k < 0:

                if nums[l] == 0:
                    k += 1
                l += 1
            # print(l,r)
        return r - l


