# 给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的数值。
#
# 注意：
#
# 给定的目标值 target 是一个浮点数
# 题目保证在该二叉搜索树中只会存在一个最接近目标值的数
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # ans = None
        # def helper(root):
        #     nonlocal ans
        #     if not root:
        #         return
        #     if ans == None or abs(root.val-target) < abs(ans-target):
        #         ans = root.val
        #     helper(root.left)
        #     helper(root.right)
        # helper(root)
        # return ans
        ans = float('inf')
        while root:
            ans = min(root.val, ans, key=lambda x: abs(target-x))
            root = root.right if root.val < target else root.left
        return ans