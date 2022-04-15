# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 示例 2：
#
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
# 示例 3：
#
# 输入：nums = [1]
# 输出：[[1]]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def dfs(pos):
            if pos == n - 1:
                nonlocal ans
                ans.append(nums[:])
                return
            for i in range(pos, n):
                nums[pos], nums[i] = nums[i], nums[pos]
                dfs(pos + 1)
                nums[pos], nums[i] = nums[i], nums[pos]

        dfs(0)
        return ans

