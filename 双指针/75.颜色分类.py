# 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
# 必须在不使用库的sort函数的情况下解决这个问题。
#
#  
#
# 示例 1：
#
# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]
# 示例 2：
#
# 输入：nums = [2,0,1]
# 输出：[0,1,2]
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 扫描两次
        # idx = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums[idx],nums[i] = nums[i], nums[idx]
        #         idx += 1

        # for i in range(len(nums)):
        #     if nums[i] == 1:
        #         nums[idx],nums[i] = nums[i], nums[idx]
        #         idx += 1

        # 扫描一次
        # n = len(nums)
        # # 指向1要换的位置和0要换的位置
        # p0 = p1= 0
        # for i in range(n):
        #     if nums[i] == 1:
        #         nums[i], nums[p1] = nums[p1], nums[i]
        #         p1 += 1
        #     elif nums[i] == 0:
        #         nums[i],nums[p0] = nums[p0], nums[i]
        #         # 说明此时0后面已经有1了
        #         # 上一步操作把1换给了i位置
        #         # 要把1再换回来
        #         if p0 < p1:
        #             nums[p1], nums[i] = nums[i], nums[p1]
        #         p0 += 1
        #         p1 += 1

        # 扫描1次
        # 指向p0和p2位置
        n = len(nums)
        p0, p2 = 0, n - 1
        idx = 0
        while idx <= p2:
            # 预防nums[idx]和p2位置都是2 的 情况

            while idx <= p2 and nums[idx] == 2:
                nums[idx], nums[p2] = nums[p2], nums[idx]
                p2 -= 1
            if nums[idx] == 0:
                nums[idx], nums[p0] = nums[p0], nums[idx]
                p0 += 1
            idx += 1



