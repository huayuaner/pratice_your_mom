# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#
# push(x) —— 将元素 x 推入栈中。
# pop()—— 删除栈顶的元素。
# top()—— 获取栈顶元素。
# getMin() —— 检索栈中的最小元素。
class MinStack:

    def __init__(self):
        self.stack = list()

    def push(self, val: int) -> None:
        if not self.stack:

            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:

        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()