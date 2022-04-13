# 输入一个字符串 s，s 由小写英文字母组成，保证 s 长度小于等于 5000 并且大于等于 1。在 s 的所有不同的子串中，输出字典序第 k 小的字符串。
# 字符串中任意个连续的字符组成的子序列称为该字符串的子串。
# 字母序表示英文单词在字典中的先后顺序，即先比较第一个字母，若第一个字母相同，则比较第二个字母的字典序，依次类推，则可比较出该字符串的字典序大小。

# 思路
# 第k小的字典序长度肯定不大于k
# 将各个位置小于k长度放入集合中去重
# 再list化进行排序，选第k个
import heapq
s = input()
idx = int(input())
sub_lis = set()
for i in range(len(s)):
    for j in range(1, idx+1):
        sub_lis.add(s[i:i+j])
sub_lis = list(sub_lis)
sub_lis.sort()
# print(sub_lis)
print(sub_lis[idx-1])