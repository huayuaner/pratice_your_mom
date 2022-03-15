# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
#
#  
#
# 示例 1:
#
# 输入: [0,1,3]
# 输出: 2
# 示例 2:
#
# 输入: [0,1,2,3,4,5,6,7,9]
# 输出: 8

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # tmp = [num for num in range(n+1)]
        # for i,num in enumerate(tmp):
        #     if i!=n and num != nums[i]:
        #         return num
        # return tmp[-1]

        # for idx, num in enumerate(nums):
        #     if num != idx:
        #         return num -1
        # return len(nums)

        # 二分
        # r如果中点的值等于下标值就在[m+1:r]，不等于就在[l:m-1]
        l, r = 0, len(nums)-1
        # 当闭区间[l,r]为空跳出
        # l指向右子数组首位元素，r指向左子树组的末尾元素，因此返回l即可
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == m:
                l = m+1
            else:
                r = m-1
        return l
