# 树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。
#
# 给你一棵包含 n 个节点的树，标记为 0 到 n - 1 。给定数字 n 和一个有 n - 1 条无向边的 edges 列表（每一个边都是一对标签），其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条无向边。
#
# 可选择树中任何一个节点作为根。当选择节点 x 作为根节点时，设结果树的高度为 h 。在所有可能的树中，具有最小高度的树（即，min(h)）被称为 最小高度树 。
#
# 请你找到所有的 最小高度树 并按 任意顺序 返回它们的根节点标签列表。
#
# 树的 高度 是指根节点和叶子节点之间最长向下路径上边的数量。
from collections import defaultdict
from collections import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # bfs找最远，超时
        # if n == 1:
        #     return [0]
        # dic = defaultdict(list)
        # for e in edges:
        #     # print(e)
        #     dic[e[0]].append(e[1])
        #     dic[e[1]].append(e[0])
        #     # dic[1].append(0)
        # # print(dic)

        # def distance(dic, root):
        #     # print(root)
        #     pq = deque()
        #     pq.append(root)
        #     seen = set()
        #     seen.add(root)
        #     height = 0
        #     while pq:

        #         n = len(pq)
        #         for _ in range(n):
        #             node = pq.popleft()
        #             for i in dic[node]:
        #                 if i not in seen:
        #                     pq.append(i)
        #                     seen.add(i)
        #         height += (1 if pq else 0)
        #     # print(root, height)
        #     return height
        # ans = []
        # min_val = float("inf")
        # for key in dic.keys():
        #     tmp = distance(dic,key)
        #     if tmp < min_val:
        #         min_val = tmp
        #         ans.clear()
        #         ans.append(key)
        #     elif tmp == min_val:
        #         ans.append(key)
        # return ans

        in_degree = [0] * n
        dic = defaultdict(list)
        for e in edges:
            in_degree[e[0]] += 1
            in_degree[e[1]] += 1
            dic[e[0]].append(e[1])
            dic[e[1]].append(e[0])
        # 入度为1的点
        nodes = [i for i, val in enumerate(in_degree) if val <= 1]

        while n:
            n -= len(nodes)
            tmp = nodes
            nxt = []
            for node in nodes:
                # 只有与其相连的收到牵连
                for other in dic[node]:
                    in_degree[other] -= 1
                    if in_degree[other] == 1:
                        nxt.append(other)
            nodes = nxt
        return tmp


