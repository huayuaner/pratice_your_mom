#输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）
def reversePrint(self, head: ListNode) -> List[int]:
    # res = []
    # while head != None:
    #     res.append(head.val)
    #     head = head.next

    # return res[::-1]
    return self.reversePrint(head.next) + [head.val] if head else []