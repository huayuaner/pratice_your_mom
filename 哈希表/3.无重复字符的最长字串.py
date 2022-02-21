给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s)==1:
        #     return 1
        # maxlen = 0
        # left = 0
        # HashMap = dict()
        # for i in range(len(s)):
        #     if s[i] :
        #         if s[i] not in HashMap:
        #             HashMap[s[i]] = i
        #             if i == len(s)-1:
        #                 return max(maxlen, i-left+1)
        #         else:
        #             maxlen = max(maxlen, i-left)
        #            # print(s[left:i+1],left,i)
        #             for pre in range(left, HashMap[s[i]]):
        #                 del HashMap[s[pre]]
        #             left = HashMap[s[i]] + 1
        #             HashMap[s[i]] = i
                    

        # return maxlen
        k, res, c_dict = -1, 0, {}
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i-k)
        return res