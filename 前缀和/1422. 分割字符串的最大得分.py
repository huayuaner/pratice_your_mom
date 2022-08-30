# 给你一个由若干 0 和 1 组成的字符串 s ，请你计算并返回将该字符串分割成两个 非空 子字符串（即 左 子字符串和 右 子字符串）所能获得的最大得分。
#
# 「分割字符串的得分」为 左 子字符串中 0 的数量加上 右 子字符串中 1 的数量。
#
#  
#
# 示例 1：
#
# 输入：s = "011101"
# 输出：5
# 解释：
# 将字符串 s 划分为两个非空子字符串的可行方案有：
# 左子字符串 = "0" 且 右子字符串 = "11101"，得分 = 1 + 4 = 5
# 左子字符串 = "01" 且 右子字符串 = "1101"，得分 = 1 + 3 = 4
# 左子字符串 = "011" 且 右子字符串 = "101"，得分 = 1 + 2 = 3
# 左子字符串 = "0111" 且 右子字符串 = "01"，得分 = 1 + 1 = 2
# 左子字符串 = "01110" 且 右子字符串 = "1"，得分 = 2 + 1 = 3
class Solution:
    def maxScore(self, s: str) -> int:
        # n = len(s)
        # # score_r = score_l = 0
        # score_r = 0
        # score_l = 0 if s[0] == '1' else 1
        # for i in range(1,n):
        #     if s[i] == '1':
        #         score_r += 1
        # # print(score_l, score_r)
        # ans = score_r + score_l
        # for i in range(1, n-1):
        #     if s[i] == '0':
        #         score_l += 1
        #     else:
        #         score_r -= 1
        #     ans = max(ans, score_l + score_r)
        # return ans

        # 优雅写法
        # ans = score = int(s[0]=='0') + s[1:].count('1')

        # for c in s[1:-1]:
        #     score += (1 if c == '0' else -1)
        #     ans = max(ans,score)
        # return ans

        n, presum, ans = len(s), 0, -inf
        for i in range(n):
            # cur = presum + (n - i - final_presum + presum) = presum * 2 - i + (n - final_presum)
            if i and (cur := presum * 2 - i) > ans:
                ans = cur
            presum += s[i] == "0"
        return ans + n - presum