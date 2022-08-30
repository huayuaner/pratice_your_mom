# 给你一棵二叉树的根节点 root ，二叉树中节点的值 互不相同 。另给你一个整数 start 。在第 0 分钟，感染 将会从值为 start 的节点开始爆发。
#
# 每分钟，如果节点满足以下全部条件，就会被感染：
#
# 节点此前还没有感染。
# 节点与一个已感染节点相邻。
# 返回感染整棵树需要的分钟数。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.start = None
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # 一眼dfs模型
        # 麻烦的地方在于需要往父节点走

        # 记录每个点的父节点就可以了
        # 找到start

        parents = {}
        def dfs(node, pa):
            if not node:
                return
            if node.val == start:
                self.start = node
            parents[node] = pa
            dfs(node.left,node)
            dfs(node.right,node)
        dfs(root, None)

        ans = -1
        vis = {self.start, None}
        q = [self.start]
        while q:
            ans += 1
            tmp = q
            q = []
            for node in tmp:
                # 枚举左右节点和父节点
                for x in [node.left, node.right, parents[node]]:
                    if x not in vis:
                        vis.add(x)
                        q.append(x)
        return ans

