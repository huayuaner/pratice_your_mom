# 给你一个整数数组 nums，请你将该数组升序排列。
#
#  
#
# 示例 1：
#
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
# 示例 2：
#
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # return sorted(nums)
        # 归并排序，递归版
        # def process(nums, L, R):
        #     if L == R:
        #         return
        #     mid = L + (R-L)//2
        #     process(nums, L, mid)
        #     process(nums, mid+1, R)
        #     merge(nums, L, mid, R)

        # 归并排序，迭代版
        # def process(nums):
        #     if not nums or len(nums)<2:
        #         return
        #     N = len(nums)
        #     #每次归并的左边子组大小（总大小为2）
        #     mergesize = 1
        #     while mergesize<N:
        #         #记录左边点的位置
        #         L = 0
        #         while(L<N):
        #             mid = L + mergesize -1
        #             #说明左子组小于等于当前需排列的一半长度，而这一半在上次迭代中已经排序好了，说明这一段排序完成
        #             if mid >= N:
        #                 break
        #             R = min(mid+mergesize, N-1)
        #             merge(nums, L, mid, R)
        #             L = R+1
        #         #防止溢出，当N接近系统内部最大值，mergesize*2有可能溢出
        #         if mergesize > N/2:
        #             break
        #         #排序大小变成2倍，位运算快
        #         mergesize <<= 1
        # def merge(nums, L, mid, R):
        #     i,j = L, mid+1
        #     ans = []
        #     while i<=mid and j <=R:
        #         if nums[i]<=nums[j]:
        #             ans.append(nums[i])
        #             i += 1
        #         else:
        #             ans.append(nums[j])
        #             j += 1
        #     ans.extend(nums[i:mid+1] if j > R else nums[j:R+1])
        #     nums[L:R+1] = ans
        # process(nums)
        # return nums

        # 快排
        # def process(nums, L ,R):
        #     if L > R:
        #         return
        #     i = randint(L,R)
        #     nums[R], nums[i] = nums[i], nums[R]
        #     equalArea = netherlandsFlag(nums, L, R)
        #     process(nums, L, equalArea[0]-1)
        #     process(nums, equalArea[1]+1, R)
        # def netherlandsFlag(nums, L, R):
        #     if L>R:
        #         return
        #     if L == R:
        #         return (L,R)
        #     more = R
        #     less = L - 1
        #     index = L
        #     while index < more:
        #         if nums[index] < nums[R]:
        #             nums[less+1], nums[index] = nums[index], nums[less+1]
        #             less += 1
        #             index += 1
        #         elif nums[index] == nums[R]:
        #             index += 1
        #         else:
        #             nums[index], nums[more-1] = nums[more-1], nums[index]
        #             more -= 1
        #     nums[R], nums[more] = nums[more], nums[R]
        #    # print(nums)
        #     return (less+1, more)
        # process(nums, 0, len(nums)-1)
        # return nums

        # 堆排序
        def heapSort(nums):
            if not nums or len(nums) < 2:
                return
            n = len(nums)
            # 遍历，让nums变成大根堆数组 N*log N
            # for i in range(n):  #N
            # heapInsert(nums, i) #log N
            for i in range(n - 1, -1, -1):  #  N
                heapify(nums, i, n)

            # 首位交换
            nums[0], nums[n - 1] = nums[n - 1], nums[0]
            # 让heapsize-1，让之后的结果不移动它，也就是找到了位置
            n -= 1
            # 复杂度n*logn
            while n > 0:  # n
                heapify(nums, 0, n)  # logn
                nums[0], nums[n - 1] = nums[n - 1], nums[0]
                n -= 1

        # 将更换第i个元素的位置，使得nums保持大根堆
        def heapInsert(nums, i):
            while nums[int(i - 1 / 2)] < nums[i]:
                nums[int(i - 1 / 2)], nums[i] = nums[i], nums[int(i - 1 / 2)]
                i = int(i - 1 / 2)

        # 把index位置的数字沉下去，完成大根堆
        def heapify(nums, index, heapsize):
            # 左子树的位置
            L = index * 2 + 1
            while L < heapsize:
                largest = L + 1 if L + 1 < heapsize and nums[L] < nums[L + 1] else L
                largest = index if nums[index] > nums[largest] else largest
                if largest == index:
                    break
                nums[largest], nums[index] = nums[index], nums[largest]
                index = largest
                L = 2 * index + 1

        heapSort(nums)
        return nums




