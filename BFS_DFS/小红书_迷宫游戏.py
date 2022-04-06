# 薯队长最近在玩一个迷宫探索类游戏，迷宫是一个N*N的矩阵形状，
# 其中会有一些障碍物禁止通过。这个迷宫还有一个特殊的设计，
# 它的左右 边界以及上下边界是连通的，比如在(2,n)的位置继续往右走一格可以到(2,1)，
# 在(1,2)的位置继续往上走一格可以到(n,2)。请问薯队长从起点位置S，最少走多少格才能
# 到达迷宫的出口位置E。

from collections import deque
n = int(input())
Map = []
for _ in range(n):
    Map.append(list(input()))
# bfs
def bfs(Map):
    pq = deque()
    vis = set()
    for i in range(n):
        for j in range(n):
            if Map[i][j] == 'S':
                pq.append((i,j))
                vis.add((i,j))
                break
    step = 0
    while pq:
        length = len(pq)
        for _ in range(length):
            i,j = pq.popleft()
            if Map[i][j] == 'E':
                return step
            for nx,ny in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                nx %= n
                nx = n if nx < 0 else nx
                ny %= n
                ny = n if ny < 0 else ny
                if (nx,ny) not in vis and Map[nx][ny]!= '#':
                    pq.append((nx,ny))
                    vis.add((nx,ny))
        step += 1
        # print(pq, step)
    return -1
print(bfs(Map))