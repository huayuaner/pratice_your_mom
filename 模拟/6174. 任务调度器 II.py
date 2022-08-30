# 给你一个下标从 0 开始的正整数数组 tasks ，表示需要 按顺序 完成的任务，其中 tasks[i] 表示第 i 件任务的 类型 。
#
# 同时给你一个正整数 space ，表示一个任务完成 后 ，另一个 相同 类型任务完成前需要间隔的 最少 天数。
#
# 在所有任务完成前的每一天，你都必须进行以下两种操作中的一种：
#
# 完成 tasks 中的下一个任务
# 休息一天
# 请你返回完成所有任务所需的 最少 天数。
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        day = 0
        seen = dict()
        for task in tasks: # 按顺序完成
            day += 1
            if task in seen:
                day = max(day, seen[task] + space + 1)
            seen[task] = day
        return day

