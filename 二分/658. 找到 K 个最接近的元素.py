# 给定一个 排序好 的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。
#
# 整数 a 比整数 b 更接近 x 需要满足：
#
# |a - x| < |b - x| 或者
# |a - x| == |b - x| 且 a < b
#  
#
# 示例 1：
#
# 输入：arr = [1,2,3,4,5], k = 4, x = 3
# 输出：[1,2,3,4]
# 示例 2：
#
# 输入：arr = [1,2,3,4,5], k = 4, x = -1
# 输出：[1,2,3,4]
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 特判
        #         if x >= arr[-1]:
        #             return arr[-k:]

        #         if x <= arr[0]:
        #             return arr[:k]
        #         # 二分找到大于x的最小的数
        #         n = len(arr)
        #         l,r = 0,n
        #         while l<r:
        #             m = l+(r-l)//2
        #             if arr[m] < x:
        #                 l = m + 1
        #             else:
        #                 r = m

        #         # left = []
        #         # right = []
        #         p1,p2 = l-1, l
        #         while p1 >= 0 and p2 < n and k:
        #             if abs(x - arr[p1]) <= abs(x-arr[p2]):
        #                 # left.append(arr[p1])
        #                 p1 -= 1
        #             else:
        #                 # right.append(arr[p2])
        #                 p2 += 1
        #             k -= 1
        #         if k == 0:
        #             return arr[p1+1:p2]
        #         elif p1 >= 0:
        #             if p1 >= k:
        #                 return arr[p1-k+1:p2]
        #             else:
        #                 return arr[:p2+(k-p1)]
        #         else:
        #             return arr[:p2+k]

        # 排序
        # arr.sort(key = lambda n: abs(n-x))
        # return sorted(arr[:k])

        # 二分(优雅版)
        # right = bisect_right(arr, x)
        # n = len(arr)
        # left = right - 1
        # for _ in range(k):
        #     if right == n:
        #         left -= 1
        #     elif left == -1:
        #         right += 1
        #     else:
        #         if x-arr[left] <= arr[right]-x:
        #             left -= 1
        #         else:
        #             right += 1
        # return arr[left+1:right]

        # 二分
        l, r = 0, len(arr) - k
        while l < r:
            m = l + (r - l) // 2
            # 前一个单减，后一个单增
            # 找交点
            # print(m, arr[m+k])
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
                # print(arr[l])
        # if l>0 and abs(arr[l-1]-x) == abs(arr[l+k-1]-x):
        # l -= 1
        return arr[l:l + k]


