# 给你一个整数数组 nums，请你将该数组升序排列。
#
#  
#
# 示例 1：
#
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
# 示例 2：
#
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # return sorted(nums)
        # 归并排序，递归版
        # def process(nums, L, R):
        #     if L == R:
        #         return
        #     mid = L + (R-L)//2
        #     process(nums, L, mid)
        #     process(nums, mid+1, R)
        #     merge(nums, L, mid, R)

        # 归并排序，迭代版
        def process(nums):
            if not nums or len(nums) < 2:
                return
            N = len(nums)
            # 每次归并的左边子组大小（总大小为2）
            mergesize = 1
            while mergesize < N:
                # 记录左边点的位置
                L = 0
                while (L < N):
                    mid = L + mergesize - 1
                    # 说明左子组小于等于当前需排列的一半长度，而这一半在上次迭代中已经排序好了，说明这一段排序完成
                    if mid >= N:
                        break
                    R = min(mid + mergesize, N - 1)
                    merge(nums, L, mid, R)
                    L = R + 1
                # 防止溢出，当N接近系统内部最大值，mergesize*2有可能溢出
                if mergesize > N / 2:
                    break
                # 排序大小变成2倍，位运算快
                mergesize <<= 1

        def merge(nums, L, mid, R):
            i, j = L, mid + 1
            ans = []
            while i <= mid and j <= R:
                if nums[i] <= nums[j]:
                    ans.append(nums[i])
                    i += 1
                else:
                    ans.append(nums[j])
                    j += 1
            ans.extend(nums[i:mid + 1] if j > R else nums[j:R + 1])
            nums[L:R + 1] = ans

        process(nums)
        return nums

        # 非递归版本

