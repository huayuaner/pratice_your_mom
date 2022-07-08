# 给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。
#
# 然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
#
# 你需要计算完成所有任务所需要的 最短时间 。
#
#  
#
# 示例 1：
#
# 输入：tasks = ["A","A","A","B","B","B"], n = 2
# 输出：8
# 解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B
#      在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。
# 示例 2：
#
# 输入：tasks = ["A","A","A","B","B","B"], n = 0
# 输出：6
# 解释：在这种情况下，任何大小为 6 的排列都可以满足要求，因为 n = 0
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# 诸如此类
#
from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 超时
        # ans = float('inf')
        # mission_num = len(tasks)
        # cnts = Counter(tasks)
        # def dfs(time, seen, mission_idx):
        #     if mission_idx == mission_num:
        #         nonlocal ans
        #         ans = min(ans, time)
        #         return
        #     if time >= ans:
        #         return
        #     flag = False
        #     for k in cnts:
        #         if cnts[k] == 0:
        #             continue
        #         if k not in seen or (k in seen and time-n>seen[k]):
        #             flag = True
        #             cnts[k] -= 1
        #             tmp = seen.get(k, -1)
        #             seen[k] = time
        #             dfs(time+1, seen, mission_idx+1)
        #             cnts[k] += 1
        #             if tmp!=-1:
        #                 seen[k] = tmp
        #             else:
        #                 del seen[k]
        #     if flag == False:
        #         dfs(time+1, seen, mission_idx)
        #     return
        # dfs(0, dict(), 0)
        # return ans
        length = len(tasks)
        if length < 2:
            return length
        cnts = Counter(tasks)
        # 按照次数排序
        # tasks_sorted = sorted(cnts.items(), key = lambda x:x[1], reverse=True)
        # 最少用的时间
        max_task_count = max(cnts.values())
        ans = (max_task_count - 1) * (n + 1)
        for task in cnts:
            if cnts[task] == max_task_count:
                ans += 1
        return ans if ans > length else length


