class MinStack:

    def __init__(self):
        # self.stack = []

        # 用一个变量完成
        self.min_value = -1
        self.stack = []

    def push(self, val: int) -> None:
        # if not self.stack:
        #     self.stack.append([val,val])
        # else:
        #     self.stack.append([val,min(val, self.stack[-1][1])])
        if not self.stack:
            # 当前值和最小值的差值
            self.stack.append(0)
            self.min_value = val
        else:
            diff = val - self.min_value
            self.stack.append(diff)
            # 差值大于0说明当前值大于最大值，小于等于0，当前值就是最小值
            self.min_value = self.min_value if diff > 0 else val

    def pop(self) -> None:
        # self.stack.pop()
        diff = self.stack.pop()
        # 如果diff<0，说明当前值就是最小值
        if diff < 0:
            # 这里的diff 是 val - self.min_value(上一个最小值),这时的self.min_value是val，相减得到上一个最小值
            self.min_value = self.min_value - diff

    def top(self) -> int:
        # return self.stack[-1][0]
        return self.stack[-1] + self.min_value if self.stack[-1] >= 0 else self.min_value

    def getMin(self) -> int:
        # return self.stack[-1][1]

        return self.min_value

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()