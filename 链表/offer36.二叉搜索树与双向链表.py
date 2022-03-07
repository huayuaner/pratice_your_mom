#把一个二叉树的中序遍历变成双向循环链表，左子树代表前驱，右子树代表后继
def mid(root):  #中序遍历
    if not root:
        return
    mid(root.left)
    if self.pre:  #pre非空，pre与root互指
        self.pre.right = root
        root.left = self.pre
    else:        #pre空，确定头节点
        self.head = root
    self.pre = root #更新pre
    mid(root.right)


if not root: return
self.pre = None
mid(root)
self.head.left, self.pre.right = self.pre, self.head  #将头尾节点连起来
return self.head