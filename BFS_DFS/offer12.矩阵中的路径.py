# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#  
#
# 例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。
#
# 示例 1：
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true
# 示例 2：
#
# 输入：board = [["a","b"],["c","d"]], word = "abcd"
# 输出：false

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # dfs
        start = []
        lens = len(word)
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    start.append((i, j))
        if not start:
            return False

        def dfs(x, y, pos):
            if pos == lens - 1: return True
            visited[x][y] = True
            # cnt = 0
            valid = False
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and pos < lens - 1 and board[nx][ny] == word[
                    pos + 1]:
                    # cnt += 1
                    visited[nx][ny] = True
                    valid = valid or dfs(nx, ny, pos + 1)
                    # print(visited,pos)
                    # 回溯
                    visited[nx][ny] = False
            visited[x][y] = False

            return valid

        for s in start:
            if dfs(s[0], s[1], 0):
                return True
        return False

        # 简洁版
        # def dfs(i, j, k):
        #     if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
        #     if k == len(word) - 1: return True
        #     board[i][j] = ''
        #     res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
        #     board[i][j] = word[k]
        #     return res

        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         if dfs(i, j, 0): return True
        # return False









