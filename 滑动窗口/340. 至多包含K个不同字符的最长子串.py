# 给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。
#
#  
#
# 示例 1:
#
# 输入: s = "eceba", k = 2
# 输出: 3
# 解释: 则 T 为 "ece"，所以长度为 3。
# 示例 2:
#
# 输入: s = "aa", k = 1
# 输出: 2
# 解释: 则 T 为 "aa"，所以长度为 2。

from collections import Counter


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # if k==0:
        #     return 0
        # cnts = Counter()
        # ans = 0
        # l = r = 0
        # n = len(s)
        # while r<n:
        #     cnts[s[r]] += 1
        #     while len(cnts)>k:
        #         cnts[s[l]] -= 1
        #         if cnts[s[l]] == 0:
        #             del cnts[s[l]]
        #         l += 1

        #     ans = max(ans, r-l+1)
        #     r += 1
        # return ans

        if k == 0:
            return 0
        n = len(s)
        l = r = 0
        ans = 0
        dic = dict()
        while r < n:
            dic[s[r]] = r
            if len(dic) > k:
                del_idx = min(dic.values())
                del dic[s[del_idx]]
                l = del_idx + 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans




