# 在一个 n x n 的国际象棋棋盘上，一个骑士从单元格 (row, column) 开始，并尝试进行 k 次移动。行和列是 从 0 开始 的，所以左上单元格是 (0,0) ，右下单元格是 (n - 1, n - 1) 。
#
# 象棋骑士有8种可能的走法，如下图所示。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格。
# 每次骑士要移动时，它都会随机从8种可能的移动中选择一种(即使棋子会离开棋盘)，然后移动到那里。
#
# 骑士继续移动，直到它走了 k 步或离开了棋盘。
#
# 返回 骑士在棋盘停止移动后仍留在棋盘上的概率 。


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # BFS超时
        # # dp[i][j]代表留在该位置得到概率
        # dp = [[0 for _ in range(n)] for _ in range(n)]
        # # print(dp)
        # dp[row][column] = 1
        # pq = [(row,column)]
        # while k and pq:
        #     for i in range(len(pq)):
        #         x, y = pq.pop(0)
        #         for nx, ny in [(x-2,y+1),(x-2,y-1),(x-1,y+2),(x-1,y-2),(x+2,y+1),(x+2,y-1),(x+1,y+2),(x+1,y-2)]:
        #             if 0<=nx<n and 0<=ny<n :
        #                 pq.append((nx,ny))
        #                 dp[nx][ny] += dp[x][y]/8
        #         dp[x][y]=0
        #     #print(pq)
        #     k -= 1
           
        #     #print(dp)
        # if k!=0:
        #     return 0
        # ans = []
        # for i in range(n):
        #     ans.append(sum(dp[i]))
        # return sum(ans)

        
        # 动态规划
        # dp[k][i][j]表示第k步走到[i,j]的概率，也就是从[i,j]走k步还留在棋盘上的概率，属于逆向思维
        # dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k+1)]
        # for step in range(k+1):
        #     for x in range(n):
        #         for y in range(n):
        #             if step == 0:
        #                 dp[step][x][y] = 1
        #             else:
        #                 for nx, ny in [(x-2,y+1),(x-2,y-1),(x-1,y+2),(x-1,y-2),(x+2,y+1),(x+2,y-1),(x+1,y+2),(x+1,y-2)]:

        #                     if 0<=nx<n and 0<=ny<n :
        #                         #print(dp[step-1][nx][ny])
        #                         dp[step][x][y] += dp[step-1][nx][ny]/8
        # return dp[k][row][column]

        # dfs+记忆化
        #@functools.lru_cache(None)
        def dfs(step,x,y):
            if x<0 or x>n-1 or y<0 or y>n-1:
                return 0
            if step == 0:
                return 1
            ans = 0
            if self.memo[step][x][y]!=0:
                return self.memo[step][x][y]
            for nx, ny in [(x-2,y+1),(x-2,y-1),(x-1,y+2),(x-1,y-2),(x+2,y+1),(x+2,y-1),(x+1,y+2),(x+1,y-2)]:
                ans += dfs(step-1, nx, ny)/8
            self.memo[step][x][y] = ans
            return ans
        self.memo = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k+1)]
        return dfs(k,row, column)
            


