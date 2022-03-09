# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
#
# 在加热器的加热半径范围内的每个房屋都可以获得供暖。
#
# 现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。
#
# 说明：所有供暖器都遵循你的半径标准，加热的半径也一样。
#
#  
#
# 示例 1:
#
# 输入: houses = [1,2,3], heaters = [2]
# 输出: 1
# 解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
# 示例 2:
#
# 输入: houses = [1,2,3,4], heaters = [1,4]
# 输出: 1
# 解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
# 示例 3：
#
# 输入：houses = [1,5], heaters = [2]
# 输出：3

import bisect
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # ans = 0
        # heaters.sort()
        # n = len(heaters)
        # for house in houses:
        #     pos = bisect.bisect(heaters, house)
        #     # 右边最近的取暖器距离
        #     right = heaters[pos] - house if pos < n else float("inf")
        #     # 左边同理
        #     left = house - heaters[pos-1] if pos > 0 else float("inf")
        #     # 选距离最近的
        #     distance = min(left,right)
        #     # 返回所有house距离最近中最远的
        #     ans = max(ans, distance)
        # return ans

        # 排序 双指针
        ans = 0
        houses.sort()
        heaters.sort()
        j = 0
        for i, house in enumerate(houses):
            # 当前房屋与当前heater的距离
            curDistance = abs(house - heaters[j])
            # 当下一个heater存在且更近，更新j,和curdistance
            while j + 1 < len(heaters) and abs(houses[i] - heaters[j]) >= abs(houses[i] - heaters[j + 1]):
                j += 1
                curDistance = min(curDistance, abs(houses[i] - heaters[j]))
            # 在所有房屋中选出最大值
            ans = max(ans, curDistance)
        return ans


