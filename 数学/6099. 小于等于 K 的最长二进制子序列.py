# 给你一个二进制字符串 s 和一个正整数 k 。
#
# 请你返回 s 的 最长 子序列，且该子序列对应的 二进制 数字小于等于 k 。
#
# 注意：
#
# 子序列可以有 前导 0 。
# 空字符串视为 0 。
# 子序列 是指从一个字符串中删除零个或者多个字符后，不改变顺序得到的剩余字符序列。
#  
#
# 示例 1：
#
# 输入：s = "1001010", k = 5
# 输出：5
# 解释：s 中小于等于 5 的最长子序列是 "00010" ，对应的十进制数字是 2 。
# 注意 "00100" 和 "00101" 也是可行的最长子序列，十进制分别对应 4 和 5 。
# 最长子序列的长度为 5 ，所以返回 5 。
# 示例 2：
#
# 输入：s = "00101001", k = 1
# 输出：6
# 解释："000001" 是 s 中小于等于 1 的最长子序列，对应的十进制数字是 1 。
# 最长子序列的长度为 6 ，所以返回 6 。
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        m = k.bit_length()
        n = len(s)
        if n<m:
            return n
        ans = m-1
        # 我对这个if之前有个疑问：会不会最后的后缀 > k 但是s中有长度为m且 <= k的部分会是更加优秀的答案呢？
        # 但是有一个很巧妙的地方，首先 k的开头肯定是1，所以s[n-m:]的开头也肯定是1，那么该如何降低呢？肯定要用到前面的0才可以是窗口为m的内容变小
        # 但是如果用掉了0，也就相当于其前缀0 少了一个， 其实跟m-1的情况前缀0多一个是一样的
        if int(s[n-m:],2) <= k:
            ans = m
        # print(ans)
        return s.count('0', 0, n-m) + ans