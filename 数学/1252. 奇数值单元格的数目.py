# 给你一个 m x n 的矩阵，最开始的时候，每个单元格中的值都是 0。
#
# 另有一个二维索引数组 indices，indices[i] = [ri, ci] 指向矩阵中的某个位置，其中 ri 和 ci 分别表示指定的行和列（从 0 开始编号）。
#
# 对 indices[i] 所指向的每个位置，应同时执行下述增量操作：
#
# ri 行上的所有单元格，加 1 。
# ci 列上的所有单元格，加 1 。
# 给你 m、n 和 indices 。请你在执行完所有 indices 指定的增量操作后，返回矩阵中 奇数值单元格 的数目。
#
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0]*m
        cols = [0]*n
        for x,y in indices:
            rows[x] += 1
            cols[y] += 1
        odd_x = sum(row%2 for row in rows)
        odd_y = sum(col%2 for col in cols)
        return odd_x*(n - odd_y) + odd_y*(m - odd_x)