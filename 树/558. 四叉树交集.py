# 二进制矩阵中的所有元素不是 0 就是 1 。
#
# 给你两个四叉树，quadTree1 和 quadTree2。其中 quadTree1 表示一个 n * n 二进制矩阵，而 quadTree2 表示另一个 n * n 二进制矩阵。
#
# 请你返回一个表示 n * n 二进制矩阵的四叉树，它是 quadTree1 和 quadTree2 所表示的两个二进制矩阵进行 按位逻辑或运算 的结果。
#
# 注意，当 isLeaf 为 False 时，你可以把 True 或者 False 赋值给节点，两种值都会被判题机制 接受 。
#
# 四叉树数据结构中，每个内部节点只有四个子节点。此外，每个节点都有两个属性：
#
# val：储存叶子结点所代表的区域的值。1 对应 True，0 对应 False；
# isLeaf: 当这个节点是一个叶子结点时为 True，如果它有 4 个子节点则为 False 。
#
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        # root = merge(quadTree1, quadTree2)
        def merge(tree1, tree2):
            # node = Node(-1, 0,None, None, None, None)
            if tree1.isLeaf:
                return Node(True, True) if tree1.val else tree2
            if tree2.isLeaf:
                return Node(True, True) if tree2.val else tree1
            node = Node(False, False)
            node.topLeft = merge(tree1.topLeft, tree2.topLeft)
            node.topRight = merge(tree1.topRight, tree2.topRight)
            node.bottomLeft = merge(tree1.bottomLeft, tree2.bottomLeft)
            node.bottomRight = merge(tree1.bottomRight, tree2.bottomRight)
            # print(node.topRight, node.topLeft, node.bottomLeft, node.bottomRight)
            if node.topRight.val == node.topLeft.val == node.bottomLeft.val == node.bottomRight.val and node.topRight.isLeaf and node.topLeft.isLeaf and node.bottomLeft.isLeaf and node.bottomRight.isLeaf:

                node.isLeaf = True
                node.val = node.topLeft.val
                node.topRight = node.topLeft = node.bottomLeft = node.bottomRight = None
            return node
        return merge(quadTree1, quadTree2)

