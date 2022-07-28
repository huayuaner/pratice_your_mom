# 某种外星语也使用英文小写字母，但可能顺序 order 不同。字母表的顺序（order）是一些小写字母的排列。
#
# 给定一组用外星语书写的单词 words，以及其字母表的顺序 order，只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回 false。

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 记录下标
        dic_idx = dict()
        for i, c in enumerate(order):
            dic_idx[c] = i

        def compare_(s1, s2):
            i = j = 0
            m, n = len(s1), len(s2)
            while i < m and j < n:
                if s1[i] == s2[j]:
                    i += 1
                    j += 1
                else:
                    if dic_idx[s1[i]] < dic_idx[s2[j]]:
                        return True
                    else:
                        return False
            return True if m <= n else False

        for i in range(1, len(words)):
            if not compare_(words[i - 1], words[i]):
                return False
        return True
