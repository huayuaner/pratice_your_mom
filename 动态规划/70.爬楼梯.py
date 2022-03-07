# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
#  
#
# 示例 1：
#
# 输入：n = 2
# 输出：2
# 解释：有两种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶
# 2. 2 阶
# 示例 2：
#
# 输入：n = 3
# 输出：3
# 解释：有三种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶 + 1 阶
# 2. 1 阶 + 2 阶
# 3. 2 阶 + 1 阶

class Solution:
    @functools.lru_cache(None)
    def climbStairs(self, n: int) -> int:
        # if n<2:
        #     return 1
        # dp = [0] * (n+1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3,n+1):
        #     for step in [1,2]:
        #         dp[i] += dp[i-step]
        # print(dp)
        # return dp[n]

        # 优化
        # if n<2:
        #     return 1
        # pre,pos,r = 1, 2, 2
        # while r<n:
        #     tmp = pre + pos
        #     pre = pos
        #     pos = tmp
        #     r+=1
        # return pos

        # 递归
        
        return n if n<=2 else self.climbStairs(n-1)+self.climbStairs(n-2)


