# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
#
# 返回这三个数的和。
#
# 假定每组输入只存在恰好一个解。
#
#  
#
# 示例 1：
#
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
# 示例 2：
#
# 输入：nums = [0,0,0], target = 1
# 输出：0
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float("inf")
        nums.sort()
        n = len(nums)
        for i in range(n):
            left, right = i+1, n-1
            while left<right:
                #print(i,left,right)
                total = nums[i]+nums[left]+nums[right]
                #print(total)
                res = total if abs(total-target)<abs(res-target) else res
                if total == target:
                    return target
                elif total < target:
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    left += 1
                else:
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
        return res