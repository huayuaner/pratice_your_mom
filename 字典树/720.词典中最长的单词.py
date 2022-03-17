# 给出一个字符串数组 words 组成的一本英语词典。返回 words 中最长的一个单词，该单词是由 words 词典中其他单词逐步添加一个字母组成。
#
# 若其中有多个可行的答案，则返回答案中字典序最小的单词。若无答案，则返回空字符串。
#
#  
#
# 示例 1：
#
# 输入：words = ["w","wo","wor","worl", "world"]
# 输出："world"
# 解释： 单词"world"可由"w", "wo", "wor", 和 "worl"逐步添加一个字母组成。
# 示例 2：
#
# 输入：words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# 输出："apple"
# 解释："apply" 和 "apple" 都能由词典中的单词组成。但是 "apple" 的字典序小于 "apply"

class Trie:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26

    def insert(self, word):
        node = self
        for c in word:
            idx = ord(c) - ord('a')
            # 如果下边没有初始化
            if not node.children[idx]:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.isEnd = True

    def search(self, word):
        node = self
        for c in word:
            idx = ord(c) - ord('a')
            # 这里加入了判断这个孩子是不是结尾，所以从word往下每一个都会被判断到
            if not node.children[idx] or not node.children[idx].isEnd:
                return False
            node = node.children[idx]
        return True if node.isEnd else False


class Solution:
    def longestWord(self, words: List[str]) -> str:
        t = Trie()
        for word in words:
            t.insert(word)
        ans = ''
        for word in words:
            if t.search(word) and (len(word) > len(ans) or len(word) == len(ans) and word < ans):
                ans = word
        return ans

        # Set = set(words)
        # ans = ''
        # for word in words:

        #     tmp = word
        #     while 1:
        #         if len(tmp)==1:
        #             if len(word)>len(ans):
        #                 ans = word
        #             elif len(word)==len(ans):
        #                 ans = min(word, ans)
        #             break
        #         else:
        #             if tmp[:-1] not in Set:
        #                 break
        #             else:
        #                 tmp = tmp[:-1]

        # return ans

        # 按长度的负值和字典序排序，再反转，就是长度从小到大且长度相同字典序从大到小
        # words.sort(key=lambda x: (-len(x), x), reverse=True)
        # # print(words)
        # longest = ""
        # candidates = {""}
        # for word in words:
        #     # 字典序从大到小，遍历完总是要不len更大要不字典序更小的word
        #     if word[:-1] in candidates:
        #         longest = word
        #         candidates.add(word)
        # return longest




