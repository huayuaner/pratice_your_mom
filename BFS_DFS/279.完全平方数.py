给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

 

示例 1：

输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4
示例 2：

输入：n = 13
输出：2
解释：13 = 4 + 9
class Solution:
    def numSquares(self, n: int) -> int:
        # if n == 1:
        #     return 1
        # total_square = []
        # # 防止n=1时 不遍历
        # for i in range(1, n+1):
        #     if (tmp:=pow(i,2)) > n:
        #         break
        #     total_square.append(tmp)
        
        # dp = [float("inf")]*(n+1)
        # dp[0] = 0
        # for num in total_square:
        #     for x in range(1,n+1):
        #         if x-num >=0:
        #             dp[x] = min(dp[x],dp[x-num]+1)
        
        # return dp[n]
        
       