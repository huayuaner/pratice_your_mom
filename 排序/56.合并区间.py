# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
#
#  
#
# 示例 1：
#
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2：
#
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort()
        # ans = []
        # n = len(intervals)
        # i = 0
        # while i<n:
        #     start = intervals[i][0]
        #     end = intervals[i][1]
        #     while i<n-1 and end >= intervals[i+1][0]:
        #         end = max(intervals[i+1][1],end)
        #         i += 1
        #     ans.append([start,end])
        #     i+=1
        # return ans
            
        intervals.sort(key = lambda x: x[0])

        ans = []
        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans