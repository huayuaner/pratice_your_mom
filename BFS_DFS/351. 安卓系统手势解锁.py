# 我们都知道安卓有个手势解锁的界面，是一个 3 x 3 的点所绘制出来的网格。用户可以设置一个 “解锁模式” ，通过连接特定序列中的点，形成一系列彼此连接的线段，每个线段的端点都是序列中两个连续的点。如果满足以下两个条件，则 k 点序列是有效的解锁模式：
#
# 解锁模式中的所有点 互不相同 。
# 假如模式中两个连续点的线段需要经过其他点的 中心 ，那么要经过的点 必须提前出现 在序列中（已经经过），不能跨过任何还未被经过的点。
# 例如，点 5 或 6 没有提前出现的情况下连接点 2 和 9 是有效的，因为从点 2 到点 9 的线没有穿过点 5 或 6 的中心。
# 然而，点 2 没有提前出现的情况下连接点 1 和 3 是无效的，因为从圆点 1 到圆点 3 的直线穿过圆点 2 的中心。
import functools


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:

        # graph 中保存从键到键中键需要经过的数字
        graph = {
            1: {3: 2, 7: 4, 9: 5},
            2: {8: 5},
            3: {1: 2, 7: 5, 9: 6},
            4: {6: 5},
            5: {},
            6: {4: 5},
            7: {1: 4, 3: 5, 9: 8},
            8: {2: 5},
            9: {1: 5, 3: 6, 7: 8},
        }

        @functools.lru_cache(None)
        def dfs(state, cnt, cur_num):
            # 结束
            if cnt == n:
                return 1
            cur_mode = 1 if cnt >= m else 0
            for i in range(1, 10):
                # 如果这个数字没有被使用
                if (1 << i) & state == 0:
                    # 如果cur_num到达i不需要经过值 或者 经过的值已经被选择了
                    if i not in graph[cur_num] or (1 << graph[cur_num][i] & state):
                        cur_mode += dfs(state | (1 << i), cnt + 1, i)
            return cur_mode

        ans = 0
        ans += 4 * dfs(1 << 1, 1, 1)
        ans += 4 * dfs(1 << 2, 1, 2)
        ans += dfs(1 << 5, 1, 5)
        return ans





