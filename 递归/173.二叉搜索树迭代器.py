# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        #完成中序遍历的前半部分，存了左边的深度
        while root:
            self.stack.append(root)
            root = root.left

        # self.stack = []
        # self.Midorder = []
        # self.i = 0
        # while root or self.stack:
        #     if root:
        #         self.stack.append(root)
        #         root = root.left
        #     else:
        #         root = self.stack.pop()
        #         self.Midorder.append(root.val)
        #         root = root.right
        # print(self.Midorder)

        # self.queue = collections.deque()
        # self.MidOrder(root)

    # def MidOrder(self, root):
    #     if not root:
    #         return
    #     self.MidOrder(root.left)
    #     self.queue.append(root.val)
    #     self.MidOrder(root.right)

    # 中序遍历的下一个值
    def next(self) -> int:
        # return self.queue.popleft()

        # self.i+=1
        # return self.Midorder[self.i-1]

        #调用此函数才计算当前中序的值
        cur = self.stack.pop()
        node = cur.right
        #将node的左子树放入栈，衔接之后的中序遍历，同时为hasnode准备
        while node:
            self.stack.append(node)
            node = node.left
        return cur.val

    # 中序遍历是否有下一个值
    def hasNext(self) -> bool:
        #由于此时已放入当前值的所有左子树进入栈中，所以栈空表明中序遍历结束
        return len(self.stack) > 0

        # return self.i < len(self.Midorder)

        # return len(self.queue)>0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()