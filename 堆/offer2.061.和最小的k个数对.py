# 给定两个以升序排列的整数数组 nums1 和 nums2 , 以及一个整数 k 。
#
# 定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。
#
# 请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。
#
#  
#
# 示例 1:
#
# 输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# 输出: [1,2],[1,4],[1,6]
# 解释: 返回序列中的前 3 对数：
#     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# 示例 2:
#
# 输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# 输出: [1,1],[1,1]
# 解释: 返回序列中的前 2 对数：
#      [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# 示例 3:
#
# 输入: nums1 = [1,2], nums2 = [3], k = 3
# 输出: [1,3],[2,3]
# 解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]
#
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # 堆
        m, n = len(nums1), len(nums2)
        ans = []
        # 用nums1[i] + nums2[0],i,0 的元组存入list
        # 由于两个都是有序的，所以list中的内容也会是有序的
        hq = [(nums1[i] + nums2[0], i, 0) for i in range(min(m, k))]
        while hq and k:
            # 每次弹出堆中最小值，获取其中的i,j
            _, i, j = heapq.heappop(hq)
            ans.append([nums1[i], nums2[j]])
            k -= 1
            # 如果当前的j不是最后一个那么就将当前i和j+1的组合放入堆中
            if j + 1 < n:
                heapq.heappush(hq, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans

