# 你被给定一个 m × n 的二维网格 rooms ，网格中有以下三种可能的初始化值：
#
# -1 表示墙或是障碍物
# 0 表示一扇门
# INF 无限表示一个空的房间。然后，我们用 231 - 1 = 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647 的。
# 你要给每个空房间位上填上该房间到 最近门的距离 ，如果无法到达门，则填 INF 即可。
INF = 2 ** (31) - 1
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # 从门去dfs
        pq = deque()

        m, n = len(rooms), len(rooms[0])
        vis = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    pq.append((0, i, j))
                    vis[i][j] = True
        # print(pq)
        while pq:
            dis, i, j = pq.popleft()
            dis += 1
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ni < m and 0 <= nj < n and rooms[ni][nj] != -1 and vis[ni][nj] == False:
                    vis[ni][nj] = True
                    rooms[ni][nj] = dis
                    pq.append((dis, ni, nj))
        return rooms
