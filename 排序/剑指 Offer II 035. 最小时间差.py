# 给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。
#
#  
#
# 示例 1：
#
# 输入：timePoints = ["23:59","00:00"]
# 输出：1
# 示例 2：
#
# 输入：timePoints = ["00:00","23:59","00:00"]
# 输出：0
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        if n > 1440:
            return 0
        timePoints.sort()

        ans = 720
        for i in range(n):

            pre = timePoints[i - 1]
            hour_gap = int(pre[:2]) - int(timePoints[i][:2])
            min_gap = int(pre[3:]) - int(timePoints[i][3:])
            totalmin = abs(hour_gap) * 60 + abs(min_gap) if hour_gap * min_gap >= 0 else (
                                                                                                     abs(hour_gap) - 1) * 60 + 60 - abs(
                min_gap)
            if totalmin > 720:
                totalmin = 1440 - totalmin
            ans = min(ans, totalmin)
        return ans
