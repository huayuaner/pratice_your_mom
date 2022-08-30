# 给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。
#
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。
#
#  
#
# 示例1:
#
# 输入: pattern = "abba", s = "dog cat cat dog"
# 输出: true
# 示例 2:
#
# 输入:pattern = "abba", s = "dog cat cat fish"
# 输出: false
# 示例 3:
#
# 输入: pattern = "aaaa", s = "dog cat cat dog"
# 输出: false
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # if len(pattern)!= len(s.split()):
        #     return False
        # dic_p2s = dict()
        # dic_s2p = dict()
        # for p,word in zip(pattern,s.split()):
        #     # print(p,word)
        #     if p not in dic_p2s and word not in dic_s2p:
        #         dic_p2s[p] = word
        #         dic_s2p[word] = p
        #     elif p in dic_p2s and word in dic_s2p and dic_p2s[p] == word and dic_s2p[word]==p:
        #         continue
        #     else:
        #         # print(p, word)
        #         return False
        #     # print(dic_p2s, dic_s2p)
        # return True

        # 单个哈希思路
        dic = dict()
        words = s.split()
        if len(pattern)!=len(words):
            return False
        for p, word in zip(pattern, words):
            if p not in dic:
                if word in dic.values():
                    return False
                dic[p] = word
            else:
                if dic[p] != word:
                    return False
        return True