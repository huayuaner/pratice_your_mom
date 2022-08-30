# 给你一个字符串 s 和一个整数 k ，请你找出 至多 包含 k 个 不同 字符的最长子串，并返回该子串的长度。
#
#  
#
# 示例 1：
#
# 输入：s = "eceba", k = 2
# 输出：3
# 解释：满足题目要求的子串是 "ece" ，长度为 3 。
# 示例 2：
#
# 输入：s = "aa", k = 1
# 输出：2
# 解释：满足题目要求的子串是 "aa" ，长度为 2 。
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # 哈希
        dic = dict()
        ans = l = r = 0
        n = len(s)
        while r < n:
            dic[s[r]] = r
            if len(dic) > k:
                del_idx = min(dic.values())
                l = del_idx + 1
                del dic[s[del_idx]]

            ans = max(ans, r - l + 1)
            r += 1
        return ans
