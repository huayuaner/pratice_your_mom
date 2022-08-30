# 给你一个仅由数字（0 - 9）组成的字符串 num 。
#
# 请你找出能够使用 num 中数字形成的 最大回文 整数，并以字符串形式返回。该整数不含 前导零 。
#
# 注意：
#
# 你 无需 使用 num 中的所有数字，但你必须使用 至少 一个数字。
# 数字可以重新排序。
#  
#
# 示例 1：
#
# 输入：num = "444947137"
# 输出："7449447"
# 解释：
# 从 "444947137" 中选用数字 "4449477"，可以形成回文整数 "7449447" 。
# 可以证明 "7449447" 是能够形成的最大回文整数。
# 示例 2：
#
# 输入：num = "00009"
# 输出："9"
# 解释：
# 可以证明 "9" 能够形成的最大回文整数。
# 注意返回的整数不应含前导零。
from collections import Counter


class Solution:
    def largestPalindromic(self, num: str) -> str:
        # 先构造左半部分，最后镜像
        # 特判 前导0的情况
        n = len(num)
        cnts = Counter(num)
        # 全是 0
        if cnts['0'] == n:
            return '0'
        ans = ''
        # 遍历 9-1
        for d in digits[:0:-1]:
            ans += d * (cnts[d] // 2)
        if ans:  # 可以填0
            ans += '0' * (cnts['0'] // 2)

        t = ans[::-1]
        for d in digits[::-1]:
            if cnts[d] % 2 == 1:
                ans += d
                break
        return ans + t


