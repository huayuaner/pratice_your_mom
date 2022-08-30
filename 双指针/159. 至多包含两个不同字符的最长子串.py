# 给你一个字符串 s ，请你找出 至多 包含 两个不同字符 的最长子串，并返回该子串的长度。
#  
#
# 示例 1：
#
# 输入：s = "eceba"
# 输出：3
# 解释：满足题目要求的子串是 "ece" ，长度为 3 。
# 示例 2：
#
# 输入：s = "ccaabbb"
# 输出：5
# 解释：满足题目要求的子串是 "aabbb" ，长度为 5 。
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # 双指针
        # l, r = 0,-1
        # n = len(s)
        # cnts  = defaultdict(int)# Counter()
        # ans = 0
        # while r<n:
        #     while r<n and len(cnts)<3:
        #         r += 1
        #         if r<n:
        #             cnts[s[r]] += 1

        #     # print(l,r)
        #     # print(cnts)
        #     ans = max(ans, r-l)
        #     while len(cnts) > 2:
        #         # print(cnts)
        #         cnts[s[l]] -= 1
        #         if cnts[s[l]] == 0:
        #             del cnts[s[l]]
        #         l += 1
        #     # print(l,r)

        #     # r += 1
        #     # print(l,r)
        # return ans

        # 不用哈希
        # 初始化

        n = len(s)

        def helper(idx, l):
            while idx < n and s[idx] in l:
                idx += 1
            return idx

        idx = 0
        ans = 0
        while idx < n:
            fir_chr = s[idx]
            fir_idx = idx
            sec_idx = helper(idx, [fir_chr])
            if sec_idx == n:
                return max(ans, sec_idx - fir_idx)
            sec_chr = s[sec_idx]
            nex_idx = helper(sec_idx, [fir_chr, sec_chr])

            ans = max(ans, nex_idx - fir_idx)
            idx = sec_idx
            # print(fir_idx, sec_idx)
            # break
        return ans











