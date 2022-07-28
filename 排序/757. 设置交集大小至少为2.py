# 一个整数区间 [a, b]  ( a < b ) 代表着从 a 到 b 的所有连续整数，包括 a 和 b。
#
# 给你一组整数区间intervals，请找到一个最小的集合 S，使得 S 里的元素与区间intervals中的每一个整数区间都至少有2个元素相交。
#
# 输出这个最小集合S的大小。
#
# 示例 1:
#
# 输入: intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
# 输出: 3
# 解释:
# 考虑集合 S = {2, 3, 4}. S与intervals中的四个区间都有至少2个相交的元素。
# 且这是S最小的情况，故我们输出3。
# 示例 2:
#
# 输入: intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
# 输出: 5
# 解释:
# 最小的集合S = {1, 2, 3, 4, 5}.

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[1]))
        # print(intervals)
        n = len(intervals)
        a,b,ans = -1, -1, 0
        # end = intervals[0][1]
        for left,right in intervals:
            if left>b:
                a,b, ans = right-1, right, ans + 2
            elif left>a:
                a,b,ans = b, right, ans + 1
            # print(a,b)
            # print(ans,a,b)
        return ans