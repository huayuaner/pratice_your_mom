# 给你一个由 n 个节点（下标从 0 开始）组成的无向加权图，该图由一个描述边的列表组成，其中 edges[i] = [a, b] 表示连接节点 a 和 b 的一条无向边，且该边遍历成功的概率为 succProb[i] 。
#
# 指定两个节点分别作为起点 start 和终点 end ，请你找出从起点到终点成功概率最大的路径，并返回其成功概率。
#
# 如果不存在从 start 到 end 的路径，请 返回 0 。只要答案与标准答案的误差不超过 1e-5 ，就会被视作正确答案。
#
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Dijkstra
        vis = [False]*n
        # dist = [0]*n
        # dist[start] = 1
        pq = [(-1, start)]
        graph = [[] for _ in range(n)]
        for i,(a,b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))

        while pq:
            cur_prob,node  = heapq.heappop(pq)
            if node == end:
                return -cur_prob
            cur_prob = -cur_prob
            if vis[node] == True:
                continue
            vis[node] = True
            for nex,prob in graph[node]:
                nex_prob = (prob*cur_prob)
                # if nex_prob > dist[nex]:
                    # dist[nex] = nex_prob
                heapq.heappush(pq, (-nex_prob,nex))
        return 0