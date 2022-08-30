# 给你一个由小写字母组成的字符串 s ，和一个整数 k 。如果满足下述条件，则可以将字符串 t 视作是 理想字符串 ：
#
# t 是字符串 s 的一个子序列。
# t 中每两个 相邻 字母在字母表中位次的绝对差值小于或等于 k 。
# 返回 最长 理想字符串的长度。
#
# 字符串的子序列同样是一个字符串，并且子序列还满足：可以经由其他字符串删除某些字符（也可以不删除）但不改变剩余字符的顺序得到。
#
# 注意：字母表顺序不会循环。例如，'a' 和 'z' 在字母表中位次的绝对差值是 25 ，而不是 1 。
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # 字符串问题套路：枚举字符
        # 子序列 + 相邻 -> DP 关键词
        # 我的版本也可以
        # 可以f[i][c] 为前i个字符中结尾为字符c的最长长度
        # 第一个维度可以被压缩掉
        # 用我写的版本即可

        cnts = [0] * 26
        for c in s:
            idx = ord(c) - ord('a')
            # max_val = 0
            # print(max(0, idx-k), min(26, idx+k))
            # for i in range(max(0, idx-k), min(26, idx+k+1)):
            #     cnts[idx] = max(cnts[idx], cnts[i])
            # cnts[idx] += 1
            cnts[idx] = max(cnts[max(0, idx - k): idx + k + 1]) + 1
        return max(cnts)
