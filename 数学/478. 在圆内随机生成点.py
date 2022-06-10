# 给定圆的半径和圆心的位置，实现函数 randPoint ，在圆中产生均匀随机点。
#
# 实现 Solution 类:
#
# Solution(double radius, double x_center, double y_center) 用圆的半径 radius 和圆心的位置 (x_center, y_center) 初始化对象
# randPoint() 返回圆内的一个随机点。圆周上的一点被认为在圆内。答案作为数组返回 [x, y] 。
#  
#
# 示例 1：
#
# 输入:
# ["Solution","randPoint","randPoint","randPoint"]
# [[1.0, 0.0, 0.0], [], [], []]
# 输出: [null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]
# 解释:
# Solution solution = new Solution(1.0, 0.0, 0.0);
# solution.randPoint ();//返回[-0.02493，-0.38077]
# solution.randPoint ();//返回[0.82314,0.38945]
# solution.randPoint ();//返回[0.36572,0.17248]

import random
import math


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x = x_center
        self.y = y_center
        self.radius = radius
        self.area = math.pi * radius ** 2

    def randPoint(self) -> List[float]:
        # # x 的随机
        # x = random.uniform(self.x-self.radius, self.x+self.radius)
        # # 得到y的范围
        # y_field = [sqrt(self.radius**2 - (x-self.x)**2)+self.y,-sqrt(self.radius**2 - (x-self.x)**2)+self.y]
        # y =  random.uniform(y_field[0], y_field[1])
        # return [x,y]

        # 面积随机
        # 随机得到一个角度和一个随机面积的半径
        theta, r = random.uniform(0, 2 * math.pi), math.sqrt(random.uniform(0, self.area) / math.pi)
        return [self.x + math.cos(theta) * r, self.y + math.sin(theta) * r]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()