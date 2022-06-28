# 数对 (a,b) 由整数 a 和 b 组成，其数对距离定义为 a 和 b 的绝对差值。
#
# 给你一个整数数组 nums 和一个整数 k ，数对由 nums[i] 和 nums[j] 组成且满足 0 <= i < j < nums.length 。返回 所有数对距离中 第 k 小的数对距离。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,3,1], k = 1
# 输出：0
# 解释：数对和对应的距离如下：
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# 距离第 1 小的数对是 (1,1) ，距离为 0 。
# 示例 2：
#
# 输入：nums = [1,1,1], k = 2
# 输出：0
# 示例 3：
#
# 输入：nums = [1,6,1], k = 3
# 输出：5

import bisect
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # 排序 + 二分
        # def count(mid):
        #     cnt = 0
        #     for i,num in enumerate(nums):
        #         # 这里的意思是对于当前第i个数num，有几个是以num为尾的对数小于等于mid
        #         # 拿num-mid就可以的得到与num相差mid的数pre
        #         # 由于num是sorted的，我们将num-mid插入值nums[:i+1]的范围
        #         # 就可以的到num-mid在nums[:i+1]的位置
        #         # pre右边的点的和num的差值都会比mid小
        #         pre = bisect.bisect_left(nums, num-mid, 0, i)
        #         cnt += i-pre
        #     return cnt

        # 排序 + 双指针 + 二分
        def count(mid):
            cnt = i = 0
            for j,num in enumerate(nums):
                while num - nums[i] > mid:
                    i += 1
                cnt += j-i
            return cnt
        nums.sort()
        # 在范围[0,nums[-1]-num[0]]进行二分查找count结果第k个的数
        return bisect.bisect_left(range(nums[-1]-nums[0]), k, key = count)