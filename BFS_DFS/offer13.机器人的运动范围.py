# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
#
#  
#
# 示例 1：
#
# 输入：m = 2, n = 3, k = 1
# 输出：3
# 示例 2：
#
# 输入：m = 3, n = 1, k = 0
# 输出：1

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        # bfs
        def bitsum(n):
            s = 0
            while n:
                s += n%10
                n //= 10
            return s

        if k==0:
            return 1
        # cnt = 1
        # visited = [[False for _ in range(n)] for _ in range(m)]
        # visited[0][0] = True
        visited = set()
        visited.add((0,0))
        pq = [(0,0)]
        while pq:
            x,y = pq.pop(0)
            for nx,ny in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited and bitsum(nx)+bitsum(ny)<=k:
                    pq.append((nx,ny))
                    # visited[nx][ny] = True
                    visited.add((nx, ny))
                    # cnt += 1
        return len(visited)


