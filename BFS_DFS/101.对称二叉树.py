# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
#
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # dfs
        # def dfs(T1, T2):
        #     if not T1 and not T2:
        #         return True
        #     if not T1 or not T2:
        #         return False
        #     return  T1.val == T2.val and (dfs(T1.left, T2.right)) and dfs(T1.right, T2.left)
        # return dfs(root,root)

        # bfs
        pq = [root, root]
        while pq:
            left = pq.pop(0)
            right = pq.pop(0)
            if not left and not right:
                continue
            if (not left or not right) or (left.val != right.val):
                return False
            pq.append(left.right)
            pq.append(right.left)

            pq.append(right.right)
            pq.append(left.left)
        return True






