# 给定一棵二叉搜索树，请找出其中第 k 大的节点的值。
#
#  
#
# 示例 1:
#
# 输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 4
# 示例 2:
#
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 4


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # N
        # ans = []
        # def dfs(root):
        #     if not root:
        #         return
        #     #print(ans)
        #     if len(ans) >= k:
        #         return
        #     dfs(root.right)
        #     ans.append(root.val)
        #     dfs(root.left)
        # dfs(root)

        # return ans[k-1]

        self.k = k

        def dfs(root):
            if not root:
                return
                # print(ans)
            dfs(root.right)
            self.k -= 1
            if self.k == 0:
                self.ans = root.val
                return
            dfs(root.left)

        dfs(root)

        return self.ans
