# 给定两个字符串 s 和 p，找到 s 中所有 p 的 变位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#
# 变位词 指字母相同，但排列不同的字符串。
#
#  
#
# 示例 1:
#
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的变位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的变位词。
#  示例 2:
#
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的变位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的变位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的变位词。

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 滑窗 + 排序
        # m, n = len(s), len(p)
        # if m < n:
        #     return []
        # # target
        # target = ''.join(sorted(p))
        # l, r = 0, n-1
        # ans = []
        # while r<m:
        #     if ''.join(sorted(s[l:r+1])) == target:
        #         ans.append(l)
        #     l+=1
        #     r+=1
        # return ans

        # 滑窗
        # m, n = len(s), len(p)
        # if m<n:
        #     return []
        # cnt_p = [0]*26
        # cnt_win = [0]*26
        # for i in range(n):
        #     cnt_p[ord(p[i])-ord('a')] += 1
        #     cnt_win[ord(s[i])-ord('a')] += 1
        # ans = []
        # if cnt_p==cnt_win:
        #     ans.append(0)
        # for i in range(m-n):
        #     cnt_win[ord(s[i])-ord('a')] -= 1
        #     cnt_win[ord(s[i+n])-ord('a')] += 1
        #     if cnt_win == cnt_p:
        #         ans.append(i+1)
        # return ans

        # 滑窗的优化
        m, n = len(s), len(p)
        if m<n:
            return []
        ans = []
        cnt = [0]*26
        for i in range(n):
            cnt[ord(p[i])-ord('a')] -= 1
            cnt[ord(s[i])-ord('a')] += 1
        diff = [c!=0 for c in cnt].count(True)
        if diff==0:
            ans.append(0)
        for i in range(m-n):
            if (tmp:=cnt[ord(s[i]) - ord('a')]) == 1:
                diff -= 1
            elif tmp == 0:
                diff += 1
            cnt[ord(s[i])-ord('a')] -= 1
            # print(cnt,tmp)
            if (tmp:=cnt[ord(s[i+n]) - ord('a')]) == -1:
                # print(diff)
                diff -= 1
            elif tmp == 0:
                diff += 1
            cnt[ord(s[i+n]) - ord('a')] += 1
            # print(cnt,tmp)
            # print(i, diff)
            if diff==0:
                ans.append(i+1)
        return ans
