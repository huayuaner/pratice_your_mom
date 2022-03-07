# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

dum = cur = ListNode(0)  # dum指向的头节点也发生了变化
cur.next = head


# while cur.next != None and cur.next.next!=None:
#     node1= cur.next  #保存的是链表往后遍历无法碰到的位置
#     cur.next = node1.next
#     node1.next = node1.next.next
#     cur.next.next = node1
#     cur = node1
#return dum.next
def func(cur):
    if cur.next == None or cur.next.next == None:
        return
    else:
        node1 = cur.next
        cur.next = node1.next
        node1.next = node1.next.next
        cur.next.next = node1

    return func(node1)


func(cur)
return dum.next