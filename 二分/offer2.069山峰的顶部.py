# 符合下列属性的数组 arr 称为 山峰数组（山脉数组） ：
#
# arr.length >= 3
# 存在 i（0 < i < arr.length - 1）使得：
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# 给定由整数组成的山峰数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i ，即山峰顶部。
#
#  
#
# 示例 1：
#
# 输入：arr = [0,1,0]
# 输出：1
# 示例 2：
#
# 输入：arr = [1,3,5,4,2]
# 输出：2
# 示例 3：
#
# 输入：arr = [0,10,5,2]
# 输出：1
# 示例 4：
#
# 输入：arr = [3,4,5,1]
# 输出：2
# 示例 5：
#
# 输入：arr = [24,69,100,99,79,78,67,36,26,19]
# 输出：2

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # 二分
        l, r = 0, len(arr) - 1
        # ans = 0
        while l <= r:
            m = l + (r - l) // 2
            # 这种情况m可能是峰，所以要判断一下
            if arr[m] > arr[m + 1]:
                r = m - 1
                # ans = m
                if arr[r] < arr[m]:
                    return m
            # 这种情况 m 必然不是峰
            else:
                l = m + 1

        return l

        # n = len(arr)
        # left, right, ans = 1, n - 2, 0

        # while left <= right:
        #     mid = (left + right) // 2
        #     if arr[mid] > arr[mid + 1]:
        #         ans = mid
        #         right = mid - 1
        #     else:
        #         left = mid + 1

        # return ans

