# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
#
#  
#
# 示例 1:
#
# 输入: [7,5,6,4]
# 输出: 5
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # 归并
        if not nums:
            return 0
        self.res = 0

        def process(nums, l, r):
            if l == r:
                return
            m = l + (r - l) // 2
            process(nums, l, m)
            process(nums, m + 1, r)
            merge(nums, l, m, r)

        def merge(nums, l, m, r):
            ans = []
            i, j = l, m + 1
            while i <= m and j <= r:
                if nums[i] <= nums[j]:
                    ans.append(nums[i])
                    i += 1
                else:
                    ans.append(nums[j])
                    self.res += m - i + 1
                    j += 1
            ans.extend(nums[i:m + 1] if j > r else nums[j:r + 1])
            nums[l:r + 1] = ans

        process(nums, 0, len(nums) - 1)
        return self.res