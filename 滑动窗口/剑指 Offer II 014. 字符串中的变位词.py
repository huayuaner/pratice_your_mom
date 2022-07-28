# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的某个变位词。
#
# 换句话说，第一个字符串的排列之一是第二个字符串的 子串 。

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # cnts = Counter(s1)
        # m,n = len(s1), len(s2)
        # sub = Counter(s2[:m])
        # if sub == cnts:
        #     return True
        # for i in range(1, n-m+1):
        #     sub[s2[i+m-1]] += 1
        #     sub[s2[i-1]] -= 1
        #     if sub[s2[i-1]] == 0: del sub[s2[i-1]]
        #     if sub == cnts:
        #         return True

        # return False

        # 使用数组记录每个字符的差异，使用diff记录总体差异
        cnts = [0]*26
        m,n = len(s1), len(s2)
        if m>n: return False
        for i in range(m):
            # s2的 + ，s1的 -
            cnts[ord(s2[i])-ord('a')] += 1
            cnts[ord(s1[i])-ord('a')] -= 1
        diff = 0
        for d in cnts:
            if d != 0:
                diff += 1
        if diff==0: return True
        for i in range(1, n-m+1):
            # 如果失去的和新增的是相同的字符，相当于不变
            if s2[i+m-1] == s2[i-1]:continue
            # 如果失去的字符之前平衡，那么diff需要+1
            if cnts[ord(s2[i-1])-ord('a')] == 0: diff += 1
            # 失去的字符 -1
            cnts[ord(s2[i-1])-ord('a')] -= 1
            # 如果失去了这个字符平衡了，diff-1
            if cnts[ord(s2[i-1])-ord('a')] == 0: diff -= 1
            # 下面同理
            if cnts[ord(s2[i+m-1])-ord('a')] == 0:diff += 1
            cnts[ord(s2[i+m-1])-ord('a')] += 1
            if cnts[ord(s2[i+m-1])-ord('a')] == 0: diff -= 1
            if diff == 0:
                return True
        return False


