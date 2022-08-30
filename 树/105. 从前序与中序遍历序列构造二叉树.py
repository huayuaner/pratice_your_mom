# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dic = {val:idx for idx,val in enumerate(inorder)}
        idx_pre = 0
        def helper(l,r):
            if l>r:
                return
            nonlocal idx_pre
            root = TreeNode(preorder[idx_pre])
            idx_in = dic[preorder[idx_pre]]
            idx_pre += 1
            root.left = helper(l,idx_in-1)
            # idx_pre += 1
            root.right = helper(idx_in+1, r)
            return root
        return helper(0, len(preorder)-1)