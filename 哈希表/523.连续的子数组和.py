给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：

子数组大小 至少为 2 ，且
子数组元素总和为 k 的倍数。
如果存在，返回 true ；否则，返回 false 。

如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。0 始终视为 k 的一个倍数。

 

示例 1：

输入：nums = [23,2,4,6,7], k = 6
输出：true
解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。
示例 2：

输入：nums = [23,2,6,4,7], k = 6
输出：true
解释：[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。 
42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。
示例 3：

输入：nums = [23,2,6,4,7], k = 13
输出：false

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums)<2:
            return False
        HashMap = dict()
        remainder = 0
        HashMap[remainder] = -1
        # 余数定理
        for i,num in enumerate(nums):
            remainder = (remainder + num) % k
            if remainder in HashMap:
                if i - HashMap[remainder]>=2:
                    return True
            else:
                HashMap[remainder] = i
        return False