# 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。
#
# 假设输入的前序遍历和中序遍历的结果中都不含重复的# Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
#
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         #递归
#         # HashMap = {val:idx for idx,val in enumerate(inorder)}
#         # def helper(l, r):
#         #     if l > r:
#         #         return
#         #     #print(l,r)
#         #     val = preorder.pop(0)
#         #     root = TreeNode(val)
#         #     idx = HashMap[val]
#         #     # 由于pop(0)是从左边开始pop，所以要从左子树开始
#         #     # 106的中序后序 pop是从右边开始，所以从右子树开始恢复
#         #     root.left = helper(l, idx-1)
#         #     root.right = helper(idx+1,r)
#
#         #     return root
#         # return helper(0, len(preorder)-1)
#
#         # 迭代
#         # 前序:中左右；中序：左中右
#         # 前序的下一个就是前一个左子树，而中序的第一个指向没有左子树的子树
#
#         if not preorder:
#             return None
#         root = TreeNode(preorder[0])
#         stack = [root]
#         inorderIndex = 0
#         for i in range(1, len(preorder)):
#             preorderVal = preorder[i]
#             node = stack[-1]
#             # 如果当前前序的下一个不是没有左子树的那个，那他就是上一个的左子树
#             if inorder[inorderIndex] != node.val:
#                 node.left = TreeNode(preorderVal)
#                 stack.append(node.left)
#             # 如果当前栈顶元素没有左子树了，所以前序下一个就是右子树，要找这是谁的右子树
#             else:
#                 # 这是因为栈中的任意两个相邻的节点，前者都是后者的某个祖先。
#                 # 并且我们知道，栈中的任意一个节点的右儿子还没有被遍历过，说明后者一定是前者左儿子的子树中的节点，那么后者就先于前者出现在中序遍历中。
#                 # 这个这个右子树是栈顶和inorderIndex指向的最后一个相同的元素的右子树
#                 while stack and stack[-1].val == inorder[inorderIndex]:
#                     node = stack.pop()
#                     inorderIndex += 1
#                 # 确定右子树，将右子树放入栈
#                 node.right = TreeNode(preorderVal)
#                 stack.append(node.right)
#         return root数字。