# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
#
#  
#
# 示例:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.min();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.min();   --> 返回 -2.

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()

    def push(self, x: int) -> None:
        if self.stack:
            min_ = min(x, self.stack[-1][1])
            self.stack.append([x, min_])
        else:
            self.stack.append([x, x])

    def pop(self) -> None:
        return self.stack.pop()[0] if self.stack else -1

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else -1

    def min(self) -> int:
        return self.stack[-1][1] if self.stack else -1

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()