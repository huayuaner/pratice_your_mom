# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
#
# 请你找出符合题意的 最短 子数组，并输出它的长度。
#
#  
#
# 示例 1：
#
# 输入：nums = [2,6,4,8,10,9,15]
# 输出：5
# 解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        ##获得排序后的数组
        # sort = sorted(nums)
        ##pre和end是否改变的标记位
        # flag1, flag2 = -1, -1
        # pre = 0
        # end = len(nums)-1
        ##判断条件当pre和end都找到则跳出
        # while pre<=end and (flag1==-1 or flag2==-1):
        #     if nums[pre]!=sort[pre] and flag1 == -1:
        #         flag1 = pre
        #     if nums[end]!=sort[end] and flag2 == -1:
        #         flag2 = end
        #     if flag1 == -1:
        #         pre += 1
        #     if flag2 == -1:
        #         end -= 1
        # print(flag1, flag2)
        # return flag2-flag1+1 if flag1!=-1 and flag2!=-1 else 0
        n = len(nums)
        maxn, right = float("-inf"), -1
        minn, left = float("inf"), n
        for i in range(len(nums)):
            # 如果大于最大值则更新最大值
            if nums[i]>=maxn:
                maxn = nums[i]
            ##如果小于最大值则更新right，right代表无序的右边，因为C串的最小大于B串的最大，所以当这种情况发生说明right还处在无序的串中
            else:
                right = i
            ##左边同理
            if nums[n-i-1]<=minn:
                minn = nums[n-i-1]
            else:
                left = n-i-1
            #如果找不到右边说明已经是升序
        return 0 if right == -1 else right - left + 1
