# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
# 示例 2：
#
# 输入：head = [1], n = 1
# 输出：[]
# 示例 3：
#
# 输入：head = [1,2], n = 1
# 输出：[1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dum = ListNode(0)
        dum.next = head
        slow,fast = head, head
        for _ in range(n):
            fast = fast.next
        pre = dum
        while fast:
            pre = slow
            slow = slow.next
            fast = fast.next
        pre.next = slow.next
        return dum.next