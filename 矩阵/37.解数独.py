编写一个程序，通过填充空格来解决数独问题。

数独的解法需 遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用 '.' 表示。

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        # 记录每行，每列，每个九宫格数字的出现
        self.row = [set() for _ in range(9)]
        self.col = [set() for _ in range(9)]
        self.box = [set() for _ in range(9)]
        # 记录需要填入的位置
        self.space = []
        # 是否遍历到头的标记
        valid = False
        # 遍历整个矩阵，将出现的放入行，列，方格中，并记录位置
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    self.space.append((i,j))
                else:
                    self.row[i].add(ord(board[i][j]) - ord('0'))
                    self.col[j].add(ord(board[i][j]) - ord('0'))
                    self.box[i//3 * 3+j//3].add(ord(board[i][j]) - ord('0'))
        
        
        def dfs(pos):
            # if pos == len(self.space):
            #     return 
            # 如果没有标记位之后错误的答案会覆盖正确的答案
            nonlocal valid
            if pos == len(self.space):
                valid = True
                return

            i, j = self.space[pos]
            for num in range(1,10):
                if num not in self.row[i] and num not in self.col[j] and num not in self.box[i//3 * 3+j//3]:
                    # 通过在三个集合中增加此数字判定数字加入
                    self.row[i].add(num)
                    self.col[j].add(num)
                    self.box[i//3 * 3+j//3].add(num)
                    board[i][j] = str(num)
                    dfs(pos+1)
                    # 在回溯过程中再删掉这个数字
                    self.row[i].remove(num)
                    self.col[j].remove(num)
                    self.box[i//3 * 3+j//3].remove(num)
                # 验证此轮遍历是否有效
                if valid :
                    return 
        return dfs(0)
