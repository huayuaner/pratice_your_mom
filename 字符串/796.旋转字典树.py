# 给定两个字符串, s 和 goal。如果在若干次旋转操作之后，s 能变成 goal ，那么返回 true 。
#
# s 的 旋转操作 就是将 s 最左边的字符移动到最右边。 
#
# 例如, 若 s = 'abcde'，在旋转一次之后结果就是'bcdea' 。
#  
#
# 示例 1:
#
# 输入: s = "abcde", goal = "cdeab"
# 输出: true
# 示例 2:
#
# 输入: s = "abcde", goal = "abced"
# 输出: false

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # 模拟
        # times = len(s)
        # if s == goal:
        #     return True
        # while times:
        #     s = s[1:]+s[0]
        #     if s==goal:return True
        #     times -= 1
        # return False

        # return len(goal) == len(s) and goal in s+s