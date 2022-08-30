# 给定一个二叉树的根 root 和两个整数 val 和 depth ，在给定的深度 depth 处添加一个值为 val 的节点行。
#
# 注意，根节点 root 位于深度 1 。
#
# 加法规则如下:
#
# 给定整数 depth，对于深度为 depth - 1 的每个非空树节点 cur ，创建两个值为 val 的树节点作为 cur 的左子树根和右子树根。
# cur 原来的左子树应该是新的左子树根的左子树。
# cur 原来的右子树应该是新的右子树根的右子树。
# 如果 depth == 1 意味着 depth - 1 根本没有深度，那么创建一个树节点，值 val 作为整个原始树的新根，而原始树就是新根的左子树。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # if depth == 1:
        #     node = TreeNode(val)
        #     node.left = root
        #     return node
        # # bfs
        # pq = deque([root])
        # cur_depth = 0
        # while pq:
        #     cur_depth += 1
        #     if cur_depth < depth - 1:
        #         for _ in range(len(pq)):
        #             node = pq.popleft()
        #             if node.left:
        #                 pq.append(node.left)
        #             if node.right:
        #                 pq.append(node.right)
        #     elif cur_depth == depth - 1:
        #         for _ in range(len(pq)):
        #             node = pq.popleft()
        #             left,right = node.left,node.right
        #             node.left,node.right = TreeNode(val),TreeNode(val)
        #             node.left.left = left
        #             node.right.right = right
        #         break
        # return root

        # 优雅写法
        # if depth == 1:
        #     return TreeNode(val, root, None)
        # # bfs
        # # bfs到depth-1为止
        # pq = deque([root])
        # for _ in range(depth-2):
        #     for _ in range(len(pq)):
        #         node = pq.popleft()
        #         if node.left:
        #             pq.append(node.left)
        #         if node.right:
        #             pq.append(node.right)
        # # print(pq)
        # for node in pq:
        #     node.left = TreeNode(val, node.left, None)
        #     node.right = TreeNode(val, None,node.right)
        # return root

        # dfs

        if not root:
            return None
        if depth == 1:
            return TreeNode(val, root, None)
        if depth == 2:
            root.left = TreeNode(val, root.left, None)
            root.right = TreeNode(val, None, root.right)
            # return root
        else:
            self.addOneRow(root.left, val, depth - 1)
            self.addOneRow(root.right, val, depth - 1)
        return root
