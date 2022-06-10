# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
#
# 一般来说，删除节点可分为两个步骤：
#
# 首先找到需要删除的节点；
# 如果找到了，删除它。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # if not root:
        #     return root
        # pre = None
        # cur = root
        # while cur:
        #     if cur.val > key:
        #         pre = cur
        #         cur = cur.left
        #     elif cur.val < key:
        #         pre = cur
        #         cur = cur.right
        #     else:
        #         if pre:
        #             if pre.left == cur:
        #                 if cur.left:
        #                     left = cur.left
        #                     pre.left = cur.left
        #                     while 1:
        #                         if not left.right:
        #                             break
        #                         left = left.right
        #                     left.right = cur.right
        #                     # pre.left.right = cur.right
        #                 elif cur.right:
        #                     pre.left = cur.right
        #                 else:
        #                     pre.left = None
        #             else:
        #                 if cur.left:
        #                     pre.right = cur.left
        #                     left = cur.left
        #                     while 1:
        #                         if not left.right:
        #                             break
        #                         left = left.right
        #                     left.right = cur.right
        #                     # pre.right.right = cur.right
        #                 elif cur.right:
        #                     pre.right = cur.right
        #                 else:
        #                     pre.right = None
        #         else:
        #             # print(111)
        #             if root.left:
        #                 right = root.right
        #                 left = root.left
        #                 root = root.left
        #                 while 1:
        #                     if not left.right:
        #                         break
        #                     else:
        #                         left = left.right
        #                 left.right = right

        #             elif root.right:
        #                 root = root.right
        #             else:
        #                 # print(111)
        #                 return

        #         break
        # return root

        # 递归
        if not root:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        # 找到了
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
                # 将右子树接到左子树的最右
            node = root.left
            while 1:
                if not node.right:
                    break
                node = node.right
            node.right = root.right
            root = root.left
        return root


