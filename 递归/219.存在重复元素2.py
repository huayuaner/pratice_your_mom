给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。

 

示例 1：

输入：nums = [1,2,3,1], k = 3
输出：true
示例 2：

输入：nums = [1,0,1,1], k = 1
输出：true
示例 3：

输入：nums = [1,2,3,1,2,3], k = 2
输出：false


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # cnt = {}
        # for i in range(len(nums)):
        #     if nums[i] in cnt and i-cnt[nums[i]] <= k:
        #         return True
        #     cnt[nums[i]] = i

        # return False

        #滑动窗口
        Set = set()
        for i in range(len(nums)):
            #保持窗口内元素都在集合中
            if i > k:
                Set.remove(nums[i - k - 1])
            #发现重复元素直接返回
            if nums[i] in Set:
                return True
            #非重复元素添加进集合中
            Set.add(nums[i])
        return False
