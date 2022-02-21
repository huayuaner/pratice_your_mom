给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。

请你找出并返回只出现一次的那个数。

你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。

 

示例 1:

输入: nums = [1,1,2,3,3,4,4,8,8]
输出: 2
示例 2:

输入: nums =  [3,3,7,7,10,11,11]
输出: 10
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # def divide(left,right):
        #     if left > right:
        #         return -1
        #     if left == right:
        #         return nums[left]
        #     # if right - left + 1 < 3:
        #     #     return -1  
        #     mid = left + (right-left)//2
        #     if nums[mid] != nums[mid-1] and  nums[mid] != nums[mid+1]:
        #         #print(left,right,mid)
        #         return nums[mid]
        #     elif nums[mid] == nums[mid-1]:
        #         return divide(left,mid-2) if divide(left,mid-2)!=-1 else divide(mid+1,right)
        #     elif nums[mid] == nums[mid+1]:
        #         return divide(left,mid-1) if divide(left,mid-1)!=-1 else divide(mid+2,right)
        # if len(nums)<2:
        #     return nums[0]
        # return divide(0, len(nums)-1)

        # 奇偶性
        # 整个数组长度为奇数，其中target左右两边长度都是偶数
        # 对于target左边的数，如果下边是偶数，那么跟后一个数相同；如果是奇数，那么跟前一个数相同
        # 所以我们可以是用二分法找mid，mid满足此规则则mid在target左边，否则在右边
        
        # L, R = 0, len(nums)-1
        
        # while L < R:
        #     mid = L+(R-L)//2
        #     # mid^1是按位异或，如果mid是偶数，则会+1；奇数-1
        #     #print(L, R,mid)
        #     if nums[mid] == nums[mid^1]:
        #         L = mid+1
        #     else:
        #         R = mid
        # # 最后左右会收敛成一个数，而那时候mid不再更新，所以返回L
        # return nums[L] 

        # 偶数下标的二分
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            # 奇数-1 偶数 -0
            mid -= mid & 1
            # 与上面一个意思，奇数和前一个比，偶数和后一个比
            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid
        return nums[low]



