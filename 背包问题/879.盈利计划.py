# 集团里有 n 名员工，他们可以完成各种各样的工作创造利润。
#
# 第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。
#
# 工作的任何至少产生 minProfit 利润的子集称为 盈利计划 。并且工作的成员总数最多为 n 。
#
# 有多少种计划可以选择？因为答案很大，所以 返回结果模 10^9 + 7 的值。
#
#  
#
# 示例 1：
#
# 输入：n = 5, minProfit = 3, group = [2,2], profit = [2,3]
# 输出：2
# 解释：至少产生 3 的利润，该集团可以完成工作 0 和工作 1 ，或仅完成工作 1 。
# 总的来说，有两种计划。
# 示例 2：
#
# 输入：n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
# 输出：7
# 解释：至少产生 5 的利润，只要完成其中一种工作就行，所以该集团可以完成任何工作。
# 有 7 种可能的计划：(0)，(1)，(2)，(0,1)，(0,2)，(1,2)，以及 (0,1,2) 。
#
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        # 找利益合法的子集
        # 再找合法子集里人数合法的子集
        mod = 10**9+7
        length = len(group)
        # 有两个限制条件：人数， 利益
        # dp[i][j][k]表示前i个任务，恰好用j人，最低利益为k的方案数
        # dp = [[[0 for _ in range(minProfit+1)]for _ in range(n+1)]for _ in range(length+1)]
        # # 初始化
        # # 这句初始化对应恰好j个人
        # # dp[0][0][0] = 1
        # # 最多j个人的初始化
        # for i in range(length+1):
        #     for j in range(n+1):
        #         dp[i][j][0] = 1
        # for i in range(1, length+1):
        #     g, p = group[i-1], profit[i-1]
        #     for j in range(n+1):
        #         for k in range(minProfit+1):
        #             # 可用人数小于当前任务需要人数
        #             if j<g:
        #                 dp[i][j][k] = dp[i-1][j][k]
        #             else:
        #                 dp[i][j][k] = (dp[i-1][j][k] + dp[i-1][j-g][max(0, k-p)])%mod
        # # print(dp[-1][-1][-1])
        # # 为什么这里要求和
        # # 原因在于定义 dp[i][j][k]表示恰好用了j个人， 而不是最多用j个人
        # # 最多用j个人的初始化需要将 dp[i][j][0]都设置为 1
        # # return sum(dp[length][j][minProfit] for j in range(n+1))%mod
        # return dp[-1][-1][-1]

        dp = [[0 for _ in range(minProfit+1)] for _ in range(n+1)]
        for j in range(n+1):
            dp[j][0] = 1
        for i in range(length):
            g, p = group[i], profit[i]
            for j in range(n, g-1, -1):
                for k in range(minProfit, -1, -1):
                    # if j >= g:
                    dp[j][k] = (dp[j][k]+dp[j-g][max(0,k-p)])%mod
        return dp[-1][-1]






