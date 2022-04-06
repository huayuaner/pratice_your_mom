# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明：叶子节点是指没有子节点的节点。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # def dfs(root, depth):
        #     # 只有一个节点没有左右两个子树的情况才能返回深度
        #     if not root.left and not root.right:
        #         return depth
        #     if not root.left:
        #         return dfs(root.right,depth+1)
        #     elif not root.right:
        #         return dfs(root.left, depth+1)
        #     else:
        #         return min(dfs(root.left, depth+1), dfs(root.right,depth+1))
        # if not root:
        #     return 0
        # return dfs(root, 1)

        if not root:
            return 0
        # 当左右只有一个有，因为有一个必是0，选其中较大的，+1（+1是包括当前root的意思）
        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right))+1
        # 当左右都有，返回最小
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right))+1