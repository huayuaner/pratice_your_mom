# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
#
#  
#
# 示例 1：
#
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
# 示例 2：
#
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
# 示例 3：
#
# 输入：s = ""
# 输出：0

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #主旨思想：具体做法是我们始终保持栈底元素为当前已经遍历过的元素中「最后一个没有被匹配的右括号的下标」
        ans = 0
        st = [-1]
        for idx,c in enumerate(s):
            if c == '(':
                st.append(idx)
            else:
                st.pop()
                if st:
                    ans = max(ans, idx - st[-1])
                else:
                    st.append(idx)
        return ans
