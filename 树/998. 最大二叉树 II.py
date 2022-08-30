# 最大树 定义：一棵树，并满足：其中每个节点的值都大于其子树中的任何其他值。
#
# 给你最大树的根节点 root 和一个整数 val 。
#
# 就像 之前的问题 那样，给定的树是利用 Construct(a) 例程从列表 a（root = Construct(a)）递归地构建的：
#
# 如果 a 为空，返回 null 。
# 否则，令 a[i] 作为 a 的最大元素。创建一个值为 a[i] 的根节点 root 。
# root 的左子树将被构建为 Construct([a[0], a[1], ..., a[i - 1]]) 。
# root 的右子树将被构建为 Construct([a[i + 1], a[i + 2], ..., a[a.length - 1]]) 。
# 返回 root 。
# 请注意，题目没有直接给出 a ，只是给出一个根节点 root = Construct(a) 。
#
# 假设 b 是 a 的副本，并在末尾附加值 val。题目数据保证 b 中的值互不相同。
#
# 返回 Construct(b) 。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if val > root.val:
        #     node = TreeNode(val, root)
        #     return node
        # def helper(fa, root):

        #     if not root:
        #         return
        #     # print(root.val)
        #     if root.val < val:
        #         node = TreeNode(val)
        #         fa.right = node
        #         node.left = root

        #         return
        #     else:
        #         if not root.right:

        #             node = TreeNode(val)
        #             root.right = node
        #             return
        #     # helper(root,root.left)
        #     helper(root,root.right)
        # helper(None, root)
        # return root

        # 优雅写法
        # if not root or val > root.val:
        #     node = TreeNode(val, root)
        #     return node
        # root.right = self.insertIntoMaxTree(root.right, val)
        # return root

        # 非递归
        fa = None
        cur = root
        while cur:
            if cur.val < val:
                break
            fa = cur
            cur = cur.right
        if fa:
            fa.right = TreeNode(val, cur)
        else:
            return TreeNode(val, root)
        return root

