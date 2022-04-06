# 给定两个用链表表示的整数，每个节点包含一个数位。
#
# 这些数位是反向存放的，也就是个位排在链表首部。
#
# 编写函数对这两个整数求和，并用链表形式返回结果。
#
# 示例：
#
# 输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
# 输出：2 -> 1 -> 9，即912
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    def func(cur, l1, l2, carry):
        if l1 == None and l2 == None and carry == 0:
            return

        sum_ = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        carry = sum_ // 10
        cur.next = ListNode(sum_ % 10)

        return func(cur.next, l1.next if l1 != None else l1, l2.next if l2 != None else l2, carry)

    res = cur = ListNode(0)
    carry = 0
    func(cur, l1, l2, carry)
    return res.next

    # res = cur = ListNode(0)

    # carry = 0
    # while l1 != None or l2 != None or carry!=0:
    #     sum_ = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
    #     carry = sum_//10
    #     cur.next = ListNode(sum_%10)
    #     cur = cur.next
    #     l1 = l1.next if l1 != None else l1
    #     l2 = l2.next if l2 != None else l2
    # return res.next

    # res = cur = ListNode(0)
    # add_ = 0
    # while l1!=None and l2!=None:
    #     sum_ = l1.val+l2.val
    #     if add_ == 0:
    #         cur.next = ListNode(sum_%10)
    #         add_ = sum_//10
    #     else:
    #         cur.next = ListNode((sum_ + add_)%10)
    #         add_ = (sum_ + add_)//10
    #     l1, l2 = l1.next, l2.next
    #     cur = cur.next

    # cur.next = l1 if l1 else l2
    # print(add_)
    # while add_ != 0:
    #     if cur.next==None:
    #         cur.next = ListNode(add_)
    #         add_ = 0
    #     else:
    #         sum_ = cur.next.val + add_
    #         cur.next.val = sum_ % 10
    #         add_ = sum_//10
    #         cur = cur.next

    # return res.next