请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
 

注意：

一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
空白格用 '.' 表示。

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # HashMap = defaultdict(list)
        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j]!=".":
        #             if board[i][j] in HashMap:
        #                 #print(HashMap[board[i][j]])
        #                 for i_p,j_p in HashMap[board[i][j]]:
        #                     if i_p == i or j_p == j:
        #                         print(i,j, i_p, j_p)
        #                         return False
        #                     if i_p in range(i//3*3, i//3*3+3) and j_p in range(j//3*3, j//3*3+3):
        #                         print(i,j, 2)
        #                         return False
        #             HashMap[board[i][j]].append((i,j))
        # print(HashMap)
        # return True

        # 数组
        # 行，列，九宫格
        row = [[0 for _ in range(10)] for _ in range(9)]
        col = [[0 for _ in range(10)] for _ in range(9)]
        box = [[0 for _ in range(10)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                curNum = int(board[i][j])
                #print(i, curNum)
                if row[i][curNum] == 1: return False
                if col[j][curNum] == 1: return False
                if box[i//3 + j // 3 * 3][curNum] == 1: return False
                row [i][curNum] += 1
                col [j][curNum] += 1
                box [i//3 + j // 3 * 3][curNum] += 1
        return True
                 
        