# 多级双向链表中，除了指向下一个节点和前一个节点指针之外，它还有一个子链表指针，可能指向单独的双向链表。这些子列表也可能会有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。
#
# 给定位于列表第一级的头节点，请扁平化列表，即将这样的多级双向链表展平成普通的双向链表，使所有结点出现在单级双链表中。

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return
        cur = head
        while cur:
            if not cur.child:
                cur = cur.next
            else:
                nex_node = cur.next
                child = self.flatten(cur.child)
                # 找child的尾节点
                tail = child
                while tail.next:
                    tail = tail.next
                # 将child的内容放在cur和nex中间
                cur.next = cur.child
                cur.child.prev = cur
                if nex_node:
                    tail.next = nex_node
                    nex_node.prev = tail
                # cur 更新至nex的位置
                # 这句忘记写了
                cur.child = None
                cur = nex_node
        # print(head)
        return head
