# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。
#
#  
#
# 示例：
#
# 输入：S = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 最少可以分成一个
        # 最多可以分成n个
        # 分成没有交集的段，最多能分几段
        # n = len(s)
        # ans = []
        # dic = defaultdict(list)
        # for i,c in enumerate(s):
        #     dic[c].append(i)
        # end = dic[s[0]][-1]
        # for i in range(1, n+1):
        #     # if i==0:continue
        #     if i > end:
        #         if not ans:
        #             ans.append(end+1)
        #         else:
        #             ans.append(end-sum(ans)+1)
        #     if i<n:
        #         end = max(end, dic[s[i]][-1])
        # return ans

        # 只用记录每个字符出现的最后的位置即可
        cnt = [0]*26
        for i,c in enumerate(s):
            cnt[ord(c) - ord('a')] = i
        start = end = 0
        ans = []
        for i,c in enumerate(s):
            end = max(end, cnt[ord(c) - ord('a')])
            if i == end:
                ans.append(i-start + 1)
                start = i+1
        return ans