# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 归并
        def middle(head):
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
                # print(slow,fast)
            return slow

        def process(head):
            if not head:
                return
            mid = middle(head)
            if mid == head:
                if not head.next:
                    return head
                else:
                    if head.val <= head.next.val:
                        return head
                    else:
                        dum = head.next
                        head.next.next = head
                        head.next = None
                        return dum

            # print(111)
            l1 = head
            l2 = mid.next
            mid.next = None
            l1 = process(l1)
            l2 = process(l2)
            p1, p2 = l1, l2
            cur = dum = ListNode(0)
            while p1 and p2:
                if p1.val < p2.val:
                    cur.next = p1
                    p1 = p1.next
                else:
                    cur.next = p2
                    p2 = p2.next
                cur = cur.next
            cur.next = p1 if not p2 else p2

            return dum.next

        return process(head)

