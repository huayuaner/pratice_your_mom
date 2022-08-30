# 给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:
#
# 创建一个根节点，其值为 nums 中的最大值。
# 递归地在最大值 左边 的 子数组前缀上 构建左子树。
# 递归地在最大值 右边 的 子数组后缀上 构建右子树。
# 返回 nums 构建的 最大二叉树 。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # def helper(l,r):
        #     if l>=r:
        #         return None
        #     max_val = nums[l]
        #     max_idx = l
        #     for i in range(l+1,r):
        #         if nums[i] > max_val:
        #             max_val = nums[i]
        #             max_idx = i
        #     root = TreeNode(max_val)
        #     root.left = helper(l,max_idx)
        #     root.right = helper(max_idx+1, r)
        #     return root
        # return helper(0,len(nums))

        n = len(nums)
        stack = list()
        tree = [None] * n
        for i in range(n):
            tree[i] = TreeNode(nums[i])
            while stack and nums[i] > nums[stack[-1]]:
                # tree[i] 左边 小于等于tree[i].val 的最大值
                tree[i].left = tree[stack[-1]]
                stack.pop()
            if stack:
                # 这时候的tree[i]是stack[-1] 右边的最大值
                tree[stack[-1]].right = tree[i]
            stack.append(i)
        return tree[stack[0]]

