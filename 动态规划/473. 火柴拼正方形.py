# 你将得到一个整数数组 matchsticks ，其中 matchsticks[i] 是第 i 个火柴棒的长度。你要用 所有的火柴棍 拼成一个正方形。你 不能折断 任何一根火柴棒，但你可以把它们连在一起，而且每根火柴棒必须 使用一次 。
#
# 如果你能使这个正方形，则返回 true ，否则返回 false 。
#
# 输入: matchsticks = [1,1,2,2,2]
# 输出: true
# 解释: 能拼成一个边长为2的正方形，每边两根火柴。
# 示例 2:
#
# 输入: matchsticks = [3,3,3,3,4]
# 输出: false
# 解释: 不能用所有火柴拼成一个正方形。

from collections import Counter


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        total = sum(matchsticks)
        if total % 4:
            return False
        length = total // 4
        # dfs
        # 预先对matchsticks做排序可以使得不合法的快速返回False
        # matchsticks.sort(reverse=True)
        # edges = [0]*4
        # def dfs(index):
        #     if index == len(matchsticks):
        #         return True
        #     nonlocal edges
        #     for i in range(4):
        #         edges[i] += matchsticks[index]
        #         if edges[i] <= length and dfs(index+1):
        #             return True
        #         edges[i] -= matchsticks[index]
        #     return False
        # return dfs(0)

        # (1<<len(matchsticks)) 作为二进制可以表示每一个火柴或选或不选
        dp = [-1] * (1 << len(matchsticks))
        # print(dp, len(dp))
        # 0代表一个边的开始和上一个边的结束
        dp[0] = 0
        for s in range(1, len(dp)):
            for i, ma in enumerate(matchsticks):
                # 当前状态s没有选择第i个值
                if s & (1 << i) == 0:
                    continue
                    # 去找 s未选择 i火柴的状态
                s1 = s - (1 << i)
                # 如果s1的状态合法（也就是是从dp[0]转换出来的）
                if dp[s1] >= 0 and dp[s1] + ma <= length:
                    # 如果加和为length 代表这个边结束了，下一个开始了，使用%length让其为0
                    dp[s] = (dp[s1] + ma) % length
                    # 该状态转换完成 break出来
                    break
            # print(dp)
        return dp[-1] == 0







