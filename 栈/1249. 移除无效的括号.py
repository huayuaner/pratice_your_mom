# 给你一个由 '('、')' 和小写字母组成的字符串 s。
#
# 你需要从字符串中删除最少数目的 '(' 或者 ')' （可以删除任意位置的括号)，使得剩下的「括号字符串」有效。
#
# 请返回任意一个合法字符串。
#
# 有效「括号字符串」应当符合以下 任意一条 要求：
#
# 空字符串或只包含小写字母的字符串
# 可以被写作 AB（A 连接 B）的字符串，其中 A 和 B 都是有效「括号字符串」
# 可以被写作 (A) 的字符串，其中 A 是一个有效的「括号字符串」
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # stack = []
        # ans = []
        # for c in s:
        #     if c.isalpha():
        #         ans.append(c)
        #     elif c =='(':
        #         stack.append(len(ans))
        #         ans.append('(')
        #     else:
        #         if stack:
        #             stack.pop()
        #             ans.append(')')
        # for idx in reversed(stack):
        #     del ans[idx]
        # return ''.join(ans)

        # 两次遍历
        def helper(s, open_, end):
            ans = []
            balance = 0
            for c in s:
                if c == open_:
                    balance += 1
                elif c == end:
                    if balance == 0:
                        continue
                    balance -= 1
                ans.append(c)
            return ''.join(ans)
        s = helper(s, '(',')')

        s = helper(s[::-1], ')','(')
        return s[::-1]
