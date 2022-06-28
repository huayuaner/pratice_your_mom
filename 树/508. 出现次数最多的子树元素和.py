# 给你一个二叉树的根结点 root ，请返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。
#
# 一个结点的 「子树元素和」 定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        cnt = Counter()

        def dfs(root):
            if not root:
                return 0
            l, r = dfs(root.left), dfs(root.right)
            cur_val = root.val + l + r
            cnt[cur_val] += 1
            return cur_val

        dfs(root)
        max_cnt = max(cnt.values())
        return [key for key in cnt if cnt[key] == max_cnt]


