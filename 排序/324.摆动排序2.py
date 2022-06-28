# 给你一个整数数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。
#
# 你可以假设所有输入数组都可以得到满足题目要求的结果。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,5,1,1,6,4]
# 输出：[1,6,1,5,1,4]
# 解释：[1,4,1,5,1,6] 同样是符合题目要求的结果，可以被判题程序接受。
# 示例 2：
#
# 输入：nums = [1,3,2,2,3,1]
# 输出：[2,3,1,3,1,2]
#  
#
# 提示：
#
# 1 <= nums.length <= 5 * 104
# 0 <= nums[i] <= 5000
# 题目数据保证，对于给定的输入 nums ，总能产生满足题目要求的结果
#  
#
# 进阶：你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？
#
# class helper:
#     @staticmethod
#     def quickSelect(arr, l, r, index):
#         q = helper.randomPartition(arr,l,r)
#         if q == index:
#             return arr[q]
#         if q<index:
#             return helper.quickSelect(arr,q+1,r,index)
#         return helper.quickSelect(arr,l, q-1, index)
#     @staticmethod
#     def randomPartition(nums, l, r):
#         i = randint(l,r)
#         # 随机选择 一个当pivot
#         nums[i],nums[r] = nums[r], nums[i]
#         return helper.Partition(nums,l, r)
#     @staticmethod
#     def Partition(nums, l, r):
#         pivot = nums[r]
#         # 记录小于pivot的长度
#         i = l - 1
#         for j in range(l,r):
#             if nums[j] < pivot:
#                 i += 1
#                 nums[i], nums[j] = nums[j], nums[i]
#         nums[i+1], nums[r] = nums[r], nums[i+1]

#         return i + 1



class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 排序 + 反向更新
        # n = len(nums)
        # nums_sorted = sorted(nums)
        # mid = n // 2 if n%2==0 else n // 2 + 1
        # # print(mid)
        # # print(nums_sorted)
        # # left = nums_sorted[:mid]
        # # right = nums_sorted[mid:]
        # i = 0
        # idx = 0
        # while n-1-idx >= mid:
        #     nums[i] = nums_sorted[mid-1-idx]
        #     nums[i+1] = nums_sorted[n-1-idx]
        #     # print(nums_sorted[mid-1-i], nums_sorted[n-1-i])
        #     i += 2
        #     idx += 1

        # print(idx,mid)
        # if mid - idx - 1== 0:
            # print(111)
            # nums[n-1] = nums_sorted[0]

        # 3路切分
        # n = len(nums)
        # x = (n+1)//2
        # # pivot
        # target = helper.quickSelect(nums, 0, n-1, x-1)
        # # print(target)
        # k,i,j = 0,0,n-1
        # # 快排的分块
        # while i<=j:
        #     if nums[i] > target:
        #         while j > i and nums[j] > target:
        #             j -= 1
        #         nums[i], nums[j] = nums[j], nums[i]
        #         j -= 1
        #     if nums[i] < target:
        #         nums[k], nums[i] = nums[k], nums[i]
        #         k += 1
        #     i += 1
        # arr = nums.copy()
        # # print(arr)
        # j,k = x-1, n-1
        # for i in range(0,n,2):
        #     nums[i] = arr[j]
        #     if i+1<n:
        #         nums[i+1] = arr[k]
        #     j -= 1
        #     k -= 1
        # 使用迭代代替递归
        # 空间复杂度降到1
        def quickSelect(a: List[int], k: int) -> int:
            # seed(datetime.datetime.now())
            # shuffle(a)
            l, r = 0, len(a) - 1
            while l < r:
                pivot = a[l]
                i, j = l, r + 1
                while True:
                    i += 1
                    while i < r and a[i] < pivot:
                        i += 1
                    j -= 1
                    while j > l and a[j] > pivot:
                        j -= 1
                    if i >= j:
                        break
                    a[i], a[j] = a[j], a[i]
                a[l], a[j] = a[j], pivot
                if j == k:
                    break
                if j < k:
                    l = j + 1
                else:
                    r = j - 1
            return a[k]
        n = len(nums)
        x = (n + 1) // 2
        # seed(datetime.datetime.now())
        # target找到的是中位数的值
        # target = helper.quickSelect(nums, 0, n - 1, x - 1)
        target = quickSelect(nums, x - 1)
        # 下标映射，将空间降到 log N
        transAddress = lambda i: (2 * n - 2 * i - 1) % (n | 1)
        k, i, j = 0, 0, n - 1
        while k <= j:
            tk = transAddress(k)
            if nums[tk] > target:
                while j > k and nums[transAddress(j)] > target:
                    j -= 1
                tj = transAddress(j)
                nums[tk], nums[tj] = nums[tj], nums[tk]
                j -= 1
            if nums[tk] < target:
                ti = transAddress(i)
                nums[tk], nums[ti] = nums[ti], nums[tk]
                i += 1
            k += 1


        # k, i, j = 0, 0, n - 1
        # while k <= j:
        #     if nums[k] > target:
        #         while j > k and nums[j] > target:
        #             j -= 1
        #         nums[k], nums[j] = nums[j], nums[k]
        #         j -= 1
        #     if nums[k] < target:
        #         nums[k], nums[i] = nums[i], nums[k]
        #         i += 1
        #     k += 1
        # arr = nums.copy()
        # j, k = x - 1, n - 1
        # for i in range(0, n, 2):
        #     nums[i] = arr[j]
        #     if i + 1 < n:
        #         nums[i + 1] = arr[k]
        #     j -= 1
        #     k -= 1





