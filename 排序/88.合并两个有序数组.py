给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

 

示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。
示例 3：

输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。

import bisect
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 时间 (m+n) log (m+n)
        # nums1[m:] = nums2
        # return nums1.sort()

        # 正向归并
        # 时间 m+n 空间 n+m
        # tmp = []
        # i, j=0, 0
        # while i<m and j<n:
        #     if nums1[i] <= nums2[j]:
        #         tmp.append(nums1[i])
        #         i += 1
        #     else:
        #         tmp.append(nums2[j])
        #         j += 1
        # if i<m:
        #     tmp.extend(nums1[i:m])
        # if j<n:
        #     tmp.extend(nums2[j:])
        # nums1[:] = tmp
        # print(tmp)
        # return nums1

        # 从后往前遍历
        i,j = m-1, n-1
        tail = n+m-1
        while i >= 0 or j >=0:
            if i == -1:
                nums1[:j+1] = nums2[:j+1]
                break
            elif j==-1:
                 #nums1[:i+1] = nums1[:i+1]
                 break
            elif nums1[i] >= nums2[j]:
                nums1[tail] = nums1[i]
                i-=1
            elif nums1[i] < nums2[j]:
                nums1[tail] = nums2[j]
                j-=1
            tail -= 1
        return nums1

        
            


        

