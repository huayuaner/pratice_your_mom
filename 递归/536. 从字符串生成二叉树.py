# 你需要用一个包括括号和整数的字符串构建一棵二叉树。
#
# 输入的字符串代表一棵二叉树。它包括整数和随后的 0 、1 或 2 对括号。整数代表根的值，一对括号内表示同样结构的子树。
#
# 若存在子结点，则从左子结点开始构建。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if len(s) == 0:
            return None
        n = len(s)
        left_l = -1
        for i in range(n):
            if s[i] == '(':
                left_l = i
                break
                # print()
        if left_l == -1:
            root = TreeNode(int(s))
            return root
        else:
            root = TreeNode(int(s[:left_l]))
        if left_l != -1:
            left_r = -1
            cnt = 0
            for i in range(left_l, n):
                if s[i] == '(':
                    cnt += 1
                elif s[i] == ')':
                    cnt -= 1
                    if cnt == 0:
                        left_r = i
                        break
            root.left = self.str2tree(s[left_l + 1:left_r])
        if left_r != n - 1:
            right_l = left_r + 1
            right_r = -1
            cnt = 0
            for i in range(right_l, n):
                if s[i] == '(':
                    cnt += 1
                elif s[i] == ')':
                    cnt -= 1
                    if cnt == 0:
                        right_r = i
                        break
            root.right = self.str2tree(s[right_l + 1:right_r])
        return root



