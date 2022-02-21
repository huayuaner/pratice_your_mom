在大小为 n x n 的网格 grid 上，每个单元格都有一盏灯，最初灯都处于 关闭 状态。

给你一个由灯的位置组成的二维数组 lamps ，其中 lamps[i] = [rowi, coli] 表示 打开 位于 grid[rowi][coli] 的灯。即便同一盏灯可能在 lamps 中多次列出，不会影响这盏灯处于 打开 状态。

当一盏灯处于打开状态，它将会照亮 自身所在单元格 以及同一 行 、同一 列 和两条 对角线 上的 所有其他单元格 。

另给你一个二维数组 queries ，其中 queries[j] = [rowj, colj] 。对于第 j 个查询，如果单元格 [rowj, colj] 是被照亮的，则查询结果为 1 ，否则为 0 。在第 j 次查询之后 [按照查询的顺序] ，关闭 位于单元格 grid[rowj][colj] 上及相邻 8 个方向上（与单元格 grid[rowi][coli] 共享角或边）的任何灯。

返回一个整数数组 ans 作为答案， ans[j] 应等于第 j 次查询 queries[j] 的结果，1 表示照亮，0 表示未照亮。

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        point = set()
        # 这里使用x+y表示正对角线，x-y表示负对角线。拥有相同正对角线的点x+y的值是相同的，副对角线同理，是一个很好表示正负对角线的表达形式。
        row, col, diagonal, antidiagonal = Counter(), Counter(), Counter(), Counter()
        for x, y in lamps:
            # 去重，lamp在同一位置上视为同一个
            if (x, y) in point:
                continue
            point.add((x,y))
            row[x] += 1
            col[y] += 1
            diagonal[x+y] += 1
            antidiagonal[x-y] += 1
        ans = [0]*len(queries)
        # 遍历queries
        for i, (x, y) in enumerate(queries):
            # 如果行，列，正对角，反对有值则置1
            if row[x] or col[y] or diagonal[x+y] or antidiagonal[x-y]:
                ans[i] = 1
            # 搜寻该点周围八个方向的值，进行关灯操作
            for i in range(x-1,x+2):
                for j in range(y-1, y+2):
                    if 0<=i<n and 0<=j<n and (i,j) in point:
                        point.remove((i,j))
                        row[i] -= 1
                        col[j] -= 1
                        diagonal[i+j] -= 1
                        antidiagonal[i-j] -= 1
        return ans