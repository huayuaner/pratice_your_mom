# 给你一个 n 个节点的 有向图 ，节点编号为 0 到 n - 1 ，每个节点 至多 有一条出边。
#
# 有向图用大小为 n 下标从 0 开始的数组 edges 表示，表示节点 i 有一条有向边指向 edges[i] 。如果节点 i 没有出边，那么 edges[i] == -1 。
#
# 同时给你两个节点 node1 和 node2 。
#
# 请你返回一个从 node1 和 node2 都能到达节点的编号，使节点 node1 和节点 node2 到这个节点的距离 较大值最小化。如果有多个答案，请返回 最小 的节点编号。如果答案不存在，返回 -1 。
#
# 注意 edges 可能包含环。
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # 把node1能搜索的所有点的距离求出来
        # 把node2能搜索到的所有点的距离求出来
        n = len(edges)
        min_dis = float('inf')
        ans = -1
        def calc_dis(x:int)->List[int]:
            dis = [float('inf')]*n
            d = 0
            while x!=-1 and dis[x] == float('inf'):
                dis[x] = d
                d += 1
                x = edges[x]
            return dis
        # print(calc_dis(node1))
        # print(calc_dis(node2))
        for i,d1,d2 in zip(range(n),calc_dis(node1), calc_dis(node2)):
            d = max(d1,d2)
            # print(min_dis,d)
            if d < min_dis:
                ans = i
                min_dis = d
        return ans