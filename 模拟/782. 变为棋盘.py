# 一个 n x n 的二维网络 board 仅由 0 和 1 组成 。每次移动，你能任意交换两列或是两行的位置。
#
# 返回 将这个矩阵变为  “棋盘”  所需的最小移动次数 。如果不存在可行的变换，输出 -1。
#
# “棋盘” 是指任意一格的上下左右四个方向的值均与本身不同的矩阵。
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        # 行的掩码 和 列的掩码
        rowMask, colMask = 0, 0
        for i in range(n):
            rowMask |= (board[0][i] << i)
            colMask |= (board[i][0] << i)
        # n位取反
        # print(rowMask, colMask)
        reverse_rowMask = ((1 << n) - 1) ^ rowMask
        reverse_colMask = ((1 << n) - 1) ^ colMask
        # 记录和rowMask 和 colMask 相同的行数和列数
        rowcnt = colcnt = 0
        for i in range(n):
            cur_rowMask, cur_colMask = 0, 0
            for j in range(n):
                cur_rowMask |= (board[i][j] << j)
                cur_colMask |= (board[j][i] << j)
            if cur_rowMask not in [rowMask, reverse_rowMask] or cur_colMask not in [colMask, reverse_colMask]:
                return -1
            rowcnt += cur_rowMask == rowMask
            colcnt += cur_colMask == colMask

        def getMoves(mask: int, count: int) -> int:

            # 记录掩码 1 的个数
            ones = mask.bit_count()
            # print(ones, bin(mask)[2:], count)
            # 如果长度是奇数
            if n & 1:
                # 掩码中1的个数不合法 或 每种类型出现的次数不合法
                if abs(n - 2 * ones) != 1 or abs(n - 2 * count) != 1:
                    return -1
                # 如果1出现的个数是偶数
                # print(ones,n//2, ones&1)
                if ones == n // 2:  # ones&1 == 0:
                    # 这里的意思是1的个数是偶数 -> 需要还原的1的个数就是偶数
                    # (mask&0xAAAAAAAA).bit_count()表示101010101 与 mask相同的位数，也就是1放对地方的位置
                    # 每次转换把一个1放对地方，那转换次数就是 总的1的个数 - 放对地方的1的个数
                    return n // 2 - (mask & 0xAAAAAAAA).bit_count()
                else:
                    # 如果是奇数个
                    # 在长度为奇数的情况下要多1
                    return (n + 1) // 2 - (mask & 0x55555555).bit_count()
            else:
                if ones * 2 != n or count * 2 != n:
                    return -1
                cnt0 = n // 2 - (mask & 0xAAAAAAAA).bit_count()
                cnt1 = (n) // 2 - (mask & 0x55555555).bit_count()
                return min(cnt0, cnt1)

        rowMoves = getMoves(rowMask, rowcnt)
        colMoves = getMoves(colMask, colcnt)
        # print(rowMoves, colMoves)
        return -1 if rowMoves == -1 or colMoves == -1 else rowMoves + colMoves

