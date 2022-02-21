给定一个长度为 n 的整数数组和一个目标值 target ，寻找能够使条件 nums[i] + nums[j] + nums[k] < target 成立的三元组  i, j, k 个数（0 <= i < j < k < n）。

 

示例 1：

输入: nums = [-2,0,1,3], target = 2
输出: 2 
解释: 因为一共有两个三元组满足累加和小于 2:
     [-2,0,1]
     [-2,0,3]
示例 2：

输入: nums = [], target = 0
输出: 0 
示例 3：

输入: nums = [0], target = 0
输出: 0 
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums)<3:
            return 0
        ans = 0
        nums.sort()
        n = len(nums)
        for i in range(n):
            L, R = i+1, n-1
            while L<R:
                if (total := nums[i] + nums[L] + nums[R]) < target:
                    ans += R-L
                    L += 1
                else:
                    R -=1
                #print(ans,L, R)
        return ans
                
