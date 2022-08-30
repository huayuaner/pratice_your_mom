# 给你下标从 0 开始、长度为 n 的字符串 pattern ，它包含两种字符，'I' 表示 上升 ，'D' 表示 下降 。
#
# 你需要构造一个下标从 0 开始长度为 n + 1 的字符串，且它要满足以下条件：
#
# num 包含数字 '1' 到 '9' ，其中每个数字 至多 使用一次。
# 如果 pattern[i] == 'I' ，那么 num[i] < num[i + 1] 。
# 如果 pattern[i] == 'D' ，那么 num[i] > num[i + 1] 。
# 请你返回满足上述条件字典序 最小 的字符串 num。
# from strings import digits
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # O(n)
        n = len(pattern)
        ans = list(digits[1:n+2])
        i = 0
        while i<n:
            if pattern[i] == 'I':
                i += 1
                continue
            start = i
            i += 1
            while i<n and pattern[i] == 'D':
                i += 1
            ans[start:i+1] = ans[start:i+1][::-1]
        return ''.join(ans)