# 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
#
# 示例:
#
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # if not nums:
        #     return []
        # l, r = 0, k-1
        # n = len(nums)

        # ans = [max(nums[l:r+1])]
        # l+= 1
        # r+= 1
        # while r<n:
        #     if ans[-1] == nums[l-1]:
        #         ans.append(max(nums[l:r+1]))
        #     else:
        #         if ans[-1] >= nums[r]:
        #             ans.append(ans[-1])
        #         else:
        #             ans.append(nums[r])
        #     l+=1
        #     r+=1
        # return ans

        # 堆
        # if not nums:
        #     return []
        # l, r = 0, k-1
        # n = len(nums)
        # # 加入堆记录数值大小与下标信息
        # heap = [(-nums[i],i) for i in range(l, r+1)]
        # heapify(heap)
        # ans = [-heap[0][0]]
        # l += 1
        # r += 1
        # while r < n:
        #     heappush(heap, (-nums[r],r))
        #     while heap[0][1] < l:
        #         heappop(heap)
        #     ans.append(-heap[0][0])
        #     l += 1
        #     r += 1
        # return ans

        # 单调队列
        if not nums:
            return []
        l, r = 0, k - 1
        n = len(nums)
        # 加入堆记录数值大小与下标信息
        queue = []
        for i in range(l, r + 1):
            while queue and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])
        ans = [queue[0]]
        l += 1
        r += 1
        while r < n:
            while queue and nums[r] > queue[-1]:
                queue.pop()
            queue.append(nums[r])
            if queue[0] == nums[l - 1]:
                queue.pop(0)
            ans.append(queue[0])
            l += 1
            r += 1
        return ans


