# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
#
#  
#
# 示例 1:
#
# 输入: 12258
# 输出: 5
# 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

class Solution:
    def translateNum(self, num: int) -> int:
        # 动态规划
        # dp[i]代表前i个字符有几种表现形式
        # s = str(num)
        # n = len(s)
        # dp = [0] * n

        # dp[0] = 1
        # for i in range(1, n):
        #     n = s[i-1:i+1]
        #     if i != 1:
        #         if 10<=int(n)<=25:
        #             dp[i] = dp[i-2] + dp[i-1]

        #         else:
        #             dp[i] = dp[i-1]
        #     else:

        #         dp[i] = dp[i-1] + 1 if 10<=int(n)<=25 else dp[i-1]
        # #print(dp)
        # return dp[-1]

        # dfs
        if num < 10:
            return 1
        # 末尾两个数在 能表示的范围
        if 9 < num % 100 < 26:
            # num//10表示末尾用单个字符表示，num//100 表示末尾两个数用一个字符表示
            return self.translateNum(num // 10) + self.translateNum(num // 100)
        else:
            # 末尾俩数不在能表示的范围，用单字符表示末尾
            return self.translateNum(num // 10)



