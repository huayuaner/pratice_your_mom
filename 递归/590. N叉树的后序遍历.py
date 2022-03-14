# 给定一个 n 叉树的根节点 root ，返回 其节点值的 后序遍历 。
#
# n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # def posorder(root):
        #     if not root:
        #         return
        #     for child in root.children:
        #         posorder(child)
        #     ans.append(root.val)
        # ans = []
        # posorder(root)
        # return ans

        # 迭代
        if not root:
            return []
        ans = []
        stack = [root]
        # visited代表这个点的children已经被遍历过了额
        visited = set()
        while stack:
            c = stack[-1]
            # 当该节点没有孩子或者孩子已经被遍历过，将值弹出
            if len(c.children)==0 or c in visited:
                ans.append(c.val)
                stack.pop()
                continue
            stack.extend(reversed(c.children))
            visited.add(c)
        return ans