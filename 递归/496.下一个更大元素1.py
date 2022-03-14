# nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。
#
# 给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。
#
# 对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。
#
# 返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。
#
#  
#
# 示例 1：
#
# 输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
# 输出：[-1,3,-1]
# 解释：nums1 中每个值的下一个更大元素如下所述：
# - 4 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
# - 1 ，用加粗斜体标识，nums2 = [1,3,4,2]。下一个更大元素是 3 。
# - 2 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ##双循环遍历
        # ans = []
        # for i in range(len(nums1)):
        #     for j in range(nums2.index(nums1[i]), len(nums2)):
        #         if nums2[j]>nums1[i]:
        #             ans.append(nums2[j])
        #             break
        #         elif j == len(nums2) - 1:
        #             ans.append(-1)
        # return ans

        #栈+哈希表
        res = {}
        stack = []
        #遍历反向的nums2
        for num in reversed(nums2):
            #运用单调栈
            while stack and stack[-1]<num:
                stack.pop()
            #这时栈顶元素就是num对应的下一个更大元素，若栈空，则没有。将此关系放入哈希表中
            res[num] = stack[-1] if stack else -1
            stack.append(num)
            #遍历nums1找出哈希表对应的下一个最大元素
        return [res[num] for num in nums1]

