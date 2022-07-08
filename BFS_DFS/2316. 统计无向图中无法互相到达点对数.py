# 给你一个整数 n ，表示一张 无向图 中有 n 个节点，编号为 0 到 n - 1 。同时给你一个二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示节点 ai 和 bi 之间有一条 无向 边。
#
# 请你返回 无法互相到达 的不同 点对数目 。

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # 构建邻接矩阵
        grid = [[] for _ in range(n)]
        for a,b in edges:
            grid[a].append(b)
            grid[b].append(a)
        total = cnt = ans = 0
        vis = [False] * n
        def dfs(x):
            vis[x] = True
            # 当前连通集的节点个数
            nonlocal cnt
            cnt += 1
            for y in grid[x]:
                if not vis[y]:
                    dfs(y)
        for i in range(n):
            if not vis[i]:
                cnt = 0
                dfs(i)
                ans += cnt*total
                total += cnt
        return ans
