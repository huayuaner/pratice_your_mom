# 对于两个字符串A和B，如果A和B中出现的字符种类相同且每种字符出现的次数相同，则A和B互为变形词，请设计一个高效算法，检查两给定串是否互为变形词。
#
# 给定两个字符串A和B，请返回一个bool值，代表他们是否互为变形词。

from collections import Counter
def compare(s1, s2):
    cnt1 = Counter(s1)
    cnt2 = Counter(s2)
    for key in cnt1.keys():
        if key not in cnt2 or cnt1[key]!=cnt2[key]:
            return 0
    return 1
s1 = str(input())
s2 = str(input())
if len(s1)!= len(s2):
    print(0)
else:
    print(compare(s1, s2))