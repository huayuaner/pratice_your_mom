cur = dum = ListNode(0)
while l1 and l2:
    if l1.val < l2.val:
        cur.next, l1 = l1, l1.next
    else:
        cur.next, l2 = l2, l2.next
    cur = cur.next
cur.next = l1 if l1 else l2
return dum.next

