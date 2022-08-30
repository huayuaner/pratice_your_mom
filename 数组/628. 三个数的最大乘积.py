# 给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # nums.sort(reverse=True)

        # return max(nums[0]*nums[1]*nums[2], nums[0]*nums[-1]*nums[-2])

        # 线性扫描
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num

            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
        return max(max1 * max2 * max3, min1 * min2 * max1)
