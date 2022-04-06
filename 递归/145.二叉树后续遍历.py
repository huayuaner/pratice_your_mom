# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # def pos(root):
        #     if not root:
        #         return
        #     pos(root.left)
        #     pos(root.right)
        #     self.ans.append(root.val)
        # self.ans = []
        # pos(root)
        # return self.ans
        stack = []
        ans = []
        pre = None
        # 万古不变进入条件
        while root or stack:
            # 遍历到最左边
            while root:
                stack.append(root)
                root = root.left
            # 返回上一级
            root = stack.pop()
            # 如果右边没有值或者右边等于之前遍历过的结果
            if not root.right or root.right == pre:
                ans.append(root.val)
                # 把记录过值的root记录下来，防止重复遍历
                pre = root
                # 将root置空 使得root不会再进while循环中（因为这个root已经被遍历过）
                root = None
            # 如果右边有值且等于pre
            else:
                # 将这个节点放入栈中，移至其右节点
                stack.append(root)
                root = root.right
        return ans




