# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
#
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
#
# 你可以认为每种硬币的数量是无限的。
#
#  
#
# 示例 1：
#
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
# 示例 2：
#
# 输入：coins = [2], amount = 3
# 输出：-1
# 示例 3：
#
# 输入：coins = [1], amount = 0
# 输出：0

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bfs
        # if amount == 0:
        #     return 0
        # pq = [0]
        # Set = set()
        # Set.add(0)
        # step = 0
        # while pq:
        #     step += 1
        #     for _ in range(len(pq)):
        #         cur = pq.pop(0)
                
        #         for coin in coins:
        #             if cur+coin < amount and (cur+coin) not in Set:
        #                 pq.append(cur+coin)
        #                 Set.add(cur+coin)
        #             if cur+coin == amount:
        #                 return step

        # return -1

        # dfs
        # 将函数调用结果放入缓存
        # @functools.lru_cache(amount)
        # def dfs(res):
        #     if res < 0:
        #         return -1
        #     if res == 0:
        #         return 0
        #     step = float("inf")
        #     for coin in coins:
        #         rest = dfs(res-coin)
        #         # 这里加入了比较rest<step，因为这里需要比较所以把step设置为极大值会更好
        #         if rest >= 0 and rest < step:
        #             step = rest + 1
        #     return step if step!=float("inf") else -1
        # if amount<1:return 0
        # return dfs(amount)

        # 动态规划 dp[i]代表到达面额i的最少步骤
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for x in range(1,amount+1):
            for coin in coins:
                # x位置的值是dp[i-coin]之中最小的值+1
                if x-coin >=0:
                    dp[x] = min(dp[x], dp[x-coin]+1)
        return dp[amount] if dp[amount]!=float("inf") else -1
        

