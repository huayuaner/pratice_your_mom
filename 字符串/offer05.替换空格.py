# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
#
#  
#
# 示例 1：
#
# 输入：s = "We are happy."
# 输出："We%20are%20happy."

class Solution:
    def replaceSpace(self, s: str) -> str:
        # return s.replace(' ','%20')

        # c = list(s)
        # for i in range(len(c)):
        #     if c[i] == ' ':
        #         c[i] = '%20'
        # return ''.join(c)

        # 双指针
        cnt = s.count(' ')
        i, j = len(s) - 1, len(s) + 2 * cnt - 1
        c = list(s)
        c.extend([' '] * cnt * 2)
        while i != j:
            if c[i] != ' ':
                c[j] = c[i]
                i -= 1
                j -= 1
            else:
                c[j] = '0'
                c[j - 1] = '2'
                c[j - 2] = '%'
                i -= 1
                j -= 3
        return ''.join(c)