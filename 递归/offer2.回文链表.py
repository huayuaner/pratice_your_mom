# 给定一个链表的
# 头节点
# head ，请判断其是否为回文链表。
#
# 如果一个链表是回文，那么链表节点序列从前往后看和从后往前看是相同的。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
# if head.next==None:
#     return True
# res1= []
# res1.append(head.val)
# while(head.next!=None):
#     head = head.next
#     res1.append(head.val)
# start, end = 0, len(res1)-1

# while start<end:

#     if res1[start] != res1[end]:
#         return False
#     start += 1
#     end -= 1
# return True

# 递归

# self.front = head

# def func(current=head):
#     if current != None:
#         if not func(current.next):
#             return False
#         if self.front.val != current.val:
#             return False
#         self.front = self.front.next
#     return True

# return func()


# 快慢指针(时间n空间1)
# def find_first_end(self, head):
#     slow, fast = head, head
#     while fast.next is not None and fast.next.next is not None:
#         slow = slow.next
#         fast = fast.next.next
#     return slow
# def reverse(self, head):
#     pre=None
#     cur=head
#     while cur is not None:
#         nex_node = cur.next
#         cur.next = pre
#         pre = cur
#         cur = nex_node
#     return pre
# if head is None :
#   return True
# first_end = find_first_end(self, head)
# second_start = reverse(self, first_end.next)


# first_position = head
# second_position = second_start

# while  (second_position is not None):
#     if first_position.val != second_position.val:
#         return False
#     first_position = first_position.next
#     second_position = second_position.next
# return True




