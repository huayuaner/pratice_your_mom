# 给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。
#
# 如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3,4,5]
# 输出：true
# 解释：任何 i < j < k 的三元组都满足题意
# 示例 2：
#
# 输入：nums = [5,4,3,2,1]
# 输出：false
# 解释：不存在满足题意的三元组
# 示例 3：
#
# 输入：nums = [2,1,5,0,4,6]
# 输出：true
# 解释：三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6
#
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        # left = [0]*n
        # left[0] = nums[0]
        ##建立左右序列，注意不要用min或max，徒增时间复杂度
        # for i in range(1, n):
        #     left[i] = min(left[i-1], nums[i])
        #     #left.append(min(nums[:i+1]))
        # right = [0]*n
        # right[n-1] = nums[n-1]
        # for i in range(n-2,-1, -1):
        #     #right.append(max(nums[i:]))
        #     right[i] = max(right[i+1], nums[i])

        # for i in range(1, n-1):
        #     if left[i-1]<nums[i]<right[i+1]:
        #         print(i)
        #         return True
        # return False
        first = nums[0]
        second = float("inf")
        #保存second最小的升序对
        for i in range(1, n):
            if nums[i] > second:
                return True
            if nums[i] > first:
                second = nums[i]

            else:
                first = nums[i]

        return False
