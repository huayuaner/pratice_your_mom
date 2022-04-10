# 给定四个整数 sx , sy ，tx 和 ty，如果通过一系列的转换可以从起点 (sx, sy) 到达终点 (tx, ty)，则返回 true，否则返回 false。
#
# 从点 (x, y) 可以转换到 (x, x+y)  或者 (x+y, y)。
#
#  
#
# 示例 1:
#
# 输入: sx = 1, sy = 1, tx = 3, ty = 5
# 输出: true
# 解释:
# 可以通过以下一系列转换从起点转换到终点：
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)
# 示例 2:
#
# 输入: sx = 1, sy = 1, tx = 2, ty = 2
# 输出: false
# 示例 3:
#
# 输入: sx = 1, sy = 1, tx = 1, ty = 1
# 输出: true

from collections import deque


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # bfs
        # 超时
        # pq = deque()
        # pq.append((sx,sy))
        # while pq:
        #     nx, ny = pq.popleft()
        #     if nx==tx and ny==ty:
        #         return True
        #     if nx+ny <=tx:
        #         pq.append((nx+ny,ny))
        #     if nx+ny<=ty:
        #         pq.append((nx, nx+ny))
        # return False

        # 数学
        # 辗转相除法
        # 由于sx和sy都不等于0，所以只有当tx!=ty时才有上一个状态
        # 当tx>ty时，上一个状态是(tx-ty, ty)
        # 当tx<ty时，上一个状态是(tx, ty-tx)
        # 由于每一步都是大减小，可以直接更新为 大mod小
        if tx == ty:
            return tx == sx and ty == sy
        while sx < tx and sy < ty:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        if sx == tx and sy == ty:
            return True
        elif sx == tx:
            return ty > sy and (ty - sy) % tx == 0
        elif sy == ty:
            return tx > sx and (tx - sx) % ty == 0
        else:
            return False








