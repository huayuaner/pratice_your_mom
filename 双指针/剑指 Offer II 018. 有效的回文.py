# 给定一个字符串 s ，验证 s 是否是 回文串 ，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 本题中，将空字符串定义为有效的 回文串 。

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # stack = []
        # for c in s:
        #     if c.isdigit() or c.isalpha():
        #         # print(c)
        #         if c.isalpha():
        #             c = c.upper()
        #         stack.append(c)
        # # print(stack)
        # return stack == stack[::-1]

        # 在源字符串上
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            # 判断是不是字母或数字

            while l < r and not s[r].isalnum():
                r -= 1
            while l < r and not s[l].isalnum():
                l += 1
            # if l<r:
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True