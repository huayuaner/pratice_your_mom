# 给你一棵二叉搜索树，请 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        head = TreeNode(-1)
        cur = head

        def midorder(root):
            if not root:
                return
            midorder(root.left)
            nonlocal cur
            cur.right = root
            root.left = None
            cur = cur.right
            midorder(root.right)
            return

        midorder(root)
        return head.right


