给你一个单链表，随机选择链表的一个节点，并返回相应的节点值。每个节点 被选中的概率一样 。

实现 Solution 类：

Solution(ListNode head) 使用整数数组初始化对象。
int getRandom() 从链表中随机选择一个节点并返回该节点的值。链表中所有节点被选中的概率相等


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        # self.lens = 0
        # dum = ListNode(0)
        # dum.next = head
        # while dum.next:
        #     self.lens+=1
        #     dum = dum.next
        # print(self.lens)

    def getRandom(self) -> int:
        # node = self.head
        # if self.lens == 1:
        #     return node.val
        # for i in range(self.lens, 1, -1):
        #     #print(self.head)

        #     if random.random() < 1 / i:
        #         return node.val
        #     if i == 2:
        #         return node.next.val
        #     node = node.next

        # 水桶抽样法
        node, i, ans = self.head, 0, None
        while node:
            if not randint(0, i):
                ans = node.val
            node = node.next
            i += 1
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()