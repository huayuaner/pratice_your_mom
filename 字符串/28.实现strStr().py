# 实现 strStr() 函数。
#
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。
#
#  
#
# 说明：
#
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
#
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。
#
#  
#
# 示例 1：
#
# 输入：haystack = "hello", needle = "ll"
# 输出：2
# 示例 2：
#
# 输入：haystack = "aaaaa", needle = "bba"
# 输出：-1
# 示例 3：
#
# 输入：haystack = "", needle = ""
# 输出：0
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle not in haystack:
        #     return -1
        # else:
        #     return haystack.find(needle)

        # KMP 算法
        # 通过 needle 构建 next 数组，通过next数组进行匹配
        # next[i]  表示的是在i之前的字符串最长的前后缀（也就是从前往后和从后往前相同的个数）-1
        def get_next(needle):
            n = len(needle)
            next_ = [0]*n
            k = -1
            next_[0] = -1
            for i in range(1,n):
                # 这里比较的是 needle 前面和后面
                while k>=0 and needle[k+1] != needle[i]:
                    # 相当于把k往前倒
                    # 因为k最后会倒到开头，会达到-1
                    k = next_[k]
                if needle[k+1] == needle[i]:
                    k += 1
                next_[i] = k
            return next_
        n,m = len(haystack), len(needle)
        if n == 0:
            return 0
        next_ = get_next(needle)
        # 这里的p表示匹配上的个数-1
        p = -1
        for i in range(n):
            # print(p)
            # 这里比较的是needle 和 haystack
            while p>=0 and needle[p+1] != haystack[i]:
                # 退回至 最大公共前后缀之中
                p = next_[p]
                # print(p)
            if needle[p+1] == haystack[i]:
                p += 1
            if p == m-1:
                return i-m+1
        return -1
