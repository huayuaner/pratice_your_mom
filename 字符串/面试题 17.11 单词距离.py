# 有个内含单词的超大文本文件，给定任意两个不同的单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?
#
# 示例：
#
# 输入：words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"
# 输出：1
#
import bisect
class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        idx_1 = []
        idx_2 = []
        for i,word in enumerate(words):
            if word == word1:
                idx_1.append(i)
            if word == word2:
                idx_2.append(i)
        # print(idx_1,idx_2)
        ans = float('inf')
        for idx in idx_1:
            pos = bisect.bisect(idx_2, idx)
            if pos == len(idx_2):
                dis = idx - idx_2[-1]
            elif pos == 0:
                dis = idx_2[0] - idx
            else:
                dis = min(idx-idx_2[pos-1], idx_2[pos]-idx)
            ans = min(ans,dis)
        return ans
        # index1 = index2 = -1
        # ans = float('inf')
        # for i,word in enumerate(words):
        #     if word == word1:
        #         index1 = i
        #     elif word == word2:
        #         index2 = i
        #     if index1>=0 and index2>=0:
        #         ans = min(ans, abs(index1-index2))
        # return ans
