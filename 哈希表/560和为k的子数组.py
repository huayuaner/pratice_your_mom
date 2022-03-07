给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。

 

示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：

输入：nums = [1,2,3], k = 3
输出：2
 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 暴力 N^3
        # ans = 0
        # n = len(nums)
        # for left in range(0,n):
        #     for right in range(left,n):
        #         total = sum(nums[left:right+1])
        #         # for i in range(left,right+1):
        #         #     total += nums[i]
                    
        #         if total == k:
        #             ans += 1
        # return ans

        # 暴力 N^2
        # ans = 0
        # n = len(nums)
        # for i in range(n):
        #     total = 0
        #     for j in range(i,n):
        #         total += nums[j]
        #         if total == k:
        #             ans += 1
        # return ans

        # 哈希表+前缀和
        pre = 0
        HashMap = Counter()
        HashMap[pre] += 1
        ans = 0
        for num in nums:
            pre += num
            if pre-k in HashMap:
                ans += HashMap[pre-k]
            HashMap[pre] += 1
        return ans



