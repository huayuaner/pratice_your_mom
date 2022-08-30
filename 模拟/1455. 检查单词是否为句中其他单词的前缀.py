# 给你一个字符串 sentence 作为句子并指定检索词为 searchWord ，其中句子由若干用 单个空格 分隔的单词组成。请你检查检索词 searchWord 是否为句子 sentence 中任意单词的前缀。
#
# 如果 searchWord 是某一个单词的前缀，则返回句子 sentence 中该单词所对应的下标（下标从 1 开始）。如果 searchWord 是多个单词的前缀，则返回匹配的第一个单词的下标（最小下标）。如果 searchWord 不是任何单词的前缀，则返回 -1 。
#
# 字符串 s 的 前缀 是 s 的任何前导连续子字符串。
#
#  
#
# 示例 1：
#
# 输入：sentence = "i love eating burger", searchWord = "burg"
# 输出：4
# 解释："burg" 是 "burger" 的前缀，而 "burger" 是句子中第 4 个单词。
# 示例 2：
#
# 输入：sentence = "this problem is an easy problem", searchWord = "pro"
# 输出：2
# 解释："pro" 是 "problem" 的前缀，而 "problem" 是句子中第 2 个也是第 6 个单词，但是应该返回最小下标 2 。
# 示例 3：
#
# 输入：sentence = "i am tired", searchWord = "you"
# 输出：-1
# 解释："you" 不是句子中任何单词的前缀。
# class Tries:
#     def __init__(self):
#         self.isEnd = False
#         self.Children = [None]*26
#     def insert(self, word):
#         node = self
#         for c in word:
#             idx = ord(c) - ord('a')
#             if not node.Children[idx]:
#                 node.Children[idx] = Tries()
#             node = node.Children[idx]
#         node.isEnd = True
#     def search(self,word):
#         node = self
#         for c in word:
#             idx = ord(c) - ord('a')
#             if not node.Children[idx]:
#                 return False
#             node = node.Children[idx]
#         return True
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # n = len(searchWord)
        # for i,word in enumerate(sentence.split()):
        #     if searchWord == word[:n]:
        #         return i + 1
        # return -1

        i, index, n = 0, 1, len(sentence)
        while i < n:
            start = i
            while i < n and sentence[i] != ' ':
                i += 1
            end = i
            # print(sentence[start:end])
            if sentence[start:end].startswith(searchWord):
                return index
            i = end + 1
            index += 1
        return -1


