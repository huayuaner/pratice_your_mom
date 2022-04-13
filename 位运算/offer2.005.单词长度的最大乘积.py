# 给定一个字符串数组 words，请计算当两个字符串 words[i] 和 words[j] 不包含相同字符时，它们长度的乘积的最大值。假设字符串中只包含英语的小写字母。如果没有不包含相同字符的一对字符串，返回 0。
#
#  
#
# 示例 1:
#
# 输入: words = ["abcw","baz","foo","bar","fxyz","abcdef"]
# 输出: 16
# 解释: 这两个单词为 "abcw", "fxyz"。它们不包含相同字符，且长度的乘积最大。
# 示例 2:
#
# 输入: words = ["a","ab","abc","d","cd","bcd","abcd"]
# 输出: 4
# 解释: 这两个单词为 "ab", "cd"。
# 示例 3:
#
# 输入: words = ["a","aa","aaa","aaaa"]
# 输出: 0
# 解释: 不存在这样的两个单词。
from itertools import product
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # 位运算
        # mask = []
        # for word in words:
        #     tmp = 0
        #     for c in word:
        #         tmp |= (1<<(ord(c)-ord('a')))
        #     mask.append(tmp)
        # ans = 0
        # n = len(words)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if not mask[i]&mask[j]:
        #             ans = max(ans, len(words[i])*len(words[j]))
        # return ans

        # 哈希表优化
        masks = defaultdict(int)
        for word in words:
            mask = reduce(lambda a, b: a | (1 << (ord(b) - ord('a'))), word, 0)
            masks[mask] = max(masks[mask], len(word))
        return max((masks[x] * masks[y] for x, y in product(masks, repeat=2) if x & y == 0), default=0)

