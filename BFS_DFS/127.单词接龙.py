# 字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 -> s2 -> ... -> sk：
#
# 每一对相邻的单词只差一个字母。
#  对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。
# sk == endWord
# 给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0 。
#
#  
# 示例 1：
#
# 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# 输出：5
# 解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
# 示例 2：
#
# 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# 输出：0
# 解释：endWord "cog" 不在字典中，所以无法进行转换。

from collections import defaultdict
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # if endWord not in wordList or beginWord == endWord:
        #     return 0
        # n, m = len(wordList), len(wordList[0])
        # general_dic = defaultdict(list)
        # for word in wordList:
        #     for i in range(m):
        #         general_dic[word[:i]+'*'+word[i+1:]].append(word)
        # # 邻接矩阵 超时
        # # adj = [[]for _ in range(n)]
        # # for i in range(n-1):
        # #     for j in range(i+1,n):
        # #         if sum([wordList[i][idx]!=wordList[j][idx] for idx in range(m)]) == 1:
        # #             adj[i].append(j)
        # #             adj[j].append(i)
        # # print(adj)
        # pq = deque()
        # seen = set()
        # # for i in range(n):
        # #     if sum([beginWord[idx]!=wordList[i][idx] for idx in range(m)]) == 1:
        # #         pq.append((i, 1))
        # #         seen.add(i)
        # pq.append((beginWord, 0))
        # seen.add(beginWord)
        # while pq:
        #     word, step = pq.popleft()
        #     if word == endWord:
        #         return step + 1
        #     for i in range(m):
        #         for neighbour in general_dic[word[:i]+'*'+word[i+1:]]:
        #             if neighbour not in seen:
        #                 seen.add(neighbour)
        #                 pq.append((neighbour, step+1))
        #     # for j in adj[i]:
        #     #     if j not in seen:
        #     #         seen.add(j)
        #     #         pq.append((j, step+1))
        #     # print(pq)
        # return 0

        # word_set = set(wordList)
        m = len(beginWord)
        if endWord not in wordList:  # word_set:
            return 0
        general_dic = defaultdict(list)
        for word in wordList:
            for i in range(m):
                general_dic[word[:i] + '*' + word[i + 1:]].append(word)
        # print(general_dic)
        # 双向广度搜索
        pq = [deque(), deque()]
        seen = [set(), set()]
        # 分别从头尾进行搜索
        pq[0].append(beginWord)
        seen[0].add(beginWord)
        pq[1].append(endWord)
        seen[1].add(endWord)
        step = 0
        while pq[0] and pq[1]:
            # 搜索长度更小的那一个队列
            idx = (1 if len(pq[0]) > len(pq[1]) else 0)
            step += 1
            # 把队列中的全部都过一遍
            for _ in range(len(pq[idx])):
                word = pq[idx].popleft()
                oppo = (1 if idx == 0 else 0)
                # 当发现一端的广搜的结果出现在另一端广搜遍历过的node的时候，说明已经碰头，返回node
                # print(word)
                if word in seen[oppo]:
                    # print(word, seen)
                    # print(111)
                    return step
                for i in range(m):
                    for neighbour in general_dic[word[:i] + '*' + word[i + 1:]]:
                        # print(neighbour, word[:i]+'*'+word[i+1:])
                        if neighbour not in seen[idx]:
                            seen[idx].add(neighbour)
                            pq[idx].append(neighbour)
                    # for j in range(26):
                    #     tmp = word[:i] + chr(97+j) + word[i+1:]
                    #     if tmp not in seen[idx] and tmp in word_set:
                    #         pq[idx].append(tmp)
                    #         seen[idx].add(tmp)
            # print(pq)
        return 0




