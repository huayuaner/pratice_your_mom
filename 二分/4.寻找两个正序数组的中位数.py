# <<<<<<< HEAD
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
#
# 算法的时间复杂度应该为 O(log (m+n)) 。
#
#  
#
# 示例 1：
#
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
# 示例 2：
#
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # def merge(n1,n2):
        #     ans = []
        #     while n1 and n2:
        #         if n1[0] < n2[0]:
        #             ans.append(n1.pop(0))
        #         else:
        #             ans.append(n2.pop(0))
        #     if n1:
        #         ans.extend(n1)
        #     if n2:
        #         ans.extend(n2)
        #     return ans
        # tmp = merge(nums1,nums2)
        
        # if (n:=len(tmp))%2 == 1:
            
        #     return tmp[n//2]
        # else:
        #     return (tmp[n//2-1]+tmp[n//2])/2

        # 二分
        # def findKthnumber(k):
        #     index1, index2 = 0, 0
        #     while True:
        #         # k/2-1 越界了 k是第k小的数
        #         if index1 == m:
        #             return nums2[index2+k-1]
        #         if index2 == n:
        #             return nums1[index1+k-1]
        #         # k==1返回数组头俩数的最小值
        #         if k==1:
        #             return min(nums1[index1], nums2[index2])
        #         # 正常情况
        #         cur_index1 = min(index1 + k//2-1, m-1)
        #         cur_index2 = min(index2 + k//2-1, n-1)
        #         pivot1, pivot2 = nums1[cur_index1], nums2[cur_index2]
        #         if pivot1 <= pivot2:
        #             # k减去curindex1和index1之间的数的数目
        #             k -= cur_index1 - index1 + 1
        #             index1 = cur_index1 + 1
        #
        #         else:
        #             k -= cur_index2 - index2 + 1
        #             index2 = cur_index2 + 1
        # m, n = len(nums1), len(nums2)
        # total = m+n
        # if total%2==1:
        #     return findKthnumber(total//2+1)
        # else:
        #      return (findKthnumber(total//2+1)+findKthnumber(total//2))/2
        # 二分
        if len(nums1)>len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        m,n = len(nums1),len(nums2)
        left, right = 0, m
        # 第一\二部分的最小值
        median1,median2 = 0,0
        while left <= right:
            # 当i为该值时，为了保证len(part_left)>=len(part_right)
            # j就应该这样取值
            i = (left+right) //2
            j = (m+n+1)//2 - i
            # print(i,j,nums1, nums2)
            # 当划分方式在最左和最右的情况，赋予无穷的值，方便后续比较
            nums_im1 = float('-inf') if i==0 else nums1[i-1]
            nums_i = float('inf') if i == m else nums1[i]
            nums_jm1 = float('-inf') if j==0 else nums2[j-1]
            nums_j = float('inf') if j == n else nums2[j]
            # 合法情况
            # 依据推理，当nums1[i-1] <= nums2[j]，而由二分法来逼近nums[j-1] <= nums[i]（如果i是最优位置，那一定满足两个条件，而我们通过二分找到最优位置，顺便就满足了第二个条件）
            # 也就是是合法情况
            if nums_im1 <= nums_j:
                median1, median2 = max(nums_im1, nums_jm1), min(nums_i,nums_j)
                left = i + 1
            else:
                right = i - 1
        return (median1+median2)/2 if (m+n)%2==0 else median1
                    


        