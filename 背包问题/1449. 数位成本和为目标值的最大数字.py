# 给你一个整数数组 cost 和一个整数 target 。请你返回满足如下规则可以得到的 最大 整数：
#
# 给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。
# 总成本必须恰好等于 target 。
# 添加的数位中没有数字 0 。
# 由于答案可能会很大，请你以字符串形式返回。
#
# 如果按照上述要求无法得到任何整数，请你返回 "0" 。
#
#  
#
# 示例 1：
#
# 输入：cost = [4,3,2,5,6,7,2,5,5], target = 9
# 输出："7772"
# 解释：添加数位 '7' 的成本为 2 ，添加数位 '2' 的成本为 3 。所以 "7772" 的代价为 2*3+ 3*1 = 9 。 "977" 也是满足要求的数字，但 "7772" 是较大的数字。
#  数字     成本
#   1  ->   4
#   2  ->   3
#   3  ->   2
#   4  ->   5
#   5  ->   6
#   6  ->   7
#   7  ->   2
#   8  ->   5
#   9  ->   5
# 示例 2：
#
# 输入：cost = [7,6,5,5,5,6,8,7,8], target = 12
# 输出："85"
# 解释：添加数位 '8' 的成本是 7 ，添加数位 '5' 的成本是 5 。"85" 的成本为 7 + 5 = 12 。
# 示例 3：
#
# 输入：cost = [2,4,6,2,4,6,4,4,4], target = 5
# 输出："0"
# 解释：总成本是 target 的条件下，无法生成任何整数。
# 示例 4：
#
# 输入：cost = [6,10,15,40,40,40,40,40,40], target = 47
# 输出："32211"
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # 超时的原因应该是计算字符串的加减和字符串大小比较造成的
        # dp[i][j] 表示 前i个数 的成本为j的最长字符串长度
        # n = len(cost)
        # # dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
        # dp = [0 for _ in range(target+1)]
        # for j in range(1,target+1):
        #     # dp[0][j] = float("-inf")
        #     dp[j] = float('-inf')
        # # s = [['' for _ in range(target+1)] for _ in range(n+1)]
        # s = ['' for _ in range(target+1)]
        # # ans = ''
        # for i in range(1, n+1):
        #     for j in range(target, 0, -1):
        #         # 当前值不选
        #         # dp[i][j] = dp[i-1][j]
        #         # s[i][j] = s[i-1][j]
        #         # 当前值选k个
        #         k = 1
        #         while k*cost[n-i] <= j:
        #             if dp[j-k*cost[n-i]] + k > dp[j]:
        #                 dp[j] = dp[j-k*cost[n-i]] + k
        #                 s[j] = s[j-k*cost[n-i]] + k*str(n-i+1)
        #             elif dp[j-k*cost[n-i]] + k == dp[j]:
        #                 s[j] = max(s[j-k*cost[n-i]] + k*str(n-i+1), s[j])

        #             k += 1
        # # print(dp)
        # return s[-1] if dp[-1]!=float('-inf') else '0'

        # n = len(cost)
        # # 计算最长长度的
        # dp = [[float('-inf') for _ in range(target+1)] for _ in range(n+1)]
        # dp[0][0] = 0
        # # for j in range(1, target+1):
        # #     dp[0][j] = float('-inf')
        # for i in range(1,n+1):
        #     # 完全背包 ，不用在意覆盖的情况
        #     for j in range(target+1):
        #         dp[i][j] = dp[i-1][j]
        #         if j >= cost[i-1]:
        #             dp[i][j] = max(dp[i][j], dp[i][j-cost[i-1]] + 1)
        # if dp[-1][-1]<0:
        #     return '0'
        # # print(dp[-1][-1])
        # ans = []
        # j = target
        # for i in range(8,-1,-1):
        #     c = cost[i]
        #     # print(ans)
        #     # 由于是完全背包，这个时候的状态都是从这一项左边转换来的，所以只用最后一行
        #     while j>=c and dp[i+1][j] == dp[i+1][j-c] + 1:
        #         ans.append(str(i+1))
        #         j -= c
        # # print(j)
        # return "".join(ans)

        n = len(cost)
        dp = [float('-inf')] * (target + 1)
        dp[0] = 0
        for i in range(n):
            c = cost[i]
            for j in range(c, target + 1):
                dp[j] = max(dp[j], dp[j - c] + 1)
        if dp[-1] == float('-inf'):
            return '0'
        ans = []
        j = target
        for i in range(8, -1, -1):
            c = cost[i]
            while j >= c and dp[j] == dp[j - c] + 1:
                ans.append(str(i + 1))
                j -= c
        return ''.join(ans)









