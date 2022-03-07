# 给定两个 非空链表 l1和 l2 来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
#
# 可以假设除了数字 0 之外，这两个数字都不会以零开头。
#
# 输入：l1 = [7,2,4,3], l2 = [5,6,4]
# 输出：[7,8,0,7]
# 示例2：
#
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[8,0,7]
# 示例3：
#
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #反转链表+链表求和
        def reverse(head):
            pre = None
            cur = head
            while cur:
                nex_node = cur.next
                cur.next = pre
                pre = cur
                cur = nex_node

            return pre

        l1 = reverse(l1)
        l2 = reverse(l2)
        cur = dum = ListNode(0)
        add = 0

        while l1 or l2 or add:
            # 使用if控制链表的迭代
            sum_ = (l1.val if l1 else 0) + (l2.val if l2 else 0) + add
            cur.next = ListNode(sum_ % 10)
            add = sum_ // 10
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            cur = cur.next

        # print(dum.next)
        return reverse(dum.next)



