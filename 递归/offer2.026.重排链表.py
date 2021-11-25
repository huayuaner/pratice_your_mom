def reorderList(self, head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    """

    # def fast_slow(head):
    #     fast, slow = head, head
    #     while fast.next and fast.next.next:
    #         fast = fast.next.next
    #         slow = slow.next
    #     return slow
    # def reverse(head):
    #     pre = None
    #     cur = head
    #     while cur != None:
    #         nex_node = cur.next
    #         cur.next = pre
    #         pre = cur
    #         cur = nex_node
    #     return pre
    # dum = cur = ListNode(0)
    # first_position = head
    # first_end = fast_slow(head)
    # second_position = reverse(first_end.next)
    # first_end.next=None
    # #print(first_position,' ', second_position)
    # while first_position and second_position:
    #     nex_node1, nex_node2 = first_position.next, second_position.next
    #     cur.next = first_position
    #     cur.next.next = second_position
    #     #print(cur,' ',first_position)
    #     first_position, second_position = nex_node1, nex_node2
    #    # print(first_position,' ', second_position)
    #     cur = cur.next.next

    # cur.next = first_position if first_position else second_position
    # return dum.next
    def reorderList_(head, begin, end):

        if (end - begin == 1):
            # print(head, ' ', head.next)
            return head, head.next

        if (end - begin == 0):
            return head, head

        headAndTail = reorderList_(head.next, begin + 1, end - 1)
        # print(head)
        head.next = headAndTail[1].next

        headAndTail[1].next = headAndTail[1].next.next
        print(head, ' ', headAndTail[0], ' ', headAndTail[1])
        head.next.next = headAndTail[0]
        # print( headAndTail[0], ' ', headAndTail[1])
        return head, headAndTail[1]

    if (head == None):
        return None

    lens = 0
    temp = head
    while (temp != None):
        temp = temp.next
        lens += 1

    reorderList_(head, 0, lens - 1)