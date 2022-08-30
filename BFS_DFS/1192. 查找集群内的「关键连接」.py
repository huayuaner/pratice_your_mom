# 力扣数据中心有 n 台服务器，分别按从 0 到 n-1 的方式进行了编号。它们之间以「服务器到服务器」点对点的形式相互连接组成了一个内部集群，其中连接 connections 是无向的。从形式上讲，connections[i] = [a, b] 表示服务器 a 和 b 之间形成连接。任何服务器都可以直接或者间接地通过网络到达任何其他服务器。
#
# 「关键连接」 是在该集群中的重要连接，也就是说，假如我们将它移除，便会导致某些服务器无法访问其他服务器。
#
# 请你以任意顺序返回该集群内的所有 「关键连接」。
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # 入度为1的节点的连接都是关键连接
        # 入度不为1的节点也可以是关键节点
        # tarjan
        def tarjan(edges):
            ans = []
            vis = [-1]*n
            ans = []
            # 身份证
            ID = -1
            def dfs(fa, i):
                nonlocal ID
                ID += 1
                # if vis[i] == -1:
                cur_id = ID
                vis[i] = ID
                for nex in edges[i]:
                    if nex == fa:
                        continue
                    if vis[nex] == -1:
                        nex_id = dfs(i,nex)
                        if nex_id > cur_id:
                            # print(nex, i, vis)
                            ans.append([i,nex])

                        # nex_id = vis[nex]
                    vis[i] = min(vis[i], vis[nex])
                    # print(nex)
                # print(vis,i)

                # print(vis)
                return vis[i]
            dfs(-1, 0)
            return ans
        edges = [[] for _ in range(n)]
        for a,b in connections:
            edges[a].append(b)
            edges[b].append(a)
        return tarjan(edges)