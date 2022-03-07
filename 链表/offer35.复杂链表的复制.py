# 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 哈希表 2次遍历
        # if not head:
        #     return
        # HashMap = dict()
        # cur = head
        # # 建立原链表节点和新链表节点的映射
        # while cur:
        #     HashMap[cur] = Node(cur.val)
        #     cur = cur.next
        # cur = head
        # while cur:
        #     # 构建新链表的关系
        #     HashMap[cur].next = HashMap.get(cur.next)# 从哈希表get到的value是新建的node
        #     HashMap[cur].random = HashMap.get(cur.random)
        #     cur = cur.next
        # return HashMap[head]

        # 拼接+拆分 3次遍历
        if not head:
            return
        cur = head
        # 复制各个点拼接在原链表之后
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = cur.next.next
        # 2.构建各个新节点的random指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 拆分两个链表
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        # 处理原链表尾节点
        pre.next = None
        return res

