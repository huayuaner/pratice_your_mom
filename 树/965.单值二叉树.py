# 如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
#
# 只有给定的树是单值二叉树时，才返回 true；否则返回 false。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        target = root.val
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val != target:
                return False
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return True