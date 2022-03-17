# 请你设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。
#
# 实现 AllOne 类：
#
# AllOne() 初始化数据结构的对象。
# inc(String key) 字符串 key 的计数增加 1 。如果数据结构中尚不存在 key ，那么插入计数为 1 的 key 。
# dec(String key) 字符串 key 的计数减少 1 。如果 key 的计数在减少后为 0 ，那么需要将这个 key 从数据结构中删除。测试用例保证：在减少计数前，key 存在于数据结构中。
# getMaxKey() 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 "" 。
# getMinKey() 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 "" 。
#  
#
# 示例：
#
# 输入
# ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
# [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
# 输出
# [null, null, null, "hello", "hello", null, "hello", "leet"]
#
# 解释
# AllOne allOne = new AllOne();
# allOne.inc("hello");
# allOne.inc("hello");
# allOne.getMaxKey(); // 返回 "hello"
# allOne.getMinKey(); // 返回 "hello"
# allOne.inc("leet");
# allOne.getMaxKey(); // 返回 "hello"
# allOne.getMinKey(); // 返回 "leet"

class DLinkList():
    def __init__(self,key=None,val=0):
        self.val = val
        self.key = key
        self.pre = None
        self.next = None

class AllOne:
    def __init__(self):
        # 哈希 + 大小堆
        # self.cnt = Counter()
        # self.smallheap = []
        # self.bigheap = []

        # 哈希 + 双向链表
        # 存 字符 和 node的映射
        self.HashMap = dict()
        # 设置头尾节点
        self.head = DLinkList(key = 'head', val = float("inf"))
        self.tail = DLinkList(key = 'tail', val = float("-inf"))
        # 将头尾节点连接
        self.head.pre, self.tail.next = self.tail, self.head
        self.head.next, self.tail.pre = self.tail, self.head

    def inc(self, key: str) -> None:
        # 哈希 + 大小堆
        # self.cnt[key] += 1
        # heappush(self.smallheap, (self.cnt[key],key))
        # heappush(self.bigheap, (-self.cnt[key],key))

        # 双向链表+哈希
        if key in self.HashMap:
            node = self.HashMap[key]
            node.val += 1
            #
            prev = node.pre
            # 将node前后点指向node的关系改变成直接node前后点，因为之后要移动node的位置
            prev.next, node.next.pre = node.next, prev
            while prev.val < node.val:
                prev = prev.pre
            # 改变node前点指向node，node指向后点
            prev.next, node.next = node, prev.next
            # 改变node指向前点，node后点指向node
            node.pre, node.next.pre = prev, node
        else:
            node = DLinkList(key, 1)
            self.HashMap[key] = node
            # 插入值双向链表末尾
            node.pre, self.tail.pre = self.tail.pre, node
            node.pre.next, node.next = node, self.tail
            # self.tail.pre.next, node.pre = node, self.tail.pre
            # node.next, self.tail.pre = self.tail, node



    def dec(self, key: str) -> None:
        # 哈希 + 大小堆
        # self.cnt[key] -= 1
        # if self.cnt[key]:
        #     heappush(self.smallheap, (self.cnt[key],key))
        #     heappush(self.bigheap, (-self.cnt[key],key))
        # else:
        #     del self.cnt[key]

        # 双向链表 + 哈希
        node = self.HashMap[key]
        node.val -= 1
        if node.val == 0:
            # 从双向链表和哈希表中删除
            # 只需要把指向node的更改即可
            node.pre.next, node.next.pre = node.next, node.pre
            del self.HashMap[key]
        else:
            nxt = node.next
            node.pre.next, nxt.pre = nxt, node.pre
            while node.val < nxt.val:
                nxt = nxt.next
            nxt.pre, node.pre = node, nxt.pre
            node.pre.next, node.next = node, nxt



    def getMaxKey(self) -> str:
        # 哈希 + 大小堆
        # while self.bigheap:
        #     val, strs = -self.bigheap[0][0], self.bigheap[0][1]
        #     if self.cnt[strs] == val:
        #         return strs
        #     heappop(self.bigheap)
        # return ''

        # 双向链表 + 哈希表
        return self.head.next.key if self.head.next.val!=float("-inf") else ''


    def getMinKey(self) -> str:
        # 哈希 + 大小堆
        # while self.smallheap:
        #     val, strs = self.smallheap[0][0], self.smallheap[0][1]
        #     if self.cnt[strs] == val:
        #         return strs
        #     heappop(self.smallheap)
        # return ''

         # 双向链表 + 哈希表
        return self.tail.pre.key if self.tail.pre.val!=float("inf") else ''




# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()