# 给定字符串列表 strs ，返回其中 最长的特殊序列 。如果最长特殊序列不存在，返回 -1 。
#
# 特殊序列 定义如下：该序列为某字符串 独有的子序列（即不能是其他字符串的子序列）。
#
#  s 的 子序列可以通过删去字符串 s 中的某些字符实现。
#
# 例如，"abc" 是 "aebdc" 的子序列，因为您可以删除"aebdc"中的下划线字符来得到 "abc" 。"aebdc"的子序列还包括"aebdc"、 "aeb" 和 "" (空字符串)。
#
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:

        # 判断s1是不是s2的子序列
        def check(s1, s2):
            i = j = 0
            n, m = len(s1), len(s2)
            while i < n and j < m:
                if s1[i] == s2[j]:
                    i += 1
                j += 1
            return i == n

        n = len(strs)
        ans = -1
        for i, s_i in enumerate(strs):
            for j, s_j in enumerate(strs):
                if i == j:
                    continue
                    # print(s_i,s_j)
                # 判断出问题了
                if check(s_i, s_j):
                    break
            else:
                ans = max(ans, len(s_i))
        return ans


