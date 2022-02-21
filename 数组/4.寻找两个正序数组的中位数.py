给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

 

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

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
        def findKthnumber(k):
            index1, index2 = 0, 0
            while True:
                # k/2-1 越界了 k是第k小的数
                if index1 == m:
                    return nums2[index2+k-1]
                if index2 == n:
                    return nums1[index1+k-1]
                # k==1返回数组头俩数的最小值
                if k==1:
                    return min(nums1[index1], nums2[index2])
                # 正常情况
                cur_index1 = min(index1 + k//2-1, m-1)
                cur_index2 = min(index2 + k//2-1, n-1)
                pivot1, pivot2 = nums1[cur_index1], nums2[cur_index2]
                if pivot1 <= pivot2:
                    # k减去curindex1和index1之间的数的数目
                    k -= cur_index1 - index1 + 1
                    index1 = cur_index1 + 1
                    
                else:
                    k -= cur_index2 - index2 + 1
                    index2 = cur_index2 + 1
        m, n = len(nums1), len(nums2)
        total = m+n
        if total%2==1:
            return findKthnumber(total//2+1)
        else:
             return (findKthnumber(total//2+1)+findKthnumber(total//2))/2
                    

        