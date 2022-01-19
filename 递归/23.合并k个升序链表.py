# 给你一个链表数组，每个链表都已经按升序排列。
#
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
#
#  
#
# 示例 1：
#
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
# 示例 2：
#
# 输入：lists = []
# 输出：[]
# 示例 3：
#
# 输入：lists = [[]]
# 输出：[]
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    # def process(lists, L, R):#log N
    #     if L == R:
    #         return lists[L]
    #     if L > R :
    #         return
    #     mid = L + (R-L)//2
    #     return merge(process(lists,L, mid), process(lists, mid+1, R))
    # def merge(l1, l2): # n
    #     dum = cur = ListNode(0)
    #     while l1 and l2:
    #         if l1.val <= l2.val:
    #             cur.next = ListNode(l1.val)
    #             l1 = l1.next

    #         else:
    #             cur.next = ListNode(l2.val)
    #             l2 = l2.next
    #         cur = cur.next
    #     cur.next = l1 if l1 else l2
    #     #print(dum.next)
    #     return dum.next

    # #self.ans = ListNode(float("-inf"))

    # return process(lists, 0, len(lists)-1)

    # 堆合并
    pq = []
    for i, ls in enumerate(lists):
      # 将.val,i元组以小根堆方式放入pq
      if ls:  # 避免空值
        heappush(pq, (ls.val, i))
    dum = cur = ListNode(0)
    while pq:  # N
      min_node, index = heappop(pq)
      cur.next = ListNode(min_node)
      cur = cur.next
      if lists[index].next:  # 避免空值
        heappush(pq, (lists[index].next.val, index))  # log N
        lists[index] = lists[index].next
    return dum.next

