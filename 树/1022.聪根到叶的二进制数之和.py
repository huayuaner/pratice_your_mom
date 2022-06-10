# 给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。
#
# 例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。
# 对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。
#
# 返回这些数字之和。题目数据保证答案是一个 32 位 整数。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # ans = 0
        # def dfs(root, s):
        #     s += str(root.val)
        #     if not root.left and not root.right:
        #         nonlocal ans
        #         # print(s)
        #         ans += int(s, 2)
        #         return
        #     if root.left:
        #         dfs(root.left, s)
        #     if root.right:
        #         dfs(root.right, s)
        # dfs(root, '')
        # return ans
        # val = 0
        # def dfs(root,val):
        #     if not root:
        #         return 0
        #     val = (val<<1)|root.val
        #     if not root.left and not root.right:
        #         return val
        #     return dfs(root.left, val) + dfs(root.right, val)
        # return dfs(root,0)

        # 迭代
        stack = []
        ans = val = 0
        pre = None
        while stack or root:
            while root:
                val = (val << 1) | root.val
                stack.append(root)
                root = root.left
            root = stack[-1]
            # 如果当前节点的没有右子树或者右子树已经被访问过
            if not root.right or pre == root.right:
                # 如果是叶子节点
                if not root.left and not root.right:
                    ans += val
                    # 无论是叶子节点还是右边被访问过，处理完之后往上走
                val >>= 1
                stack.pop()
                pre = root
                root = None
            else:
                root = root.right
        return ans

