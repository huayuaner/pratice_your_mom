# 给定一个正整数 n，返回 连续正整数满足所有数字之和为 n 的组数 。 
#
#  
#
# 示例 1:
#
# 输入: n = 5
# 输出: 2
# 解释: 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。
# 示例 2:
#
# 输入: n = 9
# 输出: 3
# 解释: 9 = 4 + 5 = 2 + 3 + 4
# 示例 3:
#
# 输入: n = 15
# 输出: 4
# 解释: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
#
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # dp[i][j]
        # 肯定包含其本身
        # ans = 1
        # length = 2
        # while length < n:
        #     # 初始化

        #     total = sum([i+1 for i in range(length)])
        #     # print(total, length)
        #     if total >= n:
        #         ans += (1 if total==n else 0)
        #         break
        #     for i in range(length+1,n):
        #         total += length
        #         # print(total,length)
        #         if total >= n:
        #             ans += (1 if total==n else 0)
        #             break
        #     length += 1
        # return ans

        # ans = 1
        # length = 2
        # total = 3
        # while length<n:
        #     if total >= n:
        #         ans += (1 if total==n else 0)
        #         break
        #     if (n - total)%length == 0:
        #         ans += 1
        #     length += 1
        #     total += length
        # return ans

        #
        cnt = 1
        for length in range(2, n):
            a = (2 * n + length - length * length) // (2 * length)
            # print(a,length)
            if a < 1:
                break
            if (2 * a + length - 1) * length // 2 == n:
                cnt += 1
        return cnt



