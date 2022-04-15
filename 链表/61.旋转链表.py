# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
# from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # stack1,stack2 = [], []
        # cur = head
        # length = 0
        # while cur:
        #     stack1.append(cur)
        #     cur = cur.next

        # if len(stack1)<=1:
        #     return head
        # k = k%len(stack1)
        # # print(stack1)
        # # k=3
        # while k:
        #     # print(stack1, stack2)
        #     tail = stack1.pop()
        #     # print(tail)
        #     if len(stack1)==0:
        #         stack1, stack2 = stack2[::-1], stack1
        #     # print(stack1)
        #     stack1[-1].next = None
        #     tail.next = head
        #     head = tail
        #     stack2.append(head)
        #     # print(stack1)
        #     # print(head, stack1, stack2)
        #     k -= 1
        # return head
        if not head:
            return
        tail = head  # 找尾巴
        length = 1
        while tail.next:
            length += 1
            tail = tail.next
        if length == 1:
            return head
        # print(tail)
        tail.next = head  # 形成闭环
        k = length - k % length  # n-取余得到应该转的长度

        while k:
            tail = tail.next
            k -= 1
        ans = tail.next
        tail.next = None
        # print(tail)
        return ans






