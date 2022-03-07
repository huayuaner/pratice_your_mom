# 根据一棵树的中序遍历与后序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
# dict_pos = {val:idx for idx,val in enumerate(inorder)}
# # 递归方法
# def helper(left, right):
#     # 设置base case
#     if left > right:
#         return
#     # 得到节点值
#     val = postorder.pop()
#     root = TreeNode(val)
#     index = dict_pos[val]
#     # 这里的+1，-1 保证了index == right或left时下一次递归能返回
#     root.right = helper(index+1, right)
#     root.left = helper(left, index-1)
#     return root

# return helper(0, len(inorder)-1)
