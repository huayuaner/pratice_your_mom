# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#
# 本题中，一棵高度平衡二叉树定义为：
#
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # def dfs(root, depth):
        #     if not root:
        #         return True, depth
        #     left, l_dep = dfs(root.left, depth+1)
        #     right, r_dep = dfs(root.right, depth+1)
        #     return left and right and abs(l_dep-r_dep) <= 1, max(l_dep, r_dep)
        # return dfs(root, 0)[0]

        def check_height(root):
            if not root:
                return 0
            left = check_height(root.left)
            if left == -1:
                return -1
            # 这里如果返回-1，通过+1会变成0
            # 所以把+1 放在放回的地方会更好
            right = check_height(root.right)
            if right == -1:
                return - 1

            if abs(left - right) > 1:
                # print(root, left, right)
                return -1

            return max(left, right) + 1
            # tmp =

        # print(tmp)
        return check_height(root) != -1
