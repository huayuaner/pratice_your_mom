#输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。


cur = dum = ListNode(0)
while l1 and l2:
    if l1.val < l2.val:
        cur.next, l1 = l1, l1.next
    else:
        cur.next, l2 = l2, l2.next
    cur = cur.next
cur.next = l1 if l1 else l2
return dum.next

#递归
def mergeTwoLists(l1: ListNode, l2: ListNode):
    if l1 == None:return l2
    if l2 == None :return l1
    if l1.val <= l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2