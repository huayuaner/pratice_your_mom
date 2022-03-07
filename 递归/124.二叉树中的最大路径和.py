# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
#
# 路径和 是路径中各节点值的总和。
#
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
#
# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
#
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")

        def dfs(root):
            if not root:
                return 0
            # 计算左边分支贡献，如果为负，不如不选
            left = max(dfs(root.left), 0)
            # 计算右边分支贡献，如果为负，不如不选
            right = max(dfs(root.right), 0)
            # 计算left -> root -> right作为路径与历史最大值比较
            total = root.val + left + right
            self.ans = max(self.ans, total)
            # 返回经过root的单边最大支给上一层使用
            return root.val + max(left, right)

        dfs(root)
        return self.ans


