# 设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。
#
# 在链表类中实现这些功能：
#
# get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
# addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
# addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
# addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
# deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
# class DoubleLinkL:
#     def __init__(self, val, prev=None, next=None):
#         self.val = val
#         self.prev = prev
#         self.next = next

# 单向链表
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        # self.size = 0
        # # 假头假尾
        # self.head,self.tail = DoubleLinkL(-1),DoubleLinkL(-1)
        # self.head.next = self.tail
        # self.tail.prev = self.head

        self.size = 0
        # 假头
        self.head = ListNode(-1)

    def get(self, index: int) -> int:
        # if index < 0 or index >= self.size:
        #     return -1
        # if index  <= self.size//2:
        #     cur = self.head.next
        #     while index:
        #         # print(cur)
        #         cur = cur.next
        #         index -= 1
        #     # return cur.val
        # else:
        #     cur = self.tail.prev
        #     while index != self.size-1:
        #         index += 1
        #         cur = cur.prev
        # return cur.val

        if index < 0 or index >= self.size:
            return -1
        cur = self.head.next
        while index:
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        # node = DoubleLinkL(val, self.head, self.head.next)
        # self.head.next.prev = node
        # self.head.next = node
        # self.size += 1
        # print(self.size,0)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        # node = DoubleLinkL(val, self.tail.prev, self.tail)
        # self.tail.prev.next = node
        # self.tail.prev = node
        # self.size += 1
        # print(self.size,1)

    def addAtIndex(self, index: int, val: int) -> None:
        # if index <= 0:
        #     self.addAtHead(val)
        #     # return
        # elif index==self.size:
        #     self.addAtTail(val)
        #     # return
        # elif index>self.size:
        #     return
        # else:
        #     cur = self.head.next
        #     while index:
        #         cur = cur.next
        #         index -= 1
        #     prev = cur.prev
        #     node = DoubleLinkL(val, prev, cur)
        #     prev.next = node
        #     cur.prev = node
        #     self.size += 1
        # print(self.size,2)
        # return
        if index < 0:
            index = 0
        if index > self.size:
            return
        cur = self.head
        while index:
            cur = cur.next
            index -= 1
        node = ListNode(val)
        node.next = cur.next
        cur.next = node
        cur = self.head.next
        # while cur:
        #     print(cur.val)
        #     cur = cur.next
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
            # # cur = self.head.next
        # # while cur:
        # #     print(cur.val)
        # #     cur = cur.next
        # cur = self.head.next
        # # print(self.size, index)

        # while index:
        #     index -= 1
        #     cur = cur.next
        # # print(cur.val)
        # cur.prev.next = cur.next
        # # if cur.next:
        # cur.next.prev = cur.prev
        # self.size -= 1
        # # print(self.size,3)

        cur = self.head
        while index:
            index -= 1
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)