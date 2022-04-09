# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
#
# 路径和 是路径中各节点值的总和。
#
# 给定一个二叉树的根节点 root ，返回其 最大路径和，即所有路径上节点值之和的最大值。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ans = float("-inf")
        def dfs(root):
            if not root:
                return 0
            # left = dfs(root.left)
            # right = dfs(root.right)
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            total = left + right + root.val
            nonlocal ans
            ans = max(ans, total)
            return root.val + max(left, right)
        dfs(root)
        return ans