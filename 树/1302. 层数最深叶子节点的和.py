# 给你一棵二叉树的根节点 root ，请你返回 层数最深的叶子节点的和 。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # 深搜
        # max_depth = 0
        # ans = 0
        # def dfs(root,depth):
        #     if not root:
        #         return
        #     nonlocal max_depth,ans
        #     depth += 1
        #     # print(root.val,depth)
        #     if depth > max_depth:
        #         ans = root.val
        #         max_depth = depth
        #     elif depth == max_depth:
        #         ans += root.val
        #     dfs(root.left,depth)
        #     dfs(root.right,depth)
        # dfs(root, 0)
        # return ans

        # bfs
        pq = deque([root])
        # ans = 0
        while pq:
            tmp = 0
            for _ in range(len(pq)):
                node = pq.popleft()
                tmp += node.val
                if node.left:
                    pq.append(node.left)
                if node.right:
                    pq.append(node.right)
        return tmp
