# 给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 k 。
#
# 返回到目标结点 target 距离为 k 的所有结点的值的列表。 答案可以以 任何顺序 返回。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # 有点像周赛二叉树感染那道题
        # 定义node指向father的情况
        s2f = dict()
        start = None
        def dfs(root,fa):
            if not root:
                return
            s2f[root] = fa
            if root == target:
                nonlocal start
                start = root
            dfs(root.left, root)
            dfs(root.right, root)
            return
        dfs(root,None)
        # print(start,s2f)
        # bfs
        pq = deque([start])
        seen = set([start,None])
        while k and pq:
            k -= 1
            for _ in range(len(pq)):
                node = pq.popleft()
                # print(node.val)
                for nex in [node.left, node.right, s2f[node]]:
                    if nex in seen:continue
                    seen.add(nex)
                    pq.append(nex)
            # print([node.val for node in pq])
        return [node.val for node in pq]
