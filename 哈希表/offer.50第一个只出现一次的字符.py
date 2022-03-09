在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例 1:

输入：s = "abaccdeff"
输出：'b'
示例 2:

输入：s = ""
输出：' '

class Solution:
    def firstUniqChar(self, s: str) -> str:
        # cnt = Counter(s)
        # for c in s:
        #     if cnt[c]==1:
        #         return c
        # return ' '

        # 哈希+队列
        HashMap = dict()
        q = collections.deque()
        n = len(s)
        for i, c in enumerate(s):
            # 使用队列存每一个字符第一次出现的位置
            if c not in HashMap:
                HashMap[c] = i
                q.append((c,i))
            # pop掉队头的重复元素
            else:
                HashMap[c] = -1
                while q and HashMap[q[0][0]]==-1:
                    q.popleft()
        return ' ' if not q else q[0][0]

