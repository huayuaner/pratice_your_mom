# 给定循环单调非递减列表中的一个点，写一个函数向这个列表中插入一个新元素 insertVal ，使这个列表仍然是循环升序的。
#
# 给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中最小元素的指针。
#
# 如果有多个满足条件的插入位置，可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。
#
# 如果列表为空（给定的节点是 null），需要创建一个循环有序列表并返回这个节点。否则。请返回原先给定的节点。

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        cur = head
        # 记录最大的node
        max_Node = None
        # 记录小于等于insertVal的最大node
        min_Node = None
        while 1:
            if (not min_Node or min_Node.val <= cur.val) and cur.val <= insertVal:
                min_Node = cur
                # break

            if (not max_Node or max_Node.val < cur.val) and cur.val > insertVal:
                max_Node = cur
            cur = cur.next
            if cur == head:
                break
                # print(min_Node.val, max_Node.val)

        def insert(pre):
            node = Node(insertVal)
            node.next = pre.next
            pre.next = node

        if min_Node:
            insert(min_Node)
        else:
            insert(max_Node)

        return head

