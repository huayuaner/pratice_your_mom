# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
#
# 叶子节点 是指没有子节点的节点。
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        road = []

        def helper(tot, root):
            # print(root.val,road)
            road.append(root.val)
            tot += root.val
            if not root.left and not root.right:
                nonlocal ans
                if tot == targetSum:
                    ans.append(road[:])
                road.pop()
                return

            if root.left:
                helper(tot, root.left)
            if root.right:
                # road.append(root.val)
                helper(tot, root.right)
            road.pop()
            return

        if not root:
            # print(111)
            return []
        helper(0, root)
        return ans