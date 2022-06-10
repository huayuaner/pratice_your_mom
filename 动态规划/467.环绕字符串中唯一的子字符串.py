# 把字符串 s 看作是 “abcdefghijklmnopqrstuvwxyz” 的无限环绕字符串，所以 s 看起来是这样的：
#
# "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd...." . 
# 现在给定另一个字符串 p 。返回 s 中 唯一 的 p 的 非空子串 的数量 。 
#
#  
#
# 示例 1:
#
# 输入: p = "a"
# 输出: 1
# 解释: 字符串 s 中只有一个"a"子字符。
# 示例 2:
#
# 输入: p = "cac"
# 输出: 2
# 解释: 字符串 s 中的字符串“cac”只有两个子串“a”、“c”。.
# 示例 3:
#
# 输入: p = "zab"
# 输出: 6
# 解释: 在字符串 s 中有六个子串“z”、“a”、“b”、“za”、“ab”、“zab”。
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        # dp[i]记录以字母p[i-1]为结尾的字符的最长子串
        # 如果只都记录前i位会出现 abbab其中ab会被记录两次
        n = len(p)
        cnts = [0] * 26
        cnt = 1
        for i in range(n):
            if i > 0 and (ord(p[i]) - ord(p[i - 1])) % 26 == 1:  # (0-25)%26 == 1
                cnt += 1
            else:
                cnt = 1
            cnts[ord(p[i]) - ord('a')] = max(cnts[ord(p[i]) - ord('a')], cnt)
        return sum(cnts)

