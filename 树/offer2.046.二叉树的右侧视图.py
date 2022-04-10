# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]
# 示例 2:
#
# 输入: [1,null,3]
# 输出: [1,3]
# 示例 3:
#
# 输入: []
# 输出: []

from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # bfs
        # if not root:
        #     return []
        # pq = deque()
        # pq.append(root)
        # ans = []
        # while pq:
        #     n = len(pq)
        #     right = pq[-1].val
        #     for _ in range(n):
        #         node = pq.popleft()
        #         if node.left:
        #             pq.append(node.left)
        #         if node.right:
        #             pq.append(node.right)
        #     ans.append(right)
        # return ans

        # dfs
        # 存每层的最右节点
        # 存depth 和 val 的映射
        r_val = dict()
        max_depth = -1
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                # 如果没有值就设置，有值就跳过
                r_val.setdefault(depth, node.val)
                # 先左再右，弹出就是先右再左
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        # print(r_val)
        return [r_val[depth] for depth in range(max_depth + 1)]

