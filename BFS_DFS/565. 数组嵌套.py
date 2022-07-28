# 索引从0开始长度为N的数组A，包含0到N - 1的所有整数。找到最大的集合S并返回其大小，其中 S[i] = {A[i], A[A[i]], A[A[A[i]]], ... }且遵守以下的规则。
#
# 假设选择索引为i的元素A[i]为S的第一个元素，S的下一个元素应该是A[A[i]]，之后是A[A[A[i]]]... 以此类推，不断添加直到S出现重复的元素。
#
#  
#
# 示例 1:
#
# 输入: A = [5,4,0,3,1,6,2]
# 输出: 4
# 解释:
# A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.
#
# 其中一种最长的 S[K]:
# S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # seen = set()
        # ans = 1
        # for i,num in enumerate(nums):
        #     if num in seen: continue
        #     length = 1
        #     vis = set()
        #     vis.add(i)
        #     while 1:
        #         # print(num)
        #         i = nums[i]

        #         if i in vis:break
        #         vis.add(i)
        #         seen.add(i)
        #         length += 1
        #     # print()
        #     ans = max(ans,length)
        # return ans

        # 优化写法
        # n = len(nums)
        # vis = [False] * n
        # ans = 1
        # for i,num in enumerate(nums):
        #     length = 0
        #     while not vis[i]:
        #         vis[i] = True
        #         i = nums[i]
        #         length += 1
        #     ans = max(ans, length)
        # return ans

        # 空间优化写法
        n = len(nums)
        # vis = [False] * n
        ans = 1
        for i, num in enumerate(nums):
            length = 0
            while nums[i] != n:
                nex = nums[i]
                nums[i] = n
                i = nex
                length += 1
                # print(nums)
            ans = max(ans, length)
        return ans