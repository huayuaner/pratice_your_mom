# 给定一个二叉树 根节点 root ，树的每个节点的值要么是 0，要么是 1。请剪除该二叉树中所有节点的值为 0 的子树。
#
# 节点 node 的子树为 node 本身，以及所有 node 的后代。

from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        # def check(root):
        #     if not root:
        #         return True
        #     left = check(root.left)
        #     right = check(root.right)
        #     if root.val != 1:

        #         if left and right:
        #             # print(111)
        #             root.val = -1
        #             return True

        #     return False
        # check(root)
        # # print(root)
        # if root.val==-1:
        #     return
        # pq = deque()
        # pq.append(root)
        # while pq:
        #     n = len(pq)
        #     for _ in range(n):
        #         node = pq.popleft()
        #         if node.left:
        #             if node.left.val!=-1:
        #                 pq.append(node.left)
        #             else:
        #                 node.left = None
        #         if node.right:
        #             if node.right.val!=-1:
        #                 pq.append(node.right)
        #             else:
        #                 node.right = None
        # return root

        # dfs
        # def dfs(root):
        #     if not root:
        #         return True
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     if left:
        #         root.left = None
        #     if right:
        #         root.right = None
        #     return root.val!=1 and left and right
        # if not dfs(root):
        #     # print(root)
        #     return root
        # else:
        #     # print(root)
        #     return None

        # 后序遍历
        def posorder(root):
            if not root:
                return
            root.left = posorder(root.left)
            root.right = posorder(root.right)
            if root.val == 0 and not root.left and not root.right:
                return
            return root

        return posorder(root)

