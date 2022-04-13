# 给定一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
#
# 每条从根节点到叶节点的路径都代表一个数字：
#
# 例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
# 计算从根节点到叶节点生成的 所有数字之和 。
#
# 叶节点 是指没有子节点的节点。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ans = 0

        def dfs(root, num):

            num = num * 10 + root.val
            # print(num)
            if not root.left and not root.right:
                nonlocal ans
                ans += num
                return
            if root.left:
                dfs(root.left, num)
            if root.right:
                dfs(root.right, num)

        dfs(root, 0)
        return ans
