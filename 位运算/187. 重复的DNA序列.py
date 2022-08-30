# DNA序列 由一系列核苷酸组成，缩写为 'A', 'C', 'G' 和 'T'.。
#
# 例如，"ACGAATTCCG" 是一个 DNA序列 。
# 在研究 DNA 时，识别 DNA 中的重复序列非常有用。
#
# 给定一个表示 DNA序列 的字符串 s ，返回所有在 DNA 分子中出现不止一次的 长度为 10 的序列(子字符串)。你可以按 任意顺序 返回答案。
#
#  
#
# 示例 1：
#
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC","CCCCCAAAAA"]
# 示例 2：
#
# 输入：s = "AAAAAAAAAAAAA"
# 输出：["AAAAAAAAAA"]
L = 10
states = {'A':1, 'C':2, 'G':3, 'T':4}
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # if len(s)<10:
        #     return []
        # # 滑窗
        # n = len(s)
        # cur = s[:10]
        # ans = []
        # cnts = Counter()
        # cnts[cur] += 1
        # r = 10
        # while r<n:
        #     cur = cur[1:] + s[r]
        #     cnts[cur] += 1
        #     if cnts[cur] == 2:
        #         # print(r)
        #         ans.append(cur)
        #     r += 1
        #     # print(cnts)
        # return ans

        # 字符串记录状态
        if len(s)<10:
            return []
        n = len(s)
        cnt = Counter()
        ans = []
        # 初始化
        tot = 0
        for i in range(L):
            tot = (tot<<2)|states[s[i]]
        # print(tot)
        cnt[tot] += 1
        for i in range(L, n):
            tot = ((tot<<2)|states[s[i]])&((1<<20) - 1)
            # print(tot)
            cnt[tot] += 1
            if cnt[tot] == 2:
                ans.append(s[i-L+1:i+1])
        return ans

