# 翻转一棵二叉树。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # DFS
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     dfs(root.right)
        #     root.left, root.right = root.right, root.left
        # dfs(root)
        # return root

        # BFS
        if not root:
            return
        pq = deque()
        pq.append(root)
        while pq:
            node = pq.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                pq.append(node.left)
            if node.right:
                pq.append(node.right)

        return root
