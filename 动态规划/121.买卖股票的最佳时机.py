# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
#
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
#
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
#
#  
#
# 示例 1：
#
# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
# 示例 2：
#
# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这种情况下, 没有交易完成, 所以最大利润为 0。

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 单调减栈
        # 记录弹出的最低价格
        # 记录最大差值
        # stack = []
        # ans = 0
        # min_price = float("inf")
        # for price in prices:
        #     while stack and stack[-1] < price:
        #         min_price = min(min_price, stack.pop())
        #         ans = max(ans, price - min_price)
        #     stack.append(price)
        # return ans

        # 动态规划
        # dp[i]代表第i个price的与之前最小值
        # dp = [float("inf")] * len(prices)
        # ans = 0
        # for i in range(1, len(prices)):
        #     dp[i] = min(prices[i-1], dp[i-1])
        #     ans = max(prices[i]- dp[i], ans)
        # return ans
        #
        # 状态 0 cash in hand after selling 卖了股票后钱在手
        # 状态 1 stock in hand 股票在手
        dp = [[0,0] for _ in range(len(prices))]
        # 第一天买了股票，利润为-price[0]
        # 第一天不可能卖，所以为0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            # 这一天手上的钱可能是前一天手上的钱或者前一天手上的股票今天卖了的钱
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # 这一天手上的股票可能是前一天手上的股票或者今天刚买的股票
            dp[i][1] = max(dp[i-1][1],-prices[i])
        return dp[-1][0]




