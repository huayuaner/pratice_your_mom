# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
#
# 有效 二叉搜索树定义如下：
#
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 中序遍历必是单调递增序列
        # 可以考虑验证中序的序列是否单调
        # tmp = float("-inf")
        # def inorder(root):
        #     nonlocal tmp
        #     if not root:
        #         return True
        #     left = inorder(root.left)
        #     if root.val <= tmp:
        #         return False
        #     tmp = root.val
        #     right = inorder(root.right)
        #     return left and right
        # return inorder(root)

        # 非递归
        stack = []
        # tmp 记录前一个值
        tmp = float("-inf")
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()

                if cur.val <= tmp:
                    return False
                tmp = cur.val
                cur = cur.right
        return True
        # print(ans)