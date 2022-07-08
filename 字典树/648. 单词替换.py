# 在英语中，我们有一个叫做 词根(root) 的概念，可以词根后面添加其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。
#
# 现在，给定一个由许多词根组成的词典 dictionary 和一个用空格分隔单词形成的句子 sentence。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。
#
# 你需要输出替换之后的句子。
#
class Tries:
    def __init__(self) -> None:
        self.isEnd = False
        self.children = [None]*26
    def insert(self,word):
        # 这句话的意思是node是Tries的实例
        node = self
        for c in word:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                node.children[idx] = Tries()
            node = node.children[idx]
        node.isEnd = True
    def search(self, word):
        node = self
        for i,c in enumerate(word):
            idx = ord(c) - ord('a')
            if node.isEnd:
                return i
            if not node.children[idx]:
                return -1
            node = node.children[idx]
        return -1

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:


        # 字典树
        t = Tries()
        for word in dictionary:
            t.insert(word)
        l = sentence.split()
        for i in range(len(l)):
            end = t.search(l[i])
            if end != -1:
                l[i] = l[i][:end]
        return ' '.join(l)








