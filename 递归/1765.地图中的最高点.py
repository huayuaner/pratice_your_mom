给你一个大小为 m x n 的整数矩阵 isWater ，它代表了一个由 陆地 和 水域 单元格组成的地图。

如果 isWater[i][j] == 0 ，格子 (i, j) 是一个 陆地 格子。
如果 isWater[i][j] == 1 ，格子 (i, j) 是一个 水域 格子。
你需要按照如下规则给每个单元格安排高度：

每个格子的高度都必须是非负的。
如果一个格子是是 水域 ，那么它的高度必须为 0 。
任意相邻的格子高度差 至多 为 1 。当两个格子在正东、南、西、北方向上相互紧挨着，就称它们为相邻的格子。（也就是说它们有一条公共边）
找到一种安排高度的方案，使得矩阵中的最高高度值 最大 。

请你返回一个大小为 m x n 的整数矩阵 height ，其中 height[i][j] 是格子 (i, j) 的高度。如果有多种解法，请返回 任意一个 。
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # 记录矩阵的长与宽
        n, m = len(isWater), len(isWater[0])
        # ans 生成一个水域为0，其他位置为-1的矩阵
        ans = [[water-1 for water in row] for row in isWater]
        # 将所有水域的位置入队，非常巧妙的写法。遍历每行，再把遍历的行再按列遍历，如果water==1就放入这个位置
        q = deque((i, j) for i, row in enumerate(isWater) for j, water in enumerate(row) if water) 
        # 广度优先搜索
        while q:
            i,j = q.popleft()
            for x,y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0<=x<n and 0<=y<m and ans[x][y] == -1:
                    ans[x][y] = ans[i][j]+1
                    q.append((x,y))
        return ans

