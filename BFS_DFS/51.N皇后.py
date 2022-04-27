# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
#
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
# 示例 2：
#
# 输入：n = 1
# 输出：[["Q"]]

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 皇后会在所在行列正负对角线进行攻击
        # 所以决定了每行只有一个皇后
        # 再使用集合 对列， 正对角线 x+y 负对角线x-y 进行判断
        def generateMap():
            Map = list()
            for i in range(n):
                # queen[i] 表示 第i行的皇后的位置
                # print(queen)
                row[queen[i]] = 'Q'
                Map.append(''.join(row))
                row[queen[i]] = '.'
            return Map

        def backtarck(row):
            if row == n:
                Map = generateMap()
                ans.append(Map)
            # 列的遍历，皇后放哪一列
            for i in range(n):
                if i in columns or (row + i) in dial1 or (row - i) in dial2:
                    continue
                queen[row] = i
                columns.add(i)
                dial1.add(row + i)
                dial2.add(row - i)
                backtarck(row + 1)
                columns.remove(i)
                dial1.remove(row + i)
                dial2.remove(row - i)

        ans = list()
        columns, dial1, dial2 = set(), set(), set()
        queen = [-1] * n
        row = ['.'] * n
        backtarck(0)
        return ans




