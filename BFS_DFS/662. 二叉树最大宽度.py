# 给你一棵二叉树的根节点 root ，返回树的 最大宽度 。
#
# 树的 最大宽度 是所有层中最大的 宽度 。
#
# 每一层的 宽度 被定义为该层最左和最右的非空节点（即，两个端点）之间的长度。将这个二叉树视作与满二叉树结构相同，两端点间会出现一些延伸到这一层的 null 节点，这些 null 节点也计入长度。
#
# 题目数据保证答案将会在  32 位 带符号整数范围内。
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # bfs
        pq = deque([(root, 0)])
        ans = 1
        while pq:

            tmp = []
            for _ in range(len(pq)):
                node, idx = pq.popleft()
                if node.left:
                    pq.append((node.left, idx * 2 + 1))
                    tmp.append(idx * 2 + 1)
                if node.right:
                    pq.append((node.right, idx * 2 + 2))
                    tmp.append(idx * 2 + 2)
            if tmp:
                ans = max(ans, tmp[-1] - tmp[0] + 1)
        return ans
