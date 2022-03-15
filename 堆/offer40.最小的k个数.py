# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
#
#  
#
# 示例 1：
#
# 输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
# 示例 2：
#
# 输入：arr = [0,1,2,1], k = 1
# 输出：[0]
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # heapify(arr)
        # return [heappop(arr) for _ in range(k)]

        if k == 0:
            return []
        heap = [-x for x in arr[:k]]
        heapify(heap)
        for i in range(k, len(arr)):
            if -heap[0] > arr[i]:
                heappop(heap)
                heappush(heap,-arr[i])
        ans = [-x for x in heap]
        return ans
