# 给你一个字符串数组 words 。words 中每个元素都是一个包含 两个 小写英文字母的单词。
#
# 请你从 words 中选择一些元素并按 任意顺序 连接它们，并得到一个 尽可能长的回文串 。每个元素 至多 只能使用一次。
#
# 请你返回你能得到的最长回文串的 长度 。如果没办法得到任何一个回文串，请你返回 0 。
#
# 回文串 指的是从前往后和从后往前读一样的字符串。
#
from collections import Counter


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnts = Counter(words)
        ans = 0
        center_double = False
        for key in cnts.keys():
            if cnts[key] == 0:
                continue
            if key[0] == key[1]:
                # ans += cnts[key]*2
                # max_double = max(max_double, cnts[key])
                ans += cnts[key] // 2 * 4
                if cnts[key] % 2 == 1: center_double = True
                cnts[key] = 0
            elif (tmp := key[1] + key[0]) in cnts:
                ans += min(cnts[key], cnts[tmp]) * 4
                cnts[key] = 0
                cnts[tmp] = 0
        ans += 2 if center_double else 0
        return ans

        # break
