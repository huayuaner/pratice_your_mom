# 给你一个链表的头节点 head ，判断链表中是否有环。
#
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
#
# 如果链表中存在环 ，则返回 true 。 否则，返回 false 。
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:


        # 快慢指针，有环必相遇
        if not head:
            return False
        slow, fast = head, head
        while 1:
            # 只用快指针判断即可，因为慢指针在快指针之前
            if  fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                if slow==fast:
                    return True
            else:
                return False


        # if not head:
        #     return False
        # fast,slow = head.next, head
        # while  fast and fast.next:
        #     if slow==fast:
        #         return True
        #     else:
        #         slow = slow.next
        #         fast = fast.next.next
        # return False