给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。

假设二叉树中至少有一个节点。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # 最深的，最左
        # 最深优先，在最深找最左

        max_depth = -1
        left_down = None

        def helper(root, depth):
            nonlocal max_depth, left_down
            if not root:
                return
            if depth > max_depth:
                # print(depth,root,max_depth)
                left_down = root.val
                max_depth = depth
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)

        helper(root, 0)
        return left_down



