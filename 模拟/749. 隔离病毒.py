# 病毒扩散得很快，现在你的任务是尽可能地通过安装防火墙来隔离病毒。
#
# 假设世界由 m x n 的二维矩阵 isInfected 组成， isInfected[i][j] == 0 表示该区域未感染病毒，而  isInfected[i][j] == 1 表示该区域已感染病毒。可以在任意 2 个相邻单元之间的共享边界上安装一个防火墙（并且只有一个防火墙）。
#
# 每天晚上，病毒会从被感染区域向相邻未感染区域扩散，除非被防火墙隔离。现由于资源有限，每天你只能安装一系列防火墙来隔离其中一个被病毒感染的区域（一个区域或连续的一片区域），且该感染区域对未感染区域的威胁最大且 保证唯一 。
#
# 你需要努力使得最后有部分区域不被病毒感染，如果可以成功，那么返回需要使用的防火墙个数; 如果无法实现，则返回在世界被病毒全部感染时已安装的防火墙个数。

from collections import deque
import heapq


class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])

        # 返回下一轮可以传播的数量和需要的防火墙的数量
        def bfs(i, j, idx):
            pq = deque()
            pq.append((i, j))
            isInfected[i][j] = -idx
            spread = set()
            filters = 0
            while pq:
                x, y = pq.popleft()
                # 将病毒区域标记成-idx
                # isInfected[x][y] = -idx
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
                    # 下一个位置合法且没有遍历过
                    if 0 <= nx < m and 0 <= ny < n and isInfected[nx][ny] != -idx:
                        # 如果下一个位置是病毒，入队
                        if isInfected[nx][ny] == 1:
                            pq.append((nx, ny))
                            isInfected[nx][ny] = -idx
                        # 如果是未感染区域
                        elif isInfected[nx][ny] == 0:
                            # print(nx,ny,(x,y))
                            spread.add((nx, ny))
                            filters += 1
            return spread, filters

        filters = 0
        while 1:
            # 每一轮传播
            idx = 0
            pq = []
            for i in range(m):
                for j in range(n):
                    # 如果有病毒，计算下一轮能传播的个数
                    if isInfected[i][j] == 1:
                        idx += 1
                        s, f = bfs(i, j, idx)
                        heapq.heappush(pq, (-len(s), s, f, idx))
            # print(isInfected)
            # 如果没有，说明没有有效病毒了
            if not pq: break
            # 要被围起来的区域
            # print(pq)
            length, s, f, idx = heapq.heappop(pq)
            # print(pq)
            # 如果传播为0，说明全部传播成病毒了
            if length == 0: break
            filters += f

            # 还原
            for i in range(m):
                for j in range(n):
                    # 如果当前被标记成负数，说明是病毒位置
                    if isInfected[i][j] < 0:
                        isInfected[i][j] = (2 if isInfected[i][j] == -idx else 1)
            # 传播
            for length, s, f, idx in pq:
                # print(s)
                for i, j in s:
                    isInfected[i][j] = 1
                    # print(isInfected)

        return filters






