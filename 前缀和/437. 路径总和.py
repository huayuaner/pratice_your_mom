# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
#
# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter


class Solution:
    # def __init__(self) -> None:
    #     self.ans = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pre_Sum = Counter()
        pre_Sum[0] = 1
        ans = 0

        def dfs(root, preSum):
            if not root:
                return
            preSum += root.val
            if preSum - targetSum in pre_Sum:
                nonlocal ans
                # print(preSum)
                ans += pre_Sum[preSum - targetSum]
            pre_Sum[preSum] += 1
            dfs(root.left, preSum)
            dfs(root.right, preSum)
            pre_Sum[preSum] -= 1

        dfs(root, 0)
        return ans
        # if not root:
        #     return 0
        # self.dfs(root,0,targetSum)
        # self.pathSum(root.left, targetSum)
        # self.pathSum(root.right, targetSum)
        # return self.ans

    # def dfs(self, root,total,targetSum):
    #     if not root:
    #         return
    #     total+= root.val
    #     if total == targetSum:
    #         # nonlocal ans
    #         self.ans += 1
    #     self.dfs(root.left, total,targetSum)
    #     self.dfs(root.right, total,targetSum)

