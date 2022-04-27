# 在小美和小团生活的城市中，有n行m列共计n*m个十字路口，第i行j列的十字路口有两个属性aij，b­ij。当行人处在i行j列的路口，对于任意非负整数k:
#
# 当时间处在[k*aij+k*b­ij), (k+1)*aij+k*bij)时，行人可以选择走到i±1行j列的路口。
#
# 当时间处在[(k+1)*aij+k*bij), (k+1)*aij+(k+1)*b­ij)时，行人可以选择走到i行j±1列的路口。
#
# 每次移动花费的时间为1，且要保证将要去的十字路口存在，即属于n*m个路口当中。可以选择原地静止不动。
#
# 在第0时刻，小美处在xs行ys列的十字路口处，要去xt行yt列的十字路口找小团。小团原地不动等小美，请问小美所花费的时间最少是多少?

from collections import deque
# 思路bfs
# 关键是往上下走和左右走的情况
# 使用time%（a+b），查看余数的区间即可
# 通过80%
import heapq

m, n, xs, ys, xt, yt = map(int, input().split())
cross = [[0 for _ in range(m)] for _ in range(2)]
for i in range(m):
    cross[0][i] = list(map(int, input().split()))
for i in range(m):
    cross[1][i] = list(map(int, input().split()))
pq = []
pq.append((0, xs, ys))
vis = set()


# vis.add((xs,ys))
def rule(t, i, j):
    a, b = cross[0][i - 1][j - 1], cross[1][i - 1][j - 1]
    t = t % (a + b)
    if t < a:
        return True, a - t
    else:
        return False, a + b - t


while pq:
    t, x, y = heapq.heappop(pq)
    if (x, y) in vis:
        continue
    vis.add((x, y))
    # print(x,y)
    if x == xt and y == yt:
        print(t)
        break
    dire, t_w = rule(t, x, y)
    for step in [1, -1]:
        nx, ny = x + step, y + step
        if 0 <= ny < n:
            heapq.heappush(pq, (t + 1 + (t_w if dire else 0), x, ny))
        if 0 <= nx < m:
            heapq.heappush(pq, (t + 1 + (0 if dire else t_w), nx, y))




