给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。

 

示例 1：

输入：s = "barfoothefoobarman", words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
输出：[]
示例 3：

输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
输出：[6,9,12]

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 超时
        # word_l = len(words[0])
        # all_l = len(words)*word_l
        # cnt = Counter(words)
        # ans = []
        # for i in range(0, len(s)-all_l+1):
        #     tmp = []
        #     # 这一段的每个单词放入tmp
        #     for j in range(i, i+all_l, word_l):
        #         tmp.append(s[j:j+word_l])
        #     print(tmp)
        #     # tmp的Counter的结果和words的Counter的结果是否相同
        #     if Counter(tmp) == cnt :
        #         ans.append(i)
        # return ans


        word_l = len(words[0])
        cnt = Counter(words)
        word_num = len(words)
        ans = []
        # i从0-word_l，因为无效字符串对4取余的结果总是小于四，所以这样可以应对所有情况
        for i in range(word_l):
            left,right = i, i
            cur_num = 0
            cur_Counter = Counter()
            # right遍历到结尾
            while right +  word_l <= len(s):
                word_cur = s[right:right+word_l]
                right += word_l
                cur_Counter[word_cur] += 1
                cur_num += 1
                # 词频超过，移动左指针
                while cur_Counter[word_cur] > cnt[word_cur]:
                    left_word = s[left:left+word_l]
                    left += word_l
                    cur_Counter[left_word] -= 1
                    cur_num -= 1
                # 在此限制条件下，只需要词数相同即可
                if cur_num == word_num:
                    ans.append(left)
        return ans
            







