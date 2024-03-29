# 给你一个以字符串表示的非负整数 num 和一个整数 k ，移除这个数中的 k 位数字，使得剩下的数字最小。请你以字符串形式返回这个最小的数字。
#
#  
# 示例 1 ：
#
# 输入：num = "1432219", k = 3
# 输出："1219"
# 解释：移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219 。
# 示例 2 ：
#
# 输入：num = "10200", k = 1
# 输出："200"
# 解释：移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
# 示例 3 ：
#
# 输入：num = "10", k = 2
# 输出："0"
# 解释：从原数字移除所有的数字，剩余为空就是 0 。
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #保留的思路
        stack = []
        #设置保留长度
        remain = len(num)-k
        for c in num:
            #栈非空，当前值小于栈顶，k不为0
            while stack and stack[-1]>c and k:
                #移除该值且k-1
                stack.pop()
                k-=1
            stack.append(c)
        #串联应保留的stack且去除左边的“0”，为保证不返回空增加 or "0"
        return "".join(stack[:remain]).lstrip('0') or "0"
