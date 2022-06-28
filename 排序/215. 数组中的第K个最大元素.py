# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
#
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
#  
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 示例 2:
#
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
class Helper:
    @staticmethod
    def quickSelect(arr:list, l:int, r:int, index:int)->int:
        q = Helper.randomPartition(arr, l, r)
        if q == index:
            return arr[q]
        if q<index:
            return Helper.quickSelect(arr,q+1, r,index)
        return Helper.quickSelect(arr, l, q-1,index)
    @staticmethod
    def randomPartition(nums, l,r):
        i = randint(l,r)
        nums[i], nums[r] = nums[r], nums[i]
        return Helper.Partition(nums,l,r)
    @staticmethod
    def Partition(nums, l, r):
        pivot = nums[r]
        while l<r:
            # 过滤掉合法的
            # 从左边开始，因为pivot记录的是右边，这样nums[r]是可以被覆盖掉的
            while l<r and nums[l] < pivot:
                l += 1
            # 把左边不合法的值换到右边
            nums[r] = nums[l]
            while l<r and nums[r] >= pivot:
                r -= 1
            # 把右边不合法的值换到左边
            nums[l] = nums[r]
        nums[l] = pivot
        return l

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        return Helper.quickSelect(nums, 0, n-1, n-k)