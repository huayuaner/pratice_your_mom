# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
#
#  
#
# 示例:
#
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数
#
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 堆+哈希
        # uglyNum = [2, 3, 5]
        # seen = {1}
        # pq = [1]
        # for _ in range(n-1):
        #     # 每次都得到队列里最小的数
        #     # 循环n-1次就可以pop掉n-1个最小的数
        #     cur = heappop(pq)
        #     # 只用最小的数过一遍丑数
        #     for i in uglyNum:
        #         #print(i, cur)
        #         if (num:=i*cur) not in seen:
        #             seen.add(num)
        #             heappush(pq, num)
        # return heappop(pq)

        # 动态规划
        # dp[i]代表第从小到大的第i个丑数
        dp = [0] * (n + 1)
        dp[1] = 1
        # 乘2，乘3，乘5的初始位置
        p2, p3, p5 = 1, 1, 1
        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            # dp[i]为三者最小
            dp[i] = min(num2, num3, num5)
            # pointer2, 指向1, 2, 3, 4, 5, 6中，还没使用乘2机会的丑数的位置。该指针的前一位已经使用完了乘以2的机会。
            # pointer3, 指向1, 2, 3, 4, 5, 6中，还没使用乘3机会的丑数的位置。该指针的前一位已经使用完了乘以3的机会。
            # pointer5, 指向1, 2, 3, 4, 5, 6中，还没使用乘5机会的丑数的位置。该指针的前一位已经使用完了乘以5的机会。
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        # print(dp)
        return dp[n]









