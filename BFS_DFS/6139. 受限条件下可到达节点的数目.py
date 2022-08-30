# 现有一棵由 n 个节点组成的无向树，节点编号从 0 到 n - 1 ，共有 n - 1 条边。
#
# 给你一个二维整数数组 edges ，长度为 n - 1 ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条边。另给你一个整数数组 restricted 表示 受限 节点。
#
# 在不访问受限节点的前提下，返回你可以从节点 0 到达的 最多 节点数目。
#
# 注意，节点 0 不 会标记为受限节点。

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # dfs
        graph = [[] for _ in range(n)]
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        ans = 0
        r = set(restricted)
        def dfs(x, fa):
            if x in r:
                return
            nonlocal ans
            ans += 1
            for y in graph[x]:
                if y!=fa:
                    dfs(y,x)
        dfs(0, None)
        return ans