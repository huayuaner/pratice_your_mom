# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dum = cur = ListNode(-1)
        # cur1, cur2 = list1, list2
        # while cur1 and cur2:
        #     # nex_node1 = cur1.next
        #     # nex_node2 = cur2.next
        #     if cur1.val <= cur2.val:
        #         cur.next = cur1
        #         cur1 = cur1.next
        #     else:
        #         cur.next = cur2
        #         cur2 = cur2.next
        #     cur = cur.next
        # cur.next = cur1 if cur1 else cur2
        # return dum.next

        if not list1:
            return list2
        elif not list2:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
