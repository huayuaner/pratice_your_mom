# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

class Solution:
    def numTrees(self, n: int) -> int:
        # dfs
        # def helper(l, r):
        #     if r - l <= 1:
        #         return 1
        #     ans = 0

        #     for i in range(l, (l+r)//2):
        #         left = helper(l,i)
        #         right = helper(i+1,r)
        #         ans += 2* left * right
        #     # print(ans)
        #     if (r-l)%2==1:
        #         m = l + (r-l)//2
        #         ans += helper(l, m) * helper(m+1, r)
        #     return ans
        # return helper(0, n)

        # 动态规划
        dp = [0] *(n+1)
        # dp[i]表示dp[i]能构成的二叉搜索树个数
        # 0 个只有一种
        dp[0] = 1
        # 1 个只有一种
        dp[1] = 1
        # dp[2] = 1
        # 遍历至末尾
        for i in range(2, n+1):
            # j表示选第几个做根节点
            for j in range(1,i+1):
                # dp[j-1]表示左边的个数, i-j表示右边的个数
                dp[i] += dp[j-1] * dp[i-j]
        return dp[-1]