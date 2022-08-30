# 现有一个按 升序 排列的整数数组 nums ，其中每个数字都 互不相同 。
#
# 给你一个整数 k ，请你找出并返回从数组最左边开始的第 k 个缺失数字。

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # 时间 为 n的
        # for i in range(1, len(nums)):
        #     if nums[i] - nums[i-1] - 1 >=k:
        #         return nums[i-1] + k
        #     else:
        #         k -= nums[i] - nums[i-1] - 1
        # return nums[-1] + k

        # 有序 -> 二分

        # 得到位置idx之前确实的数字个数
        missing = lambda idx: nums[idx] - nums[0]- idx
        n = len(nums)
        if k > missing(n-1):
            return nums[-1] + (k - missing(n-1))
        l,r = 0, n-1
        while l<r:
            mid = l + (r-l) // 2
            if missing(mid) < k:
                l = mid+1
            else:
                r = mid
        # print(l)
        return nums[l-1] + (k - missing(l-1))
