# 给定单链表的头节点 head ，请反转链表，并返回反转后的链表的头节点

def reverseList(self, head: ListNode) -> ListNode:
    # pre = None
    # cur = head
    # while(cur is not None):
    #     nex_node = cur.next
    #     cur.next = pre
    #     pre = cur
    #     cur = nex_node
    # return pre

    # 递归

    def func(cur, pre):
        if cur is None:
            return pre
        res = func(cur.next, cur)
        cur.next = pre #改变指向
        return res

    return func(head, None)