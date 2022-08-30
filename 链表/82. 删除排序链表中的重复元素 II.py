# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dum = pre = ListNode(-1)
        # dum.next = head
        # pre_val = None
        # cur = head
        # while cur:
        #     if pre_val == None:
        #         pre_val = cur.val
        #         # pre = pre.next
        #     elif pre_val!= cur.val :
        #         pre_val = cur.val
        #         pre = pre.next
        #     elif pre_val == cur.val:
        #         # print(pre,cur.val)
        #         while cur and cur.val == pre_val:
        #             cur = cur.next
        #         pre.next = cur
        #         if cur:
        #             pre_val = cur.val
        #         else:
        #             break
        #     cur = cur.next
        # return dum.next

        # 优雅写法
        if not head:
            return None
        dum = ListNode(-1, head)
        # 这里cur是最后一个非重复节点
        cur = dum
        while cur.next and cur.next.next:
            # 如果cur后两个节点值相同
            if cur.next.val == cur.next.next.val:
                # 记录重复值
                x = cur.next.val
                # 跳过重复值
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            # 不相同则更新cur
            else:
                cur = cur.next
        return dum.next
