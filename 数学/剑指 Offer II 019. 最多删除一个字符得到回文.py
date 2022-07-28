# 给定一个非空字符串 s，请判断如果 最多 从字符串中删除一个字符能否得到一个回文字符串。

class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            # 不相同
            else:
                # 删去左或删去右
                return s[l + 1:r + 1] == s[l + 1:r + 1][::-1] or s[l:r] == s[l:r][::-1]
        return True


