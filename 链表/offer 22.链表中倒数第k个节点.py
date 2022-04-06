输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。

 

示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 利用temp来记录到达末尾的时候
        # 相当于快慢指针
        # temp是快指针，head是慢指针，temp先跑了k个，所以head会在倒数k个停下
        temp = head
        for _ in range(k):
            temp = temp.next
        while temp:
            temp = temp.next
            head = head.next
        return head