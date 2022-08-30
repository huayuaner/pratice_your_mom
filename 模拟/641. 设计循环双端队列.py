# 设计实现双端队列。
#
# 实现 MyCircularDeque 类:
#
# MyCircularDeque(int k) ：构造函数,双端队列最大为 k 。
# boolean insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true ，否则返回 false 。
# boolean insertLast() ：将一个元素添加到双端队列尾部。如果操作成功返回 true ，否则返回 false 。
# boolean deleteFront() ：从双端队列头部删除一个元素。 如果操作成功返回 true ，否则返回 false 。
# boolean deleteLast() ：从双端队列尾部删除一个元素。如果操作成功返回 true ，否则返回 false 。
# int getFront() )：从双端队列头部获得一个元素。如果双端队列为空，返回 -1 。
# int getRear() ：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1 。
# boolean isEmpty() ：若双端队列为空，则返回 true ，否则返回 false  。
# boolean isFull() ：若双端队列满了，则返回 true ，否则返回 false 。
class MyCircularDeque:
    # 在循环队列的基础上设计双端循环队列

    def __init__(self, k: int):
        # self.head = self.tail = 0
        # self.capacity = k + 1
        # self.arr = [0]*self.capacity

        self.size = 0
        self.limited = k
        # 假头假尾
        self.head = DoubleLinkedNode(-1)
        self.tail = DoubleLinkedNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, value: int) -> bool:
        # if not self.isFull():
        #     self.head = (self.head - 1 + self.capacity) % self.capacity
        #     self.arr[self.head] = value
        #     return True
        # else:
        #     return False

        if not self.isFull():
            node = DoubleLinkedNode(value)
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            node.prev = self.head
            self.size += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        # if not self.isFull():
        #     self.arr[self.tail] = value
        #     self.tail = (self.tail + 1) % self.capacity
        #     return True
        # else:
        #     return False

        if not self.isFull():
            node = DoubleLinkedNode(value)
            node.prev = self.tail.prev
            self.tail.prev.next = node
            node.next = self.tail
            self.tail.prev = node
            self.size += 1
            return True
        return False

    def deleteFront(self) -> bool:
        # if not self.isEmpty():
        #     self.head = (self.head + 1) % self.capacity
        #     return True
        # else:
        #     return False

        if not self.isEmpty():
            self.head.next.next.prev = self.head
            self.head.next = self.head.next.next
            self.size -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        # if not self.isEmpty():
        #     self.tail = (self.tail - 1 + self.capacity) % self.capacity
        #     return True
        # else:
        #     return False

        if not self.isEmpty():
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
            self.size -= 1
            return True
        return False

    def getFront(self) -> int:
        # if not self.isEmpty():
        #     return self.arr[self.head]
        # else:
        #     return -1

        if not self.isEmpty():
            return self.head.next.val
        return -1

    def getRear(self) -> int:
        # if not self.isEmpty():
        #     return self.arr[(self.tail - 1 + self.capacity)%self.capacity]
        # else:
        #     return -1

        if not self.isEmpty():
            return self.tail.prev.val
        return -1

    def isEmpty(self) -> bool:
        # return self.head == self.tail

        return self.size == 0

    def isFull(self) -> bool:
        # return self.head == (self.tail + 1) % self.capacity

        return self.size == self.limited


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


# 双向链表
class DoubleLinkedNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next