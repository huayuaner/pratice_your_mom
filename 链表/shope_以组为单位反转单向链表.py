# 给一个单向链表以及整数N，使得每N个元素为一组进行翻转。要求时间复杂度O(n), 空间复杂度O(1)。

# class ListNode:


# def __init__(self, x):
#         self.val = x
#         self.next = None

#
# reverse the given linked list
# @param head ListNode类 the head of the linked list
# @param n int整型 the N
# @return ListNode类
#
class Solution:
    def reverseLinkedList(self, head, n):
        # write code here
        # 反转使用两个参数头和尾
        def reverse(head, tail):
            # prev的初始化需注意
            prev = tail.next
            cur = head
            # 判定条件也有变化
            # 从cur -> prev!=tail 所表达的意思都是遍历到末尾
            while prev != tail:
                nex_node = cur.next
                cur.next = prev
                prev = cur
                cur = nex_node
            # 新头和新尾
            return tail, head
        # 哑节点
        dum = ListNode(-1)
        dum.next = head
        pre = dum
        while head:
            # 总共三个参 pre head tail
            # 我觉得两个即可 因为head就是pre.next
            # 确定尾节点的位置,从pre开始
            tail = pre
            # 使用tmp存上一个tail，当遍历至空可返回暂存值
            for _ in range(n):
                tmp = tail
                tail = tail.next
                # 遍历到末尾了
                if not tail:
                    tail = tmp
                    break
            # 头变成新头，尾变新尾
            head, tail = reverse(head, tail)
            # 接一下pre和head的关系
            pre.next = head
            # 更新头
            head = tail.next
            # 更新pre
            pre = tail
        return dum.next