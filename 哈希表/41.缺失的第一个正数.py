给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
 

示例 1：

输入：nums = [1,2,0]
输出：3
示例 2：

输入：nums = [3,4,-1,1]
输出：2
示例 3：

输入：nums = [7,8,9,11,12]
输出：1
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # ans = 1
        # # 这一句复杂度超过了 N
        # nums.sort()
        # for num in nums:
        #     if num >0:
        #         if num > ans:
        #             return ans
        #         if num == ans:
        #             ans += 1
        #         if num < ans:
        #             continue
        # return ans

        # 不符合空间要求
        # Set = set(nums)
        # ans = 1
        # while ans in Set:
        #     ans += 1
        # return ans 

        # 原地哈希
        def __swap(nums, index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        # size = len(nums)
        # for i in range(size):
        #     # 3应该在2位置
        #     # 4应该在3位置
        #     while 0<nums[i]<=size and nums[i] != nums[nums[i]-1]:
        #         __swap(nums, i, nums[i]-1)
        #     #print(nums,i)
        # for i in range(size):
        #     if i+1 != nums[i]:
        #         return i+1
        # return size + 1
      

        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1



            
            
            