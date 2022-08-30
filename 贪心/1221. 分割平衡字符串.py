# 在一个 平衡字符串 中，'L' 和 'R' 字符的数量是相同的。
#
# 给你一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。
#
# 注意：分割得到的每个字符串都必须是平衡字符串，且分割得到的平衡字符串是原平衡字符串的连续子串。
#
# 返回可以通过分割得到的平衡字符串的 最大数量 。
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # 遇到L +1遇到R -1
        # 贪心
        cnt = 0
        ans = 0
        for c in s:
            if c == 'L':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                ans += 1
        return ans