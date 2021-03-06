# 有效括号字符串为空 ""、"(" + A + ")" 或 A + B ，其中 A 和 B 都是有效的括号字符串，+ 代表字符串的连接。
#
# 例如，""，"()"，"(())()" 和 "(()(()))" 都是有效的括号字符串。
# 如果有效字符串 s 非空，且不存在将其拆分为 s = A + B 的方法，我们称其为原语（primitive），其中 A 和 B 都是非空有效括号字符串。
#
# 给出一个非空有效字符串 s，考虑将其进行原语化分解，使得：s = P_1 + P_2 + ... + P_k，其中 P_i 是有效括号字符串原语。
#
# 对 s 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 s 。
#
#  
#
# 示例 1：
#
# 输入：s = "(()())(())"
# 输出："()()()"
# 解释：
# 输入字符串为 "(()())(())"，原语化分解得到 "(()())" + "(())"，
# 删除每个部分中的最外层括号后得到 "()()" + "()" = "()()()"。
# 示例 2：
#
# 输入：s = "(()())(())(()(()))"
# 输出："()()()()(())"
# 解释：
# 输入字符串为 "(()())(())(()(()))"，原语化分解得到 "(()())" + "(())" + "(()(()))"，
# 删除每个部分中的最外层括号后得到 "()()" + "()" + "()(())" = "()()()()(())"。
# 示例 3：
#
# 输入：s = "()()"
# 输出：""
# 解释：
# 输入字符串为 "()()"，原语化分解得到 "()" + "()"，
# 删除每个部分中的最外层括号后得到 "" + "" = ""。
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # stack = []
        # primitive = []
        # balance = 0
        # head = 0
        # for i,c in enumerate(s):
        #     if c == '(':
        #         balance += 1
        #     else:
        #         balance -= 1
        #     if balance == 0:
        #         primitive.append(s[head+1:i])
        #         head = i + 1
        # return ''.join(primitive)

        ans, level = '', 0
        for c in s:
            # 这个判断的顺序很妙
            # 原语当level为0时就是一个单独的原语，而我们需要的是原语内部的内容
            # 先进行右括号的判定，由此判断当前的内容是不是原语内部的内容
            # 再进行左括号的判定
            if c ==')':
                level -= 1
            if level:
                ans += c
            if c == '(':
                level += 1
        return ans 