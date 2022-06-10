# 给定一个由非重叠的轴对齐矩形的数组 rects ，其中 rects[i] = [ai, bi, xi, yi] 表示 (ai, bi) 是第 i 个矩形的左下角点，(xi, yi) 是第 i 个矩形的右上角点。设计一个算法来随机挑选一个被某一矩形覆盖的整数点。矩形周长上的点也算做是被矩形覆盖。所有满足要求的点必须等概率被返回。
#
# 在给定的矩形覆盖的空间内的任何整数点都有可能被返回。
#
# 请注意 ，整数点是具有整数坐标的点。
#
# 实现 Solution 类:
#
# Solution(int[][] rects) 用给定的矩形数组 rects 初始化对象。
# int[] pick() 返回一个随机的整数点 [u, v] 在给定的矩形所覆盖的空间内。
#
import random
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.preSum = [0]
        for x1,y1,x2,y2 in self.rects:
            self.preSum.append(self.preSum[-1]+(x2-x1+1)*(y2-y1+1))


    def pick(self) -> List[int]:
        # ans = None# self.rects[0]
        # curSum = 0
        # idx = 0
        # for i,(x1,y1,x2,y2) in enumerate(self.rects):
        #     cur = (x2-x1+1)*(y2-y1+1)
        #     curSum += cur
        #     if random.randint(0,curSum) <= cur:
        #         ans = [x1,y1,x2,y2]
        # x = random.randint(ans[0],ans[2])
        # y = random.randint(ans[1],ans[3])
        # return [x,y]

        w = random.randint(0,self.preSum[-1]-1)
        idx = bisect_right(self.preSum,w)-1
        x = random.randint(self.rects[idx][0],self.rects[idx][2])
        y = random.randint(self.rects[idx][1],self.rects[idx][3])
        return [x,y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()