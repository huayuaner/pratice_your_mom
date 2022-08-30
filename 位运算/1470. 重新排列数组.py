# 给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。
#
# 请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。
#
#  
#
# 示例 1：
#
# 输入：nums = [2,5,1,3,4,7], n = 3
# 输出：[2,3,5,4,1,7]
# 解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，所以答案为 [2,3,5,4,1,7]
# 示例 2：
#
# 输入：nums = [1,2,3,4,4,3,2,1], n = 4
# 输出：[1,4,2,3,3,2,4,1]
# 示例 3：
#
# 输入：nums = [1,1,2,2], n = 2
# 输出：[1,2,1,2]
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # ans = []
        # for i in range(n):
        #     ans.append(nums[i])
        #     ans.append(nums[i+n])
        # return ans

        # nums[i] 大于1 且 小于等于 1000 -> 可以用 10 位二进制表示 -> 在用高位的10位存i正确的觉果
        # for i in range(2*n):
        #     # i 是当前位置
        #     j = 2*i if i < n else (i-n + 1)*2 - 1
        #     # print(j)
        #     # 这里(nums[i]&1023)的作用是 nums[i]可能已经被之间的某个值修改过了，已经变成了一个20位的数
        #     # 而我们只要其原来的值，也就是低十位，所以做了一个&
        #     nums[j] |= ((nums[i]&1023)<<10)
        #     # print(nums)
        # for i in range(2*n):
        #     # print(nums[i], (nums[i]>>10))
        #     nums[i] = (nums[i]>>10)
        # return nums

        # 因为nums[i]是正数，可以用负数完成
        for i in range(2 * n):
            if nums[i] < 0:
                continue
            j = i
            # 一直换到nums[i]是正确位置为止
            # 最后一轮会出现 j == i的情况，原地交换且原地取反
            while nums[i] > 0:
                # 不会出现 nums[j]已经是负数的情况
                # 因为j是正确位置，如果已经是负说明已经正确了，不可能出现还没交换就已经正确的情况
                j = 2 * j if j < n else (j - n + 1) * 2 - 1
                nums[i], nums[j] = nums[j], nums[i]
                nums[j] = -nums[j]
                # print(nums,i,j)
        for i in range(2 * n):
            nums[i] = -nums[i]
        return nums
