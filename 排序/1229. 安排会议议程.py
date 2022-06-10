# 给定两个人的空闲时间表：slots1 和 slots2，以及会议的预计持续时间 duration，请你为他们安排 时间段最早 且合适的会议时间。
#
# 如果没有满足要求的会议时间，就请返回一个 空数组。
#
# 「空闲时间」的格式是 [start, end]，由开始时间 start 和结束时间 end 组成，表示从 start 开始，到 end 结束。 
#
# 题目保证数据有效：同一个人的空闲时间不会出现交叠的情况，也就是说，对于同一个人的两个空闲时间 [start1, end1] 和 [start2, end2]，要么 start1 > end2，要么 start2 > end1。
#
#  
#
# 示例 1：
#
# 输入：slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
# 输出：[60,68]
# 示例 2：
#
# 输入：slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
# 输出：[]

import bisect


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # slots1.sort()
        # slots2.sort()
        # m,n = len(slots1), len(slots2)
        # if n>m:
        #     slots1,slots2 = slots2, slots1
        #     m,n = n,m
        # for slot in slots1:
        #     idx = bisect.bisect_left(slots2,slot)
        #     if idx == 0:
        #         start =  max(slot[0],slots2[0][0])
        #         avaliable_time = min(slots2[0][1],slot[1]) -start

        #     elif idx == n:
        #         start =  max(slot[0],slots2[n-1][0])
        #         avaliable_time = min(slots2[n-1][1],slot[1]) - max(slot[0],slots2[n-1][0])
        #     else:
        #         time_1 = min(slots2[idx-1][1],slot[1]) - max(slot[0],slots2[idx-1][0])
        #         time_2 = min(slots2[idx][1],slot[1]) - max(slot[0],slots2[idx][0])
        #         if time_1>time_2:
        #             start =  max(slot[0],slots2[idx-1][0])
        #             avaliable_time = time_1
        #         else:
        #             start =  max(slot[0],slots2[idx][0])
        #             avaliable_time = time_2
        #     # print(start, avaliable_time,duration)
        #     if avaliable_time >= duration:
        #         return [start,start+duration]
        # return []

        # 双指针
        slots1.sort()
        slots2.sort()
        m, n = len(slots1), len(slots2)
        i = j = 0
        while i < m and j < n:
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            avaliable_time = end - start
            # print(avaliable_time)
            if avaliable_time >= duration:
                return [start, start + duration]
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        return []


