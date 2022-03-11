# 给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
#
# 输入：head = [1,1,2]
# 输出：[1,2]
#
# 输入：head = [1,1,2,3,3]
# 输出：[1,2,3]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # cur = head
        # pre = None
        # while cur:
        #     # 循环掉重复部分
        #     while pre and cur and pre.val == cur.val:
        #         pre.next = cur.next
        #         cur = cur.next

        #     pre = cur
        #     cur = cur.next if cur else cur
        # return head

        cur = head
        while cur:
            # 小循环处理重复值
            forward = cur.next
            while forward:
                if forward.val == cur.val:
                    forward = forward.next
                else:
                    break
            cur.next = forward
            cur = cur.next
        return head