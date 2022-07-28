# 设计一个使用单词列表进行初始化的数据结构，单词列表中的单词 互不相同 。 如果给出一个单词，请判定能否只将这个单词中一个字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。
#
# 实现 MagicDictionary 类：
#
# MagicDictionary() 初始化对象
# void buildDict(String[] dictionary) 使用字符串数组 dictionary 设定该数据结构，dictionary 中的字符串互不相同
# bool search(String searchWord) 给定一个字符串 searchWord ，判定能否只将字符串中 一个 字母换成另一个字母，使得所形成的新字符串能够与字典中的任一字符串匹配。如果可以，返回 true ；否则，返回 false 。
class Tries:
    def __init__(self) -> None:
        self.isEnd = False
        self.children = dict()


class MagicDictionary:

    def __init__(self):
        self.root = Tries()
        # self.l = None

    def buildDict(self, dictionary: List[str]) -> None:
        # self.l = dictionary

        for word in dictionary:
            node = self.root
            for c in word:
                if c not in node.children:
                    node.children[c] = Tries()
                node = node.children[c]
            node.isEnd = True

    def search(self, searchWord: str) -> bool:
        # n = len(searchWord)
        # for word in self.l:
        #     if len(word)!=n:continue
        #     cnt = 0
        #     for i in range(n):
        #         if searchWord[i] == word[i]:
        #             cnt += 1
        #     if cnt == n-1:
        #         return True
        # return False
        n = len(searchWord)

        def dfs(node: Tries, diff: bool, pos: int) -> bool:
            if pos == n:
                return diff and node.isEnd
            c = searchWord[pos]
            # 如果c在node中
            if c in node.children:
                if dfs(node.children[c], diff, pos + 1):
                    return True
                    # 如果c不在node中
            # 如果还不存在 不同
            if not diff:
                for nex in node.children:
                    if c != nex:
                        if dfs(node.children[nex], True, pos + 1):
                            return True
            return False

        return dfs(self.root, False, 0)

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)