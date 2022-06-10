# 给定一个排序的整数数组 nums ，其中元素的范围在 闭区间 [lower, upper] 当中，返回不包含在数组中的缺失区间。
#
# 示例：
#
# 输入: nums = [0, 1, 3, 50, 75], lower = 0 和 upper = 99,
# 输出: ["2", "4->49", "51->74", "76->99"]

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # if not nums:
        #     if lower != upper:
        #         return [str(lower)+'->'+str(upper)]
        #     else:
        #         return [str(lower)]
        # ans = []
        # n = len(nums)
        # # 初始化
        # if nums[0]!=lower:
        #     if nums[0]-lower == 1:
        #         ans.append(str(lower))
        #     else:
        #         ans.append(str(lower) + '->' + str(nums[0]-1))
        # pre = nums[0]
        # for i in range(1,n):
        #     if nums[i] - pre > 1:
        #         if nums[i]-pre == 2:
        #             ans.append(str(nums[i]-1))
        #         else:
        #             ans.append(str(pre+1) + '->' + str(nums[i]-1))
        #     pre = nums[i]
        # if nums[-1] != upper:
        #     if upper-nums[-1] == 1:
        #         ans.append(str(upper))
        #     else:
        #         ans.append(str(nums[-1]+1) + '->' + str(upper))
        # return ans

        # 简化版
        nums.append(upper+1)
        ans = []
        pre = lower-1
        for num in nums:
            if num - pre == 2:
                # print(nums)
                ans.append(str(num-1))
            elif num-pre > 2:
                ans.append(str(pre+1) + '->' + str(num-1))
            pre = num
        return ans





