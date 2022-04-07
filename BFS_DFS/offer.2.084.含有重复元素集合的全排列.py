# 给定一个可包含重复数字的整数集合 nums ，按任意顺序 返回它所有不重复的全排列。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# 示例 2：
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def dfs(pos, nums):
            if pos == n-1:
                nonlocal ans
                ans.append(nums[:])
            seen = set()
            for i in range(pos,n):
                if nums[i] in seen: continue
                seen.add(nums[i])
                nums[pos], nums[i] = nums[i], nums[pos]
                dfs(pos+1, nums)
                nums[pos], nums[i] = nums[i], nums[pos]
        ans = []
        dfs(0, nums)
        return ans
