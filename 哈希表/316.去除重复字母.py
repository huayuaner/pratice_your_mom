# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
#
# 示例 1：
#
# 输入：s = "bcabc"
# 输出："abc"
# 示例 2：
#
# 输入：s = "cbacdcbc"
# 输出："acdb"
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        #stack记录答案，cnt记录字符出现次数
        stack = []
        cnt = Counter(s)
        # seen = set() 这一步是空间换时间
        for c in s:
            #对于不在stack中的字符，采取保证字典序最小措施
            if c not in stack: #if c not in seen:这一步时间复杂度为1，原来的为N
                while stack and c<stack[-1] and cnt[stack[-1]]>0:
                    stack.pop()
                #seen.add(c)
                stack.append(c)
            cnt[c] -= 1
        return ''.join(stack)
