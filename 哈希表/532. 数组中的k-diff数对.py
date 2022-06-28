# 给定一个整数数组和一个整数 k，你需要在数组里找到 不同的 k-diff 数对，并返回不同的 k-diff 数对 的数目。
#
# 这里将 k-diff 数对定义为一个整数对 (nums[i], nums[j])，并满足下述全部条件：
#
# 0 <= i < j < nums.length
# |nums[i] - nums[j]| == k
# 注意，|val| 表示 val 的绝对值。
#
#  
#
# 示例 1：
#
# 输入：nums = [3, 1, 4, 1, 5], k = 2
# 输出：2
# 解释：数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
# 尽管数组中有两个1，但我们只应返回不同的数对的数量。
# 示例 2：
#
# 输入：nums = [1, 2, 3, 4, 5], k = 1
# 输出：4
# 解释：数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5)。
# 示例 3：
#
# 输入：nums = [1, 3, 1, 5, 4], k = 0
# 输出：1
# 解释：数组中只有一个 0-diff 数对，(1, 1)。

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # 哈希表去重
        # seen,ans = set(),set()
        # for num in nums:
        #     if num-k in seen:
        #         ans.add(num-k)
        #     if num+k in seen:
        #         ans.add(num)
        #     seen.add(num)
        # return len(ans)

        # 排序 + 双指针
        nums.sort()
        n = len(nums)
        ans = j = 0
        for i in range(n):
            # 左指针去重
            if i == 0 or nums[i] != nums[i - 1]:
                while j < n and (nums[i] + k > nums[j] or j <= i):
                    j += 1
                if j >= n:
                    break
                if j < n and nums[i] + k == nums[j]:
                    ans += 1

        return ans










