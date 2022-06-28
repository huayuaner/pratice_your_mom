# 给定员工的 schedule 列表，表示每个员工的工作时间。
#
# 每个员工都有一个非重叠的时间段  Intervals 列表，这些时间段已经排好序。
#
# 返回表示 所有 员工的 共同，正数长度的空闲时间 的有限时间段的列表，同样需要排好序。
#
# 示例 1：
#
# 输入：schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
# 输出：[[3,4]]
# 解释：
# 共有 3 个员工，并且所有共同的
# 空间时间段是 [-inf, 1], [3, 4], [10, inf]。
# 我们去除所有包含 inf 的时间段，因为它们不是有限的时间段。
#  
#
# 示例 2：
#
# 输入：schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
# 输出：[[5,6],[7,9]]

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
import heapq


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # 直接求所有员工的空闲时间
        # 因为所有员工的时间是排好序的 所以pq里是最早的开始时间
        # pq = [(s[0].start, idx, 0) for idx,s in enumerate(schedule)]
        # ans = []
        # # 全局最早结束时间
        # end = min([s.end for sche in schedule for s in sche])
        # # print(end)
        # heapq.heapify(pq)
        # while pq:
        #     start, e_id, e_job_idx = heapq.heappop(pq)
        #     # print(start, end)
        #     # 全局最早结束时间和当前剩余工作的最早开始时间的比较
        #     if end < start:
        #         ans.append(Interval(end, start))
        #     # 最早结束时间的更新
        #     end = max(end, schedule[e_id][e_job_idx].end)
        #     # 放入当前e_id处理结束的工作的下一个工作
        #     if e_job_idx + 1<len(schedule[e_id]):
        #         heapq.heappush(pq, (schedule[e_id][e_job_idx+1].start, e_id, e_job_idx+1))
        # return ans

        # 排序
        # l = []
        # for sche in schedule:
        #     for s in sche:
        #         l.append(s)
        # if len(l) <= 1:
        #     return []
        # l.sort(key = lambda x: (x.start, x.end))
        # end = min(e.end for e in l)
        # ans = []
        # for job in l:
        #     if job.start > end:
        #         ans.append(Interval(end, job.start))
        #     end = max(end, job.end)
        # return ans

        # 公交车上下乘客
        # 乘客为0的时间
        times = []
        for sche in schedule:
            for s in sche:
                times.append((s.start, 1))
                times.append((s.end, -1))
        # 先上后下，防止出现0的区间
        times.sort(key=lambda x: (x[0], -x[1]))
        # print(times)
        person_num = 0
        pre = None
        ans = []
        for time, behavior in times:
            if person_num == 0 and pre is not None:
                ans.append(Interval(pre, time))
            person_num += behavior
            pre = time
        return ans














