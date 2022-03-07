# 在一个 106 x 106 的网格中，每个网格上方格的坐标为 (x, y) 。
#
# 现在从源方格 source = [sx, sy] 开始出发，意图赶往目标方格 target = [tx, ty] 。数组 blocked 是封锁的方格列表，其中每个 blocked[i] = [xi, yi] 表示坐标为 (xi, yi) 的方格是禁止通行的。
#
# 每次移动，都可以走到网格中在四个方向上相邻的方格，只要该方格 不 在给出的封锁列表 blocked 上。同时，不允许走出网格。
#
# 只有在可以通过一系列的移动从源方格 source 到达目标方格 target 时才返回 true。否则，返回 false。
#
#  
#
# 示例 1：
#
# 输入：blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
# 输出：false
# 解释：
# 从源方格无法到达目标方格，因为我们无法在网格中移动。
# 无法向北或者向东移动是因为方格禁止通行。
# 无法向南或者向西移动是因为不能走出网格。
# 示例 2：
#
# 输入：blocked = [], source = [0,0], target = [999999,999999]
# 输出：true
# 解释：
# 因为没有方格被封锁，所以一定可以到达目标方格。
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        n = len(blocked)
        if n < 2:
            return True
        #广度有限搜索
        def wfs(start, finish):
            sx, sy = start
            fx, fy = finish
            #使用队列配合搜索
            deque = [(sx, sy)]
            #记录访问过的点，避免重复访问
            visited = {(sx, sy)}
            #这个数量的blocked能包围的最大方块数
            cnt = n*(n-1)//2
            #这里cnt>0是因为source点没有计入，所以不是>=0
            while deque and cnt>0:
                #广度优先搜索
                x, y = deque[0]
                del deque[0]
                for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if nx in range(1000000) and ny in range(1000000) and [nx, ny] not in blocked and (nx, ny) not in visited:
                        #搜索非障碍方格的的时候发现了target，则能到达
                        if (nx, ny)==(fx, fy):
                            return 1
                        deque.append((nx, ny))
                        visited.add((nx, ny))
                        cnt -= 1
            #搜索完成后非障碍方格数量小于cnt，说明source点被包围了
            if cnt > 0:
                return -1
            #如果cnt=0，说明source没被包围
            return 0
        if (result:=wfs(source, target)) == 1:
            return True
        elif result == -1:
            return False
        else:
            #如果source没被包围，则查看target是否被包围了，若也没被包围，返回True，包围了返回False
            if (result_2:=wfs(target, source)) == -1:
                return False
            else:
                return True
