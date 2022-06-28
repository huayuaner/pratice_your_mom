# 给你两个整数 m 和 n ，分别表示一块矩形木块的高和宽。同时给你一个二维整数数组 prices ，其中 prices[i] = [hi, wi, pricei] 表示你可以以 pricei 元的价格卖一块高为 hi 宽为 wi 的矩形木块。
#
# 每一次操作中，你必须按下述方式之一执行切割操作，以得到两块更小的矩形木块：
#
# 沿垂直方向按高度 完全 切割木块，或
# 沿水平方向按宽度 完全 切割木块
# 在将一块木块切成若干小木块后，你可以根据 prices 卖木块。你可以卖多块同样尺寸的木块。你不需要将所有小木块都卖出去。你 不能 旋转切好后木块的高和宽。
#
# 请你返回切割一块大小为 m x n 的木块后，能得到的 最多 钱数。
#
# 注意你可以切割木块任意次。
#
import functools
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        # 动态规划

        # 处理 prices
        dic = dict()
        for h,w,p in prices:
            dic[(h,w)] = p
        # print(dic)
        # dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # for i in range(1,m+1):
        #     for j in range(1,n+1):
        #         dp[i][j] = max(dic.get((i,j), 0), max((dp[i][k]+dp[i][j-k] for k in range(1, j//2+1)), default=0),max((dp[k][j]+dp[i-k][j] for k in range(1, i//2+1)),default=0))
        #         # 竖着切一刀
        #         # if j > 2:
        #         # dp[i][j] =
        #         # 横着切一刀
        #         # if i>2:
        #         # dp[i][j] =
        # # print(dp)
        # return dp[-1][-1]

        # 记忆化dfs
        @functools.lru_cache(None)
        def helper(x,y):
            if (x,y) in dic:
                ans =  dic[(x,y)]
            else:
                ans = 0
            for i in range(1, x//2+1):
                ans = max(ans, helper(i,y)+helper(x-i,y))
            for j in range(1, y//2+1):
                ans = max(ans, helper(x, j)+helper(x,y-j))
            return ans
        return helper(m,n)