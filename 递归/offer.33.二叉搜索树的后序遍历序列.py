#输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
def func(start, end):
    if start >= end - 1:
        return True
    rootval = postorder[end]
    right = start
    while right < end:
        if postorder[right] > rootval:
            break
        right += 1
    if right == start:
        if rootval > min(postorder[right:end]):
            return False
        return func(right, end - 1)
    if right == end:
        if rootval < max(postorder[start:right]):
            return False
        return func(start, end - 1)
    # print(right, end)
    if rootval < max(postorder[start:right]) or rootval > min(postorder[right:end]):
        return False
    left = func(start, right - 1)
    right = func(right, end)
    return left and right


return func(0, len(postorder) - 1)