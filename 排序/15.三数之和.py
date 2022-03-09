# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#  
#
# 示例 1：
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 示例 2：
#
# 输入：nums = []
# 输出：[]
# 示例 3：
#
# 输入：nums = [0]
# 输出：[]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if nums[i]>0:
                return res
            if i>0 and nums[i] == nums[i-1]:
                continue
            # 因为从i开始会重复计算i位置的值
            L = i+1
            R = n-1
            while L<R:
                if nums[i]+nums[L]+nums[R] == 0:
                    res.append([nums[i],nums[L],nums[R]])
                    # 跳过重复数防止进入相同的结果
                    while nums[R] == nums[R-1] and L<R:
                        R -= 1
                    while nums[L] == nums[L+1] and L<R:
                        L += 1
                    R-=1
                    L+=1
                # 大于0说明右边的数太大
                elif nums[i]+nums[L]+nums[R] > 0:
                    R -= 1
                # 说明左边数太小
                else:
                    L += 1
        return res