# 给你一个数组 colors，里面有  1、2、 3 三种颜色。
#
# 我们需要在 colors 上进行一些查询操作 queries，其中每个待查项都由两个整数 i 和 c 组成。
#
# 现在请你帮忙设计一个算法，查找从索引 i 到具有目标颜色 c 的元素之间的最短距离。
#
# 如果不存在解决方案，请返回 -1。

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        # n = len(colors)
        # 二分
        # c_idx = [[] for _ in range(3)]
        # for i,c in enumerate(colors):
        #     c_idx[c-1].append(i)
        # ans = []
        # def seach(index, c):
        #     # 下标大于等于 index的 颜色c的下标
        #     l,r = 0, len(c_idx[c-1])-1
        #     while l<r:
        #         m = l + (r-l)//2
        #         if c_idx[c-1][m] < index:
        #             l = m+1
        #         else:
        #             r = m
        #     if l == 0:
        #         return abs(c_idx[c-1][l]-index)
        #     else:
        #         return min(abs(c_idx[c-1][l]-index), abs(c_idx[c-1][l-1]-index))

        # for i,c in queries:
        #     if not c_idx[c-1]:
        #         ans.append(-1)
        #         continue
        #     # 在 下标中找颜色最近的，左边和右边
        #     ans.append(seach(i, c))
        # return ans

        # 动态规划
        n = len(colors)

        def helper(color):
            # 记录左边每个位置i左边和右边第一个color的位置
            left, right = [float('inf')] * n, [float('inf')] * n
            stack = []
            for i in range(n):
                if colors[i] != color:
                    stack.append(i)
                else:
                    while stack:
                        j = stack.pop()
                        right[j] = i - j
                    right[i] = 0

            stack.clear()
            for i in range(n - 1, -1, -1):
                if colors[i] != color:
                    stack.append(i)
                else:
                    while stack:
                        j = stack.pop()
                        left[j] = j - i
                    left[i] = 0
            return left, right

        dp = []
        for i in range(1, 4):
            dp.append(helper(i))
        ans = []
        for i, c in queries:
            cur = dp[c - 1][0][i] if dp[c - 1][0][i] < dp[c - 1][1][i] else dp[c - 1][1][i]
            ans.append(cur if cur != float('inf') else -1)
        return ans
