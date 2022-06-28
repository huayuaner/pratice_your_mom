# 给定一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，请你判断一个人是否能够参加这里面的全部会议。
#
#  
#
# 示例 1：
#
# 输入：intervals = [[0,30],[5,10],[15,20]]
# 输出：false
# 示例 2：
#
# 输入：intervals = [[7,10],[2,4]]
# 输出：true
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort()

        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                return False
            else:
                end = intervals[i][1]
        return True