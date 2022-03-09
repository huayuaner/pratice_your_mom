# 输入两个链表，找出它们的第一个公共节点。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 用哈希集合存节点
        # HashSet = set()
        # cur = headA
        # while cur:
        #     HashSet.add(cur)
        #     cur = cur.next
        # cur = headB
        # while cur:
        #     if cur in HashSet:
        #         return cur
        #     cur = cur.next
        # return None

        # 双指针
        if not headA or not headB:
            return None
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
