# 给定一棵二叉搜索树和其中的一个节点 p ，找到该节点在树中的中序后继。如果节点没有中序后继，请返回 null 。
#
# 节点 p 的后继是值比 p.val 大的节点中键值最小的节点，即按中序遍历的顺序节点 p 的下一个节点。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # pre = None
        # ans = None
        # def midorder(root):
        #     nonlocal ans,pre
        #     if not root or ans:
        #         return
        #     midorder(root.left)
        #     if pre == p.val:
        #         ans = root
        #     pre = root.val
        #     midorder(root.right)
        #     return
        # midorder(root)
        # return ans
        successor = None
        # if p.right:
        #     successor = p.right
        #     while successor.left:
        #         successor = successor.left
        #     return successor
        node = root
        while node:
            if node.val > p.val:
                successor = node
                node = node.left
            else:
                node = node.right
        return successor