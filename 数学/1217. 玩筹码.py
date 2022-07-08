# 有 n 个筹码。第 i 个筹码的位置是 position[i] 。
#
# 我们需要把所有筹码移到同一个位置。在一步中，我们可以将第 i 个筹码的位置从 position[i] 改变为:
#
# position[i] + 2 或 position[i] - 2 ，此时 cost = 0
# position[i] + 1 或 position[i] - 1 ，此时 cost = 1
#
from collections import Counter
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # 暴力双遍历
        # n = len(position)
        # ans = float('inf')
        # for i in position:
        #     cost = 0
        #     for j in position:
        #         if j==i:continue
        #         cost += (1 if abs(i-j)%2 else 0)
        #     ans = min(ans, cost)
        # return ans

        # 奇偶统计
        cnts = Counter([i%2 for i in position])
        # print(cnts)
        return min(cnts[0], cnts[1])