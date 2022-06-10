# 你被请来给一个要举办高尔夫比赛的树林砍树。树林由一个 m x n 的矩阵表示， 在这个矩阵中：
#
# 0 表示障碍，无法触碰
# 1 表示地面，可以行走
# 比 1 大的数 表示有树的单元格，可以行走，数值表示树的高度
# 每一步，你都可以向上、下、左、右四个方向之一移动一个单位，如果你站的地方有一棵树，那么你可以决定是否要砍倒它。
#
# 你需要按照树的高度从低向高砍掉所有的树，每砍过一颗树，该单元格的值变为 1（即变为地面）。
#
# 你将从 (0, 0) 点开始工作，返回你砍完所有树需要走的最小步数。 如果你无法砍完所有的树，返回 -1 。
#
# 可以保证的是，没有两棵树的高度是相同的，并且你至少需要砍倒一棵树。

import heapq
from collections import deque


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # m, n = len(forest), len(forest[0])
        # # 计算0的个数
        # cnt = 0
        # for i in range(m):
        #     for j in range(n):
        #         if forest[i][j] == 0:
        #             cnt += 1
        # # 广搜，搜需要砍的位置
        # pq = deque()
        # heap = []
        # pq.append((0,0))
        # if forest[0][0] > 1:
        #     heap.append((forest[0][0], 0, 0))
        # seen = set()
        # seen.add((0,0))
        # # 计算 1 的个数
        # cnt_1 = (0 if forest[0][0]!=1 else 1)
        # while pq:
        #     x, y = pq.popleft()
        #     for nx,ny in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
        #         if 0<=nx<m and 0<=ny<n and forest[nx][ny] >= 1 and (nx,ny) not in seen:
        #             if forest[nx][ny] > 1:
        #                 seen.add((nx,ny))
        #                 pq.append((nx,ny))
        #                 heapq.heappush(heap,(forest[nx][ny], nx, ny))
        #             else:
        #                 cnt_1 += 1
        #     # print(pq, heap)
        # # print(cnt_1, cnt, len(heap))
        # if cnt_1 + cnt + len(heap) != m*n:
        #     return -1
        # x, y = 0, 0
        # ans = 0
        # trees = sorted((h, i, j) for i, row in enumerate(forest) for j, h in enumerate(row) if h > 1)
        # # print(trees == heapq)
        # # print(heap)
        # # 这样计算是有问题的
        # # 会出现两点之间有0阻隔，绕远路的情况，这个没有考虑进去

        # while heap:
        #     _, tx, ty = heapq.heappop(heap)
        #     ans += (abs(tx-x)+abs(ty-y))
        #     x,y = tx,ty
        # return ans
        # 计算从从起始点到目标点的距离
        # def bfs(sx, sy, tx, ty):
        #     pq = deque()
        #     pq.append((sx,sy,0))
        #     seen = set()
        #     seen.add((sx,sy))
        #     while pq:
        #         x,y,step = pq.popleft()
        #         if x==tx and y==ty:
        #             return step
        #         for nx,ny in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
        #             if 0<=nx<m and 0<=ny<n and forest[nx][ny] > 0 and (nx,ny) not in seen:
        #                 pq.append((nx,ny,step+1))
        #                 seen.add((nx,ny))
        #     return -1
        # trees = [(forest[i][j], i, j) for i in range(m) for j in range(n) if forest[i][j]>1]
        # heapq.heapify(trees)
        # # trees = sorted((h, i, j) for i, row in enumerate(forest) for j, h in enumerate(row) if h > 1)
        # ans = sx = sy = 0
        # while trees:
        # # for _,tx, ty in trees:
        #     _, tx, ty = heapq.heappop(trees)

        #     dis = bfs(sx,sy, tx, ty)
        #     if dis<0:
        #         return -1
        #     ans += dis
        #     sx,sy = tx, ty
        # return ans

        m, n = len(forest), len(forest[0])

        def f(sx, sy, tx, ty):
            return abs(tx - sx) + abs(ty - sy)

        def bfs(sx, sy, tx, ty):
            # print(dis(sx,sy,tx,ty))
            pq = [(f(sx, sy, tx, ty), sx, sy)]
            dic = {(sx, sy): 0}
            while pq:
                # print(pq)
                _, x, y = heapq.heappop(pq)
                step = dic[(x, y)]
                if (x, y) == (tx, ty):
                    return step
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= nx < m and 0 <= ny < n and forest[nx][ny] > 0:
                        if (nx, ny) not in dic or dic[(nx, ny)] > step + 1:
                            dic[(nx, ny)] = step + 1
                            heapq.heappush(pq, (step + 1 + f(nx, ny, tx, ty), nx, ny))
            return -1

        trees = [(forest[i][j], i, j) for i in range(m) for j in range(n) if forest[i][j] > 1]
        heapq.heapify(trees)
        ans = sx = sy = 0
        while trees:
            # for _,tx, ty in trees:
            _, tx, ty = heapq.heappop(trees)

            dis = bfs(sx, sy, tx, ty)
            if dis < 0:
                return -1
            ans += dis
            sx, sy = tx, ty
        return ans









