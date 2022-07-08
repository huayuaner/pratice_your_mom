# 存在一棵无向连通树，树中有编号从 0 到 n - 1 的 n 个节点， 以及 n - 1 条边。
#
# 给你一个下标从 0 开始的整数数组 nums ，长度为 n ，其中 nums[i] 表示第 i 个节点的值。另给你一个二维整数数组 edges ，长度为 n - 1 ，其中 edges[i] = [ai, bi] 表示树中存在一条位于节点 ai 和 bi 之间的边。
#
# 删除树中两条 不同 的边以形成三个连通组件。对于一种删除边方案，定义如下步骤以计算其分数：
#
# 分别获取三个组件 每个 组件中所有节点值的异或值。
# 最大 异或值和 最小 异或值的 差值 就是这一种删除边方案的分数。
# 例如，三个组件的节点值分别是：[4,5,7]、[1,9] 和 [3,3,3] 。三个异或值分别是 4 ^ 5 ^ 7 = 6、1 ^ 9 = 8 和 3 ^ 3 ^ 3 = 3 。最大异或值是 8 ，最小异或值是 3 ，分数是 8 - 3 = 5 。
# 返回在给定树上执行任意删除边方案可能的 最小 分数。
#
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        grid = [[] for _ in range(n)]
        for a,b in edges:
            grid[a].append(b)
            grid[b].append(a)
        # xor, in_, out_, clock分别是异或数组，各个节点进入的时间，出来的时间，和时间戳
        xor, in_, out_, clock = [0]*n, [0]*n, [0]*n, 0
        def dfs(x, parent):
            nonlocal clock
            clock += 1
            # 记录进入时间
            in_[x] = clock
            xor[x] = nums[x]
            for y in grid[x]:
                # 往下搜除了父节点之外的节点
                if y!=parent:
                    dfs(y,x)
                    xor[x] ^= xor[y]
            # 记录出来的时间
            out_[x] = clock
        # 把0当作父节点
        dfs(0,-1)
        ans = float('inf')
        # 遍历边
        # i从2 j从1确保可以分成三份
        for i in range(2, n):
            for j in range(1, i):
                if in_[i]<in_[j]<=out_[i]: # i 是 j 的祖先 分出的三部分是根，子树，子树的子树
                    x, y, z = xor[j], xor[i]^xor[j], xor[0]^xor[i]
                elif in_[j]<in_[i]<=out_[j]:# j 是 i 的祖先 分出的三部分是根，子树，子树的子树
                    x, y, z = xor[i], xor[j]^xor[i], xor[0]^xor[j]
                else: # 分出的子树是根，左子树，右子树
                    x, y, z = xor[i], xor[j], xor[0]^xor[i]^xor[j]
                ans = min(ans, max(x,y,z)-min(x,y,z))
                if ans == 0:
                    return ans
        return ans