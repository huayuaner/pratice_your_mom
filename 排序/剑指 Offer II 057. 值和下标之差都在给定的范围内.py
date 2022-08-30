# 给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。
#
# 如果存在则返回 true，不存在返回 false。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3,1], k = 3, t = 0
# 输出：true
# 示例 2：
#
# 输入：nums = [1,0,1,1], k = 1, t = 2
# 输出：true
# 示例 3：
#
# 输入：nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出：false

from sortedcontainers import SortedList
import bisect


# from collections import deque
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # sorted_l = SortedList()
        # for i,num in enumerate(nums):
        #     sorted_l.add(num)

        #     index = bisect.bisect_left(sorted_l, num)
        #     # print(index, sorted_l,num)
        #     if index < len(sorted_l)-1 and sorted_l[index+1]-sorted_l[index] <=t:
        #         return True

        #     if index > 0 and sorted_l[index]-sorted_l[index-1] <=t:
        #         return True
        #     if len(sorted_l)>k:
        #         sorted_l.remove(nums[i-k])
        # return False

        # 桶排序
        bucket = dict()

        def get_bucket_id(num):
            return int(num // (t + 1))

        for i, num in enumerate(nums):
            idx = get_bucket_id(num)
            if idx in bucket:

                return True
            elif idx - 1 in bucket and num - bucket[idx - 1] <= t:
                return True
            elif idx + 1 in bucket and bucket[idx + 1] - num <= t:
                return True
            bucket[idx] = num
            # print(bucket)
            if len(bucket) > k:
                del_idx = get_bucket_id(nums[i - k])
                del bucket[del_idx]

        return False


