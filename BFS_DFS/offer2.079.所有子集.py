# 给定一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 示例 2：
#
# 输入：nums = [0]
# 输出：[[],[0]]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        lis = []
        n = len(nums)

        def dfs(lis, pos):
            if pos > n - 1:
                # print(lis)
                # 如果这里不用lis[:]的话 相当于ans.append了lis这个对象，所以之后lis.pop执行后，ans中的lis也会改变
                # 呜呜呜太难了
                ans.append(lis[:])
                # print(lis,ans)
                return
            dfs(lis, pos + 1)
            # 使用dfs(lis+[nums[i]],pos+1)相当于产生了一个新对象，不再是lis了
            lis.append(nums[pos])
            dfs(lis, pos + 1)
            lis.pop()

        dfs([], 0)
        return ans