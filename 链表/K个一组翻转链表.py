# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。
#
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
# 进阶：
#
# 你可以设计一个只使用常数额外空间的算法来解决此问题吗？
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            cur = head
            prev = None
            while cur:
                # 记录尾节点
                if not prev:
                    tail = cur
                nex_node = cur.next
                cur.next = prev
                prev = cur
                cur = nex_node
            return prev, tail

        # cur =  ListNode(0)
        prev = None
        cur = head
        cnt = k
        while cur:
            cnt -= 1
            # print(cnt, cur)
            if cnt == 0:
                if not prev:
                    nex_node = cur.next
                    cur.next = None
                    head, prev = reverse(head)
                    # print(head, prev)
                    prev.next = nex_node
                    # print(prev, cur)
                else:
                    # print(prev, cur)
                    # 截出需要反转的一段链表
                    nex_node = cur.next
                    nex_node2 = prev.next
                    cur.next = None
                    prev.next = None
                    # 返回反转的头尾
                    cur_head, cur_tail = reverse(nex_node2)
                    # print(nex_node2)
                    # 拼接起来
                    prev.next = cur_head
                    cur_tail.next = nex_node
                    prev = cur_tail
                cur = prev.next
                cnt = k

            else:
                cur = cur.next
        return head






