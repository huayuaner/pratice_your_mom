# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
#
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
#
#  
#
# 示例 1：
#
# 输入：n = 12
# 输出：3
# 解释：12 = 4 + 4 + 4
# 示例 2：
#
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9

class Solution:
    def numSquares(self, n: int) -> int:
        # 零钱兑换
        # 这题的零钱是平方数
        square = []
        def suqared(n):
            for i in range(1,n+1):
                if (tmp:=i**2)>n:
                    break
                square.append(tmp)
        suqared(n)
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(len(square)):
            for j in range(square[i],n+1):
                dp[j] = min(dp[j], dp[j-square[i]]+1)
        # print(dp,square)
        return dp[-1]
