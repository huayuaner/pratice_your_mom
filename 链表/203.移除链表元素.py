#给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

def removeElements(self, head: ListNode, val: int) -> ListNode:
    # cur = dum = ListNode(0)
    # cur.next = head
    # dum.next = head
    # while cur.next != None :
    #     if cur.next.val == val:
    #             cur.next = cur.next.next

    #     elif cur.next != None :
    #         #print('111')
    #         cur = cur.next

    # return dum.next
    if head == None:
        return head
    head.next = self.removeElements(head.next, val)
    return head if head.val != val else head.next