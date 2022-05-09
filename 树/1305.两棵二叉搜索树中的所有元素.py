# 给你 root1 和 root2 这两棵二叉搜索树。请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.

# 输入：root1 = [2,1,4], root2 = [1,0,3]
# 输出：[0,1,1,2,3,4]

# 输入：root1 = [1,null,8], root2 = [8,1]
# 输出：[1,1,8,8]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from itertools import chain
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def midorder(root):
            # order = []
            cur = root
            stack = []
            while cur or stack:
                if cur:
                    stack.append(cur)
                    cur = cur.left
                else:
                    cur = stack.pop()
                    # order.append(cur.val)
                    yield cur.val
                    cur = cur.right
            # return order
        gen1 = midorder(root1)
        gen2 = midorder(root2)
        a,b = next(gen1, None), next(gen2, None)
        # print(a, b)
        ans = []
        while a is not None and b is not None:
            # print(a, b)
            if a<=b:
                ans.append(a)
                a = next(gen1, None)
            else:
                ans.append(b)
                b = next(gen2, None)
        # print(a,b)
        if a is not None:
            ans.append(a)
        if b is not None :
            ans.append(b)
        # chain将多个可迭代对象形成一个更大的迭代对象
        # print(chain(gen1, gen2))
        ans.extend(chain(gen1, gen2))
        return ans