# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# 例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # def dfs(root, p, q):
        #     if not root:
        #         return False
        #     left = dfs(root.left,p,q)
        #     right = dfs(root.right,p,q)
        #     if (root.val in [q.val, p.val] and (left or right)) or (left and right):
        #         nonlocal ans
        #         ans = root
        #         return True
        #     return root.val in [q.val, p.val] or left or right
        # ans = None
        # dfs(root, p, q)
        # return ans

        # 二叉搜索树和二叉树不一样
        ans = root
        while 1:
            if ans.val > p.val and ans.val > q.val:
                ans = ans.left
            elif ans.val < p.val and ans.val < q.val:
                ans = ans.right
            else:
                break
        return ans
