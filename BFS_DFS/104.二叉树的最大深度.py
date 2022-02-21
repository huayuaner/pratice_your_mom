#给定一个二叉树，找出其最大深度。

#二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

#说明: 叶子节点是指没有子节点的节点。

#示例：
#给定二叉树 [3,9,20,null,null,15,7]，

   # 3
 #  / \
 # 9  20
#    /  \
#   15   7
#返回它的最大深度 3 。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs
        # def dfs(root):
        #     if not root:
        #         return 0
        #     return max(dfs(root.left), dfs(root.right))+1
        # return dfs(root)

        # bfs
        if not root:
            return 0
        pq = [root]
        depth = 0
        while pq:
            depth += 1
            i = len(pq)
            for _ in range(i):
                node = pq.pop(0)
                if node.left:
                    pq.append(node.left)
                if node.right:
                    pq.append(node.right)
        return depth 



