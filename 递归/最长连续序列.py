给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

 

示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 哈希表 
        # if not nums:
        #     return 0
        # #nums.sort()
        # cnt = Counter(nums)
        # #print(cnt)
        # ans = 1
        # for key in sorted(cnt.keys()):
        #     tmp = 1
        #     i = 1
        #     while key + i in cnt and cnt[key + i]:
        #         cnt[key + i] -= 1
        #         tmp += 1
        #         ans  = max(tmp, ans)
        #         i += 1
        # return ans

        # 集合
        ans = 0
        Set = set(nums)
        for num in Set:
            # 此值是序列最小的
            if num - 1 not in Set:
                cur_num = num
                lens = 1

                while cur_num + 1 in Set:
                    cur_num += 1
                    lens += 1
                ans = max(lens, ans)
        return ans




