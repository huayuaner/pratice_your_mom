# 给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，返回 所需会议室的最小数量 。
#
#  
#
# 示例 1：
#
# 输入：intervals = [[0,30],[5,10],[15,20]]
# 输出：2
# 示例 2：
#
# 输入：intervals = [[7,10],[2,4]]
# 输出：1

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # max_val = max([inter[1] for inter in intervals])
        # min_val = min([inter[0] for inter in intervals])
        # pre_sum = [0] * (max_val-min_val+1)
        # for inter in intervals:
        #     pre_sum[inter[0]-min_val] += 1
        #     # if inter[1]-min_val < max_val-min_val:
        #     pre_sum[inter[1]-min_val] -= 1
        # ans = pre_sum[0]
        # # print(pre_sum)
        # for i in range(1, len(pre_sum)):
        #     pre_sum[i] += pre_sum[i-1]
        #     ans = max(ans, pre_sum[i])
        # return ans

        # 排序 + 堆
        # intervals.sort(key = lambda x: x[0])
        # heap = []
        # heapq.heappush(heap, intervals[0][1])
        # ans = 1
        # for i in range(1, len(intervals)):
        #     if heap[0] <= intervals[i][0]:
        #         heapq.heappop(heap)
        #         # heapq.heappush(heap, intervals[i][1])
        #     else:
        #         ans += 1
        #     heapq.heappush(heap, intervals[i][1])
        # return ans

        time_point = []
        for inter in intervals:
            time_point.append([inter[0],1])
            time_point.append([inter[1],-1])
        time_point.sort(key=lambda x:(x[0],x[1]))
        ans = 0
        tmp = 0
        for t in time_point:
            tmp += t[1]
            ans = max(ans,tmp)
        return ans
