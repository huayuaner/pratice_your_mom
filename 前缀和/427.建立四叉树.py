# 给你一个 n * n 矩阵 grid ，矩阵由若干 0 和 1 组成。请你用四叉树表示该矩阵 grid 。
#
# 你需要返回能表示矩阵的 四叉树 的根结点。
#
# 注意，当 isLeaf 为 False 时，你可以把 True 或者 False 赋值给节点，两种值都会被判题机制 接受 。
#
# 四叉树数据结构中，每个内部节点只有四个子节点。此外，每个节点都有两个属性：
#
# val：储存叶子结点所代表的区域的值。1 对应 True，0 对应 False；
# isLeaf: 当这个节点是一个叶子结点时为 True，如果它有 4 个子节点则为 False 。
# class Node {
#     public boolean val;
#     public boolean isLeaf;
#     public Node topLeft;
#     public Node topRight;
#     public Node bottomLeft;
#     public Node bottomRight;
# }
# 我们可以按以下步骤为二维区域构建四叉树：
#
# 如果当前网格的值相同（即，全为 0 或者全为 1），将 isLeaf 设为 True ，将 val 设为网格相应的值，并将四个子节点都设为 Null 然后停止。
# 如果当前网格的值不同，将 isLeaf 设为 False， 将 val 设为任意值，然后如下图所示，将当前网格划分为四个子网格。
# 使用适当的子网格递归每个子节点。
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
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(start, end):
            if start[0] > end[0] or start[1] > end[1]:
                return
            length = end[0] - start[0] + 1
            # print(start, end)
            # total = sum(sum(grid[i][start[1]:end[1]+1]) for i in range(start[0],end[0]+1))
            total = pre_sum[end[0] + 1][end[1] + 1] + pre_sum[start[0]][start[1]] - pre_sum[end[0] + 1][start[1]] - \
                    pre_sum[start[0]][end[1] + 1]
            # print(total,start,end)
            if total == length ** 2 or total == 0:
                val = 1 if total else 0
                root = Node(val, True)
            else:
                root = Node(1, False)
                root.topLeft = helper(start, [start[0] + length // 2 - 1, start[1] + length // 2 - 1])
                root.bottomLeft = helper([start[0] + length // 2, start[1]], [end[0], start[1] + length // 2 - 1])
                root.topRight = helper([start[0], start[1] + length // 2], [start[0] + length // 2 - 1, end[1]])
                # print([start[0]+length//2, start[1]+length//2], start[0], length//2)
                root.bottomRight = helper([start[0] + length // 2, start[1] + length // 2], end)
            return root

        # helper([0,0],[3,3])
        n = len(grid)
        # 二维前缀和
        pre_sum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                pre_sum[i][j] = pre_sum[i - 1][j] + pre_sum[i][j - 1] - pre_sum[i - 1][j - 1] + grid[i - 1][j - 1]
        # print(pre_sum)

        return helper([0, 0], [n - 1, n - 1])