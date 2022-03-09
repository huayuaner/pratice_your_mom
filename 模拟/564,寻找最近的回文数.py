# 给定一个表示整数的字符串 n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。
#
# “最近的”定义为两个整数差的绝对值最小。
#
#  
#
# 示例 1:
#
# 输入: n = "123"
# 输出: "121"
# 示例 2:
#
# 输入: n = "1"
# 输出: "0"
# 解释: 0 和 2是最近的回文，但我们返回最小的，也就是 0。


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        if l == 1:
            return str(int(n) - 1)
        # s: 字符串n的前半部分，奇数长度包括中间部分
        # s1: 字符串n前半部分+1
        # s2: 字符串n前半部分-1

        s = n[:l // 2 + l % 2]
        s1 = str(int(s) - 1)
        s2 = str(int(s) + 1)
        # 由s, s1, s2构成的回文串 加上可能位数有变化的100..001 和 99..99就是全部的可能性
        tmp = {'9' * (l - 1), '1' + '0' * (l - 1) + '1', s + s[-1 - l % 2::-1], s1 + s1[-1 - l % 2::-1],
               s2 + s2[-1 - l % 2::-1]}
        if n in tmp:
            tmp.remove(n)
        # print(tmp)
        # 这句话最后的. k 的意思是在前面的标准相同的情况下选择更小的
        return min(tmp, key=lambda x: (abs((k := int(x)) - int(n)), k))
        # return min('9'*(l-1)
        #             , '1'+'0'*(l-1)+'1'
        #             , s + s[-1 - l%2::-1]
        #             , s1+ s1[-1-l%2::-1]
        #             , s2+s2[-1-l%2::-1]
        #             , key=lambda x: abs(int(x) - int(n))
        #             ,key=lambda x: (abs(int(x) - int(n)) or 114514, int(x))
        #             )

        # if len(n) == 1:
        #     return str(int(n) - 1)
        # l = len(n)
        # half, v, ov = n[:l//2], int(n[:(l+1)//2]), int(n)
        # res = set()
        # s1, s2 = str(v-1), str(v + 1)
        # res.add("9" * (l - 1))
        # res.add("1" + "0" * (l - 1) + "1")
        # if l % 2:
        #     res.add(s1[:-1] + s1[-1] + s1[:-1][::-1])
        #     res.add(s2[:-1] + s2[-1] + s2[:-1][::-1])
        # else:
        #     res.add(s1 + s1[::-1])
        #     res.add(s2 + s2[::-1])
        # if n[::-1] != n:
        #     res.add(half + n[l//2] + half[::-1] if l % 2 else half + half[::-1])
        # if n in res:
        #     res.remove(n)
        # print(res)
        # return min(res, key = lambda x:(abs((k:=int(x)) - ov), k))

