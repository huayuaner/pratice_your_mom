# 给定一个整数数组，你需要验证它是否是一个二叉搜索树正确的先序遍历序列。
#
# 你可以假定该序列中的数都是不相同的。

stack = []
new_min = float('-inf')
for i in range(len(preorder)):
    if preorder[i]<new_min:return False
    while stack and stack[-1]<preorder[i]:
        new_min = stack.pop()
    stack.append(preorder[i])
return True