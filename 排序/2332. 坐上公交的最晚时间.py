# 给你一个下标从 0 开始长度为 n 的整数数组 buses ，其中 buses[i] 表示第 i 辆公交车的出发时间。同时给你一个下标从 0 开始长度为 m 的整数数组 passengers ，其中 passengers[j] 表示第 j 位乘客的到达时间。所有公交车出发的时间互不相同，所有乘客到达的时间也互不相同。
#
# 给你一个整数 capacity ，表示每辆公交车 最多 能容纳的乘客数目。
#
# 每位乘客都会搭乘下一辆有座位的公交车。如果你在 y 时刻到达，公交在 x 时刻出发，满足 y <= x  且公交没有满，那么你可以搭乘这一辆公交。最早 到达的乘客优先上车。
#
# 返回你可以搭乘公交车的最晚到达公交站时间。你 不能 跟别的乘客同时刻到达。
#
# 注意：数组 buses 和 passengers 不一定是有序的。
#
#  

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        m,n = len(buses), len(passengers)
        buses.sort()
        passengers.sort()
        j = 0
        for bus in buses:
            c = capacity
            while c and j<n and passengers[j]<=bus:
                c -= 1
                j += 1
        # 最后一个上车的人
        j -= 1
        # 如果最后遍历完还有容量上人，那么最晚可能就是发车时间
        # 如果没有容量上人，那么最晚只可能是最后一个上车的人之前的时间
        ans = buses[-1] if c else passengers[j]
        while ans == passengers[j]:
            ans -= 1
            j -= 1
        return ans