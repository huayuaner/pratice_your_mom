# 给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。
#
# 注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。
#
#  
#
# 示例 1：
#
# 输入：n = 12
# 输出：21
# 示例 2：
#
# 输入：n = 21
# 输出：-1
MAX_INT = 2**31-1
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        l = list(str(n))
        # 从后往前找第一个小于前一个的数
        length = idx = len(l)
        # 找到第一个逆序
        for i in range(length-1, 0, -1):
            if l[i] > l[i-1]:
                idx = i
                break
        # 不存在逆序
        if idx == length:
            return -1
        # 找第一个小于逆序的数之后大于这个逆序的最小的数
        j = length-1
        while j>idx:
            if l[j] > l[idx-1]:
                break
            j -= 1
        # print(l[idx],j)
        l[idx-1],l[j] = l[j],l[idx-1]
        # print(2**31-1)
        ans = int(''.join(l[:idx]) + ''.join(sorted(l[idx:])))
        # print(ans)
        return ans if ans <= MAX_INT else -1
