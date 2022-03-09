# 请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
#
# 若队列为空，pop_front 和 max_value 需要返回 -1
#
# 示例 1：
#
# 输入:
# ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
# [[],[1],[2],[],[],[]]
# 输出: [null,null,null,2,1,2]
# 示例 2：
#
# 输入:
# ["MaxQueue","pop_front","max_value"]
# [[],[],[]]
# 输出: [null,-1,-1]

class MaxQueue:

    def __init__(self):
        self.queue = []
        self.queue_max = []


    def max_value(self) -> int:
        if not self.queue_max:
            return -1
        else:
            return self.queue_max[0]



    def push_back(self, value: int) -> None:
        while self.queue_max and self.queue_max[-1]<value:
            self.queue_max.pop()
        self.queue_max.append(value)
        self.queue.append(value)


    def pop_front(self) -> int:
        if not self.queue:
            return -1
        value = self.queue.pop(0)
        if value == self.queue_max[0]:
            self.queue_max.pop(0)
        return value



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()