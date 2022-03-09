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

        timePoints = sorted(timePoints)
        ans = float('inf')
        n = len(timePoints)
        # 总共右1440种时间，如果长度大于1440，必有相同的时间
        if n > 1440:
            return 0
        for i in range(n):
            M = int(timePoints[i][:2]) * 60 + int(timePoints[i][3:])

            if i != 0:
                M_pre = int(timePoints[i - 1][:2]) * 60 + int(timePoints[i - 1][3:])
            else:
                M_pre = int(timePoints[-1][:2]) * 60 + int(timePoints[-1][3:])
            # if i !=  n-1:
            #     M_pos = int(timePoints[i+1][:2])*60+int(timePoints[i+1][3:])
            # else:
            #     M_pos = int(timePoints[0][:2])*60+int(timePoints[0][3:])
            pre = abs(M_pre - M) if abs(M_pre - M) <= 720 else 1440 - abs(M_pre - M)
            # pos = abs(M_pos - M) if abs(M_pos - M)<= 720 else 1440 - abs(M_pos - M)
            if pre == 0:  # or pos == 0:
                return 0
            ans = min(ans, pre)
        return ans

