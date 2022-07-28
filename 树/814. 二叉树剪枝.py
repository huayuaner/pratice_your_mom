# 给你二叉树的根结点 root ，此外树的每个结点的值要么是 0 ，要么是 1 。
#
# 返回移除了所有不包含 1 的子树的原二叉树。
#
# 节点 node 的子树为 node 本身加上所有 node 的后代。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # def dfs(root):
        #     if not root:
        #         return True
        #     l,r = dfs(root.left), dfs(root.right)
        #     if l:
        #         root.left = None
        #     if r:
        #         root.right = None
        #     return l and r and root.val != 1
        # if dfs(root):
        #     return None
        # return root

        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and root.val == 0:
            return None
        return root