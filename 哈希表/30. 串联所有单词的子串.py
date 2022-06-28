# 给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
#
# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。
#
#  
#
# 示例 1：
#
# 输入：s = "barfoothefoobarman", words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
# 示例 2：
#
# 输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# 输出：[]
# 示例 3：
#
# 输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# 输出：[6,9,12]

from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # n,m = len(words), len(words[0])
        # length = len(s)
        # # words_hash = set(words)

        # def check(start_idx, words):
        #     # seen = set()
        #     # 记录经过了几个
        #     # cnt = 0
        #     cnts = Counter(words)
        #     end = start_idx + m*n
        #     while start_idx < end:
        #         tmp_s = s[start_idx:start_idx+m]
        #         if tmp_s in cnts and cnts[tmp_s] > 0:
        #             cnts[tmp_s] -= 1
        #             if cnts[tmp_s] == 0:
        #                 del cnts[tmp_s]
        #         else:
        #             return False
        #         start_idx += m
        #     # print(cnts)
        #     return not cnts
        # i = 0
        # ans = []
        # while i<length:
        #     # print(i)
        #     if check(i,words):
        #         ans.append(i)

        #     i += 1
        # return ans

        # 上面的方法重复的部分做了太多次
        # 其实可以这样减少时间复杂度
        # 窗口左指针依旧是遍历len(words[0])，而在每一次遍历中左指针都可以跳跃len(words[0])
        ans = []
        n, m = len(words), len(words[0])
        length = len(s)
        # 左指针只需要遍历长度m
        # 而在每一次遍历中也是增加m
        # 由此可以得到
        # 第一次遍历左指针分别为  0, m, 2m
        # 第二次遍历左指针分别为  1, m+1, 2m+1
        # 第m次遍历 左指针分别为  m-1, 2m-1, 3m-1
        # 全部总和相当于左指针遍历了全部
        # 但是这种方式的巧妙的点在于用这种方式我每次都可以增加一个m长度的单词，更方便Counter的计数
        for i in range(m):
            # 如果右指针区域右指针超过了长度，说明无法继续遍历
            if i + m * n > length:
                break
            cnt = Counter()
            # 记录该区间长度为m的单词出现频数
            for j in range(n):
                word = s[i + j * m: i + (j + 1) * m]
                cnt[word] += 1
            # 减去words中出现单词的次数
            # 并删去为0的单词
            for word in words:
                cnt[word] -= 1
                if cnt[word] == 0:
                    del cnt[word]
            # 在i情况下，这时的步长可以是n
            # 中间的空隙在i的遍历的情况下会填补
            for start in range(i, length - n * m + 1, m):
                if start != i:
                    # 此时的word是这个滑动窗口尾巴新增的word
                    word = s[start + (n - 1) * m:start + n * m]
                    cnt[word] += 1
                    if cnt[word] == 0:
                        del cnt[word]
                    # 滑动窗口失去的单词
                    word = s[start - m: start]
                    cnt[word] -= 1
                    if cnt[word] == 0:
                        del cnt[word]
                if len(cnt) == 0:
                    # print(i,start)
                    ans.append(start)
        return ans







