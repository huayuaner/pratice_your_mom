# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
#
# 字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。
#
#  
#
# 示例 1:
#
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 示例 2:
#
# 输入: strs = [""]
# 输出: [[""]]
# 示例 3:
#
# 输入: strs = ["a"]
# 输出: [["a"]]
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ans = []
        # # n = len(strs)
        # # 字母异位词排序后是一样的
        # dic = dict()
        # for s in strs:
        #     s_sorted = ''.join(sorted(s))
        #     if s_sorted in dic:
        #         ans[dic[s_sorted]].append(s)
        #     else:
        #         dic[s_sorted] = len(ans)
        #         ans.append([s])
        # return ans

        # 计数
        dic = collections.defaultdict(list)
        for s in strs:
            cnt = [0]*26
            for c in s:
                cnt[ord(c) - ord('a')] += 1
            dic[tuple(cnt)].append(s)
        return list(dic.values())