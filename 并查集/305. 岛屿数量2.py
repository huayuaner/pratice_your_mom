# 给你一个大小为 m x n 的二进制网格 grid 。网格表示一个地图，其中，0 表示水，1 表示陆地。最初，grid 中的所有单元格都是水单元格（即，所有单元格都是 0）。
#
# 可以通过执行 addLand 操作，将某个位置的水转换成陆地。给你一个数组 positions ，其中 positions[i] = [ri, ci] 是要执行第 i 次操作的位置 (ri, ci) 。
#
# 返回一个整数数组 answer ，其中 answer[i] 是将单元格 (ri, ci) 转换为陆地后，地图中岛屿的数量。
#
# 岛屿 的定义是被「水」包围的「陆地」，通过水平方向或者垂直方向上相邻的陆地连接而成。你可以假设地图网格的四边均被无边无际的「水」所包围。
#
# 使用数组实现并查集
class UF:
    def __init__(self, N):
        # 初始化，每一个x的默认父亲是自己
        self.father = list(range(N))

    def find(self, x):
        # 如果x的父亲不是自己（还没找到最终祖先）
        # 就往下找，并更新父亲，只要父亲是祖先即可（路径压缩）
        if self.father[x] != x: self.father[x] = self.find(self.father[x])
        return self.father[x]

    def merge(self, x1, x2):
        # 如果x1，x2的相同，说明是一个集合里的
        if x1 == x2:
            return
            # 找到x1的祖先和x2的祖先
        x1_f = self.find(x1)
        x2_f = self.find(x2)
        # 如果祖先不同，将其合并，这里的谁是祖先都可以
        if x2_f != x1_f:
            self.father[x1_f] = x2_f


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ans = []
        island = 0
        uf = UF(m * n)
        seen = set()
        for x, y in positions:
            # 当前位置遍历过了
            if (x, y) in seen:
                ans.append(island)
                continue
            # 集合加上当前位置
            seen.add((x, y))
            # 计算当前idx
            idx = x * n + y
            # 首先假设岛屿+1
            island += 1
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                # 这个位置并没有出现岛屿，跳过
                if (nx, ny) not in seen:
                    continue
                    # 计算出现岛屿的idx2
                idx2 = nx * n + ny
                # 得到该位置和邻居位置的祖先
                father1, father2 = uf.find(idx), uf.find(idx2)
                # 如果祖先不一样，说明这个位置的出现将两边连起来了
                if father1 != father2:
                    # 合并
                    uf.merge(idx, idx2)
                    # 岛屿位置-1，因为二合一了
                    island -= 1
            # 将当前岛的数量加入ans中
            ans.append(island)
        return ans





