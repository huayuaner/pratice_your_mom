# 二叉树中，如果一个节点是其父节点的唯一子节点，则称这样的节点为 “独生节点” 。二叉树的根节点不会是独生节点，因为它没有父节点。
#
# 给定一棵二叉树的根节点 root ，返回树中 所有的独生节点的值所构成的数组 。数组的顺序 不限 。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        # def dfs(root):
        #     if not root.left and not root.right:
        #         return
        #     if root.left and root.right:
        #         dfs(root.left)
        #         dfs(root.right)
        #     elif root.left:
        #         dfs(root.left)
        #         # nonlocal ans
        #         ans.append(root.left.val)
        #     else:
        #         dfs(root.right)
        #         # nonlocal ans
        #         ans.append(root.right.val)
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            if root.left and not root.right:
                ans.append(root.left.val)
            elif root.right and not root.left:
                ans.append(root.right.val)
        dfs(root)
        return ans