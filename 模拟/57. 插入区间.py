# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
#
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
#
#  
#
# 示例 1：
#
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
# 示例 2：
#
# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
# 示例 3：
#
# 输入：intervals = [], newInterval = [5,7]
# 输出：[[5,7]]
# 示例 4：
#
# 输入：intervals = [[1,5]], newInterval = [2,3]
# 输出：[[1,5]]
# 示例 5：
#
# 输入：intervals = [[1,5]], newInterval = [2,7]
# 输出：[[1,7]]

import bisect


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # bisect.insort_right(intervals, newInterval)
        # # print(intervals)
        # ans = [intervals[0]]
        # for i in range(1, len(intervals)):
        #     if intervals[i][0] <= ans[-1][1]:
        #         ans[-1][1] = max(ans[-1][1],intervals[i][1])
        #     else:
        #         ans.append(intervals[i])
        # return ans

        left, right = newInterval
        placed = False
        ans = []
        for l, r in intervals:
            if r < left:
                ans.append([l, r])
            elif l > right:
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([l, r])
            else:
                left = min(left, l)
                right = max(right, r)
            # print(ans, left,right)
        if not placed:
            ans.append([left, right])
        return ans



