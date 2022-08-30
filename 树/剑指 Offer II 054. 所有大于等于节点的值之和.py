# 给定一个二叉搜索树，请将它的每个节点的值替换成树中大于或者等于该节点值的所有节点值之和。
#
#  
#
# 提醒一下，二叉搜索树满足下列约束条件：
#
# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。
#  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        pre = 0
        def helper(root):
            if not root:
                return 0
            nonlocal pre
            helper(root.right)
            root.val += pre
            pre = root.val
            helper(root.left)
        helper(root)
        return root
