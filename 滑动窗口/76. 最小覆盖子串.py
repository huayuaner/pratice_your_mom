# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
#
#  
#
# 注意：
#
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。
#  
#
# 示例 1：
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 示例 2：
#
# 输入：s = "a", t = "a"
# 输出："a"
# 示例 3:
#
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 滑动窗口
        # 使用一个Counter字典记录窗口中的是否包含了t
        cnts = Counter(t)
        n = len(cnts)
        n_s, n_t = len(s), len(t)
        l = r = 0
        ans = ""
        while r<n_s:
            # 右指针遍历
            # 使用n记录未包含的字符
            while n and r<n_s:
                if s[r] in cnts:
                    cnts[s[r]] -= 1
                    if cnts[s[r]] == 0:
                        n -= 1
                r += 1
            # s 并不包含 t
            if r == n_s and n != 0:
                break
            # 左指针遍历
            # 使用左指针找第一个让窗口不包含t的位置
            while l<=r and n == 0:
                if s[l] in cnts:
                    cnts[s[l]] += 1
                    if cnts[s[l]] > 0:
                        n += 1
                l += 1
            # 比较长度
            if not ans or r-l+1<len(ans):
                ans = s[l-1:r]
        return ans

