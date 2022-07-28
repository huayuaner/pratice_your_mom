# 设计一个包含一些单词的特殊词典，并能够通过前缀和后缀来检索单词。
#
# 实现 WordFilter 类：
#
# WordFilter(string[] words) 使用词典中的单词 words 初始化对象。
# f(string pref, string suff) 返回词典中具有前缀 prefix 和后缀 suff 的单词的下标。如果存在不止一个满足要求的下标，返回其中 最大的下标 。如果不存在这样的单词，返回 -1 。
#  
#
# 示例：
#
# 输入
# ["WordFilter", "f"]
# [[["apple"]], ["a", "e"]]
# 输出
# [null, 0]
# 解释
# WordFilter wordFilter = new WordFilter(["apple"]);
# wordFilter.f("a", "e"); // 返回 0 ，因为下标为 0 的单词：前缀 prefix = "a" 且 后缀 suff = "e" 。
class Tries():
    def __init__(self) -> None:
        self.isEnd = False
        self.children = [None] * 26
        self.idx = list()

    def insert(self, s, i):
        node = self
        for c in s:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                node.children[idx] = Tries()
            # node.idx = i
            node = node.children[idx]
            node.idx.append(i)
        node.isEnd = True

    def search(self, sub_s):
        node = self
        # cover = set()
        for c in sub_s:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                return []
            node = node.children[idx]
        return node.idx


class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.order = Tries()
        self.memo = dict()
        for i, word in enumerate(words):
            self.order.insert(word, i)

        # print(self.order.children)
        # self.dic = dict()
        # for idx,word in enumerate(words):
        #     n = len(word)
        #     for i in range(1,n+1):
        #         for j in range(1, n+1):
        #             self.dic[(word[:i], word[-j:])] = idx

    def f(self, pref: str, suff: str) -> int:
        # return self.dic.get((pref, suff),-1)
        if (pref, suff) in self.memo:
            return self.memo[(pref, suff)]
        # ans = -1
        for idx in reversed(self.order.search(pref)):
            if self.words[idx].endswith(suff):
                self.memo[(pref, suff)] = idx
                return idx
        self.memo[(pref, suff)] = -1
        return -1
        # ans = -1
        # m,n = len(pref), len(suff)
        # for i,word in enumerate(self.words):
        #     if len(word)<max(m,n):continue
        #     if word[:m] == pref and word[-n:] == suff:
        #         ans = i
        # return ans

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)