# 给定两个字符串 s 和 t 。返回 s 中包含 t 的所有字符的最短子字符串。如果 s 中不存在符合条件的子字符串，则返回空字符串 "" 。
#
# 如果 s 中存在多个符合条件的子字符串，返回任意一个。
#
#  
#
# 注意： 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
#
#  
#
# 示例 1：
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最短子字符串 "BANC" 包含了字符串 t 的所有字符 'A'、'B'、'C'
# 示例 2：
#
# 输入：s = "a", t = "a"
# 输出："a"
# 示例 3：
#
# 输入：s = "a", t = "aa"
# 输出：""
# 解释：t 中两个字符 'a' 均应包含在 s 的子串中，因此没有符合条件的子字符串，返回空字符串

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 滑窗
        if len(t) > len(s):
            return ''
        # t中字符数量
        cnt = Counter(t)
        # t中字符种类
        len_t = len(t)
        len_s = len(s)
        n = len(cnt)
        l, r = 0, 0
        ans = ''
        while r < len_s:
            while n and r < len_s:
                if s[r] in cnt:
                    cnt[s[r]] -= 1
                    if cnt[s[r]] == 0:
                        n -= 1
                r += 1
            # print(l,r,n)
            # 搜到底都没搜全
            if r == len_s and n: break

            while not n and l < r:
                if s[l] in cnt:
                    cnt[s[l]] += 1
                    if cnt[s[l]] == 1:
                        n += 1
                # print(111)
                l += 1
            if not ans or len(ans) > r - l:
                # print(l,r)
                ans = s[l - 1:r]

        return ans

