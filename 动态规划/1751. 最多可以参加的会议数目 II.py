# 给你一个 events 数组，其中 events[i] = [startDayi, endDayi, valuei] ，表示第 i 个会议在 startDayi 天开始，第 endDayi 天结束，如果你参加这个会议，你能得到价值 valuei 。同时给你一个整数 k 表示你能参加的最多会议数目。
#
# 你同一时间只能参加一个会议。如果你选择参加某个会议，那么你必须 完整 地参加完这个会议。会议结束日期是包含在会议内的，也就是说你不能同时参加一个开始日期与另一个结束日期相同的两个会议。
#
# 请你返回能得到的会议价值 最大和 。
#
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # dp[i][k] 表示在时间i之前开始 最多能做 k 件事的最高价值
        # 按结束时间排序
        events.sort(key=lambda x: x[1])
        # 得到最后的那个时间
        # n = events[-1][1]

        # 插入一个哨兵位置，这样二分最起码的结果最少是0，不会越界
        events.insert(0, [0, 0, 0])
        n = len(events)
        dp = [[0 for _ in range(k + 1)] for _ in range(n)]

        # 找到l到r中在target前且结束最晚的会议id
        def find(l, r, target):
            while l < r:
                m = l + (r - l + 1) // 2
                if events[m][1] < target:
                    l = m
                else:
                    r = m - 1
            return l

        for i, (start, end, val) in enumerate(events):
            pre_idx = find(0, i - 1, start)

            for j in range(1, k + 1):
                # print(pre_idx,i,j)
                dp[i][j] = max(dp[i - 1][j], dp[pre_idx][j - 1] + val)
        return dp[-1][-1]




