# 给你一个整数数组 nums ，按要求返回一个新数组 counts 。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。
#
#  
#
# 示例 1：
#
# 输入：nums = [5,2,6,1]
# 输出：[2,1,1,0]
# 解释：
# 5 的右侧有 2 个更小的元素 (2 和 1)
# 2 的右侧仅有 1 个更小的元素 (1)
# 6 的右侧有 1 个更小的元素 (1)
# 1 的右侧有 0 个更小的元素
# 示例 2：
#
# 输入：nums = [-1]
# 输出：[0]
# 示例 3：
#
# 输入：nums = [-1,-1]
# 输出：[0,0]
#
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # 归并
        n = len(nums)
        ans = [0] * n
        n_i = []
        for i, num in enumerate(nums):
            n_i.append([num, i])

        def merge(num_l):
            if len(num_l) <= 1:
                return num_l
            mid = len(num_l) // 2
            left = merge(num_l[:mid])
            right = merge(num_l[mid:])
            l1, l2 = len(left), len(right)
            i = j = 0
            new_nums = []
            while i < l1 and j < l2:
                # print(left, right)
                if left[i][0] <= right[j][0]:
                    new_nums.append(left[i])
                    ans[left[i][1]] += j
                    i += 1
                else:
                    new_nums.append(right[j])
                    j += 1
            if j < l2:
                new_nums.extend(right[j:])
            else:
                new_nums.extend(left[i:])
            while i < l1:
                # print(left,right)
                ans[left[i][1]] += l2
                i += 1

            return new_nums

        merge(n_i)
        return ans


