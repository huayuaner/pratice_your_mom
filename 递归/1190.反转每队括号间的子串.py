# 给出一个字符串 s（仅含有小写英文字母和括号）。
#
# 请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
#
# 注意，您的结果中 不应 包含任何括号。
#
#  
#
# 示例 1：
#
# 输入：s = "(abcd)"
# 输出："dcba"
# 示例 2：
#
# 输入：s = "(u(love)i)"
# 输出："iloveu"
# 解释：先反转子字符串 "love" ，然后反转整个字符串。
# 示例 3：
#
# 输入：s = "(ed(et(oc))el)"
# 输出："leetcode"
# 解释：先反转子字符串 "oc" ，接着反转 "etco" ，然后反转整个字符串。
# 示例 4：
#
# 输入：s = "a(bcdefghijkl(mno)p)q"
# 输出："apmnolkjihgfedcbq"

class Solution:
    def reverseParentheses(self, s: str) -> str:
        # stack = []
        # ans = s
        # for i in range(len(s)):
        #     if s[i] == "(":
        #         stack.append(i)
        #     elif s[i] == ")":
        #         pre = stack.pop()

        #         s = s[:pre+1]+s[i-1:pre:-1] + s[i:]
        #         #print(s)
        # s = s.replace("(","")
        # s = s.replace(")","")
        # return s
        # stack = []
        # for c in s:
        #     if c!=")":
        #         stack.append(c)
        #     else:
        #         tmp = []
        #         while stack and stack[-1]!="(":
                        ##用pop完成逆序
        #             tmp.append(stack.pop())
        #         stack.pop()
        #         stack += tmp
        # return "".join(stack)

        n = len(s)
        pairs = [0] * n
        stack = []
        #预处理得到括号对的对应位置
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":

                pre = stack.pop()
                pos = i
                pairs[pre] = pos
                pairs[pos] = pre
        # 方向1向右-1向左
        step = 1
        index = 0
        ans = ""
        while index < n:
            #遇到括号则跳跃至对应位置
            if s[index] in [")", "("]:
                index = pairs[index]
                step = -step
            else:
                #非括号加入结果
                ans += s[index]
            index += step
        return ans








