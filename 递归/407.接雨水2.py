# 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。
#
# 输入: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# 输出: 4
# 解释: 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。
#
# 输入: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
# 输出: 10

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if n<=2 or m <=2:
            return 0
        # 记录搜索过的值
        visited = [[0]*n for _ in range(m)]
        #print(visited)
        # 存储墙壁的值
        pq = []
        # 初始墙壁是周围一圈
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    visited[i][j] = 1
                    # 这种记录位置的方式可以学习
                    heappush(pq, (heightMap[i][j], i*n+j))
        ans = 0
        # 四个方向
        dirs = [-1, 0, 1, 0, -1]
        while pq:
            # 弹出墙壁中的高度最小值
            height, pos = heappop(pq)
            for k in range(4):
                nx, ny = pos//n+dirs[k], pos%n+dirs[k+1]
                if 0<nx<m-1 and 0<ny<n-1 and visited[nx][ny]==0:
                    # 如果该最小值四周有比其小的点，差值加入结果
                    if heightMap[nx][ny] < height:
                        ans += height - heightMap[nx][ny]
                    visited[nx][ny] = 1
                    # 遍历到的点发展成新墙壁
                    heappush(pq, (max(height, heightMap[nx][ny]), nx*n + ny))
        return ans