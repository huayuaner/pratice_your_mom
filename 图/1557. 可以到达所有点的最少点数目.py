# 给你一个 有向无环图 ， n 个节点编号为 0 到 n-1 ，以及一个边数组 edges ，其中 edges[i] = [fromi, toi] 表示一条从点  fromi 到点 toi 的有向边。
#
# 找到最小的点集使得从这些点出发能到达图中所有点。题目保证解存在且唯一。
#
# 你可以以任意顺序返回这些节点编号。
#
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # 使用入度为0的点来遍历
        # ans = []
        # vis = [False]*n
        in_degree = [0]*n
        # graph = [[]for _ in range(n)]
        for f,t in edges:
            # graph[f].append(t)
            in_degree[t] += 1
        # for i in range(n):
        #     if in_degree[i] == 0:
        #         ans.append(i)
        #         vis[i] = True
        #         pq = deque([i])
        #         while pq:
        #             node = pq.popleft()
        #             for nex in graph[node]:
        #                 if vis[nex] == False:
        #                     vis[nex] = True
        #                     pq.append(nex)
        return [i for i in range(n) if in_degree[i] == 0]