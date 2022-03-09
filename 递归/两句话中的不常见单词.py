句子 是一串由空格分隔的单词。每个 单词 仅由小写字母组成。

如果某个单词在其中一个句子中恰好出现一次，在另一个句子中却 没有出现 ，那么这个单词就是 不常见的 。

给你两个 句子 s1 和 s2 ，返回所有 不常用单词 的列表。返回列表中单词可以按 任意顺序 组织。

 

示例 1：

输入：s1 = "this apple is sweet", s2 = "this apple is sour"
输出：["sweet","sour"]
示例 2：

输入：s1 = "apple apple", s2 = "banana"
输出：["banana"]
 
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # s1 = s1.split(" ")
        # cnt_1 = Counter(s1)
        # s2 = s2.split(" ")
        # cnt_2 = Counter(s2)
        # ans = []
        # #print(cnt_1,cnt_2)
        # for key1 in cnt_1.keys():
        #     #print(key1, key2)
        #     if cnt_1[key1] < 2 and key1 not in cnt_2:
        #         ans.append(key1)
            
        # for key2 in cnt_2.keys():
        #     if cnt_2[key2] < 2 and key2 not in cnt_1:
        #         ans.append(key2)
        ans = []
        # 合并哈希表
        cnt = Counter(s1.split()) + Counter(s2.split())
        for word, times in cnt.items():
            if times == 1:
                ans.append(word)

        return ans
        