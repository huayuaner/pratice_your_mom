# 给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。
#
# 例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... 这样的车站路线行驶。
# 现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。
#
# 求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。
#
#  
#
# 示例 1：
#
# 输入：routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# 输出：2
# 解释：最优策略是先乘坐第一辆公交车到达车站 7 , 然后换乘第二辆公交车到车站 6 。
# 示例 2：
#
# 输入：routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# 输出：-1
from collections import defaultdict
from collections import deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # 公交车数量
        n = len(routes)
        # 每个公交车能到的站就是routes
        # stations = defaultdict(list)
        # for i in range(n):

        bus_in_stations = defaultdict(list)
        # 每个站包含的公交车
        for i, route in enumerate(routes):
            for sta in route:
                bus_in_stations[sta].append(i)
        pq = deque([(source, 0)])
        # print(pq)
        # 存已经做过的公交车
        buses = set()
        # 存到达过的站
        seen = set([source])
        while pq:
            # print( pq.popleft())
            sta, time = pq.popleft()
            if sta == target:
                return time
            for nex_bus in bus_in_stations[sta]:
                if nex_bus in buses: continue
                buses.add(nex_bus)
                for nex_sta in routes[nex_bus]:
                    if nex_sta in seen: continue
                    seen.add(nex_sta)
                    pq.append((nex_sta, time + 1))

            # print(pq)
        return -1


