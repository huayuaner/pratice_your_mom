# 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。
#
# 示例 1:
#
# 输入: [1,2,1]
# 输出: [2,-1,2]
# 解释: 第一个 1 的下一个更大的数是 2；
# 数字 2 找不到下一个更大的数；
# 第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        # stack = []
        # lsr = []
        # n = len(nums)
        ##物理扩充
        # nums = nums + nums[:-1]
        # for num in reversed(nums):
                #物理扩充导致会出现重复数，所以加一个"="
        #     while stack and stack[-1] <= num:
        #         stack.pop()
        #     if stack:
                ## 从前面插入
        #         lsr = [stack[-1]]+lsr
        #     else:
        #         lsr = [-1]+lsr
        #     stack.append(num)
        ##返回前n个
        # return lsr[:n]
        stack = []
        n = len(nums)
        res = [-1] * n
        #使用下标进行扩充
        for i in range(2 * n - 1):
            #使用取余完成循环的效果，单调栈存入下标。
            while stack and nums[stack[-1]] < nums[i % n]:
                res[stack.pop()] = nums[i % n]
            stack.append(i % n)
        return res