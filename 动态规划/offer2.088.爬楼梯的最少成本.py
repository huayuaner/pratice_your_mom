# 数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。
#
# 每当爬上一个阶梯都要花费对应的体力值，一旦支付了相应的体力值，就可以选择向上爬一个阶梯或者爬两个阶梯。
#
# 请找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 动规
        n = len(cost)
        # dp = [0]*n
        # dp[0], dp[1] = cost[0], cost[1]
        # for i in range(2, n):
        #     dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        # return min(dp[-1], dp[-2])

        pp, p = cost[0], cost[1]
        for i in range(2,n):
            pp, p = p, min(pp,p) + cost[i]
            # print(pp, p)
        return min(pp, p)