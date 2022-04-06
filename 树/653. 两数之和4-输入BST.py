# 给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # 深度 + 哈希
        # self.Set = set()
        # self.ans = False
        # def dfs(root):
        #     if not root:
        #         return
        #     if k - root.val in self.Set:
        #         self.ans = True
        #         return
        #     self.Set.add(root.val)
        #     dfs(root.left)
        #     dfs(root.right)
        # dfs(root)
        # return self.ans

        # 中序遍历 + 双指针
        # 中序遍历是一个单调递增数组
        arr = []

        def inorder(root):
            if not root:
                return
            nonlocal arr
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)

        # 双指针
        inorder(root)
        l, r = 0, len(arr) - 1
        while l < r:
            if (tmp := arr[l] + arr[r]) > k:
                r -= 1
            elif tmp < k:
                l += 1
            else:
                return True
        return False




