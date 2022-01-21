# 设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。
#
# 示例：
#
# 输入： arr = [1,3,5,7,2,4,6,8], k = 4
# 输出： [1,2,3,4]

class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        # heapify(arr)
        # return [heappop(arr) for _ in range(k)]


        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        print(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        print(hp)
        ans = [-x for x in hp]
        return ans

        # arr.sort()
        # return arr[:k]