# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # def func(root):
        #     if not root :
        #         return
        #     self.res.append(root.val)
        #     func(root.left)
        #     func(root.right)
        # self.res = []
        # func(root)
        # return self.res
        res = []
        if not root:
            return res
        stack = []
        #当当前节点.right为空且无高级叶节点(stack为空)跳出
        while stack or root:
            # 遍历左边节点(相当于递归的func(root.left)
            while root:
                #stack暂存上一节点
                stack.append(root)
                res.append(root.val)
                root = root.left
            #当无左边节点，返回上一节点，转向有子树
            root = stack.pop()
            root = root.right
        return res

