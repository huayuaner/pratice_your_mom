# 设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。
#
# 循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。
#
# 你的实现应该支持如下操作：
#
# MyCircularQueue(k): 构造器，设置队列长度为 k 。
# Front: 从队首获取元素。如果队列为空，返回 -1 。
# Rear: 获取队尾元素。如果队列为空，返回 -1 。
# enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
# deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
# isEmpty(): 检查循环队列是否为空。
# isFull(): 检查循环队列是否已满。

from collections import deque


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyCircularQueue:

    def __init__(self, k: int):
        # 指向头和尾的两个指针
        # self.front = self.tail = 0
        # 这里的(k+1)是为了取消front == tail 的二义性
        # 如果是k，那么front == tail既可以表示列表为空，也可以表示列表为满
        # k+1 front == tail表示列表为空  (tail+1)%(k+1) == front表示列表满
        # self.elements = [None]*(k+1)

        # 链表
        self.head = self.tail = None
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        # if self.isFull():
        #     return False
        # self.elements[self.tail] = value
        # self.tail = (self.tail + 1) % len(self.elements)
        # return True

        # 链表
        if self.isFull():
            return False
        node = ListNode(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        # if self.isEmpty():
        #     return False
        # self.front = (self.front + 1)%len(self.elements)
        # return True

        # 链表
        if self.isEmpty():
            return False
        self.head = self.head.next
        self.size -= 1
        return True

    def Front(self) -> int:
        # return self.elements[self.front] if not self.isEmpty() else -1

        # 链表
        return self.head.val if not self.isEmpty() else -1

    def Rear(self) -> int:
        # return self.elements[(self.tail-1)%len(self.elements)] if not self.isEmpty() else -1

        return self.tail.val if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        # return self.front == self.tail

        return self.size == 0

    def isFull(self) -> bool:
        # return (self.tail+1)%len(self.elements) == self.front

        return self.size == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()