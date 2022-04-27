# 有一个 m × n 的矩形岛屿，与 太平洋 和 大西洋 相邻。 “太平洋” 处于大陆的左边界和上边界，而 “大西洋” 处于大陆的右边界和下边界。
#
# 这个岛被分割成一个由若干方形单元格组成的网格。给定一个 m x n 的整数矩阵 heights ， heights[r][c] 表示坐标 (r, c) 上单元格 高于海平面的高度 。
#
# 岛上雨水较多，如果相邻单元格的高度 小于或等于 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。水可以从海洋附近的任何单元格流入海洋。
#
# 返回 网格坐标 result 的 2D列表 ，其中 result[i] = [ri, ci] 表示雨水可以从单元格 (ri, ci) 流向 太平洋和大西洋 。
#
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pos1 = set()
        pos2 = set()

        def dfs(i, j, pos):
            pos.add((i, j))
            for nx, ny in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in pos and heights[nx][ny] >= heights[i][j]:
                    dfs(nx, ny, pos)

        for i in range(m):
            dfs(i, 0, pos1)
            dfs(i, n - 1, pos2)
        for j in range(n):
            dfs(0, j, pos1)
            dfs(m - 1, j, pos2)
        # ans = []
        # # print(pos1, pos2)
        # for x,y in pos1:
        #     if (x,y) in pos2:
        #         ans.append([x,y])
        # return ans
        # print(pos1&pos2)
        # set1 & set2 取交集
        # 使用map将其中的元组换成list
        # 再对整体list化
        return list(map(list, pos1 & pos2))
