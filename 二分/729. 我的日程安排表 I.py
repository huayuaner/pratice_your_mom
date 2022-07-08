# 实现一个 MyCalendar 类来存放你的日程安排。如果要添加的日程安排不会造成 重复预订 ，则可以存储这个新的日程安排。
#
# 当两个日程安排有一些时间上的交叉时（例如两个日程安排都在同一时间内），就会产生 重复预订 。
#
# 日程可以用一对整数 start 和 end 表示，这里的时间是半开区间，即 [start, end), 实数 x 的范围为，  start <= x < end 。
#
# 实现 MyCalendar 类：
#
# MyCalendar() 初始化日历对象。
# boolean book(int start, int end) 如果可以将日程安排成功添加到日历中而不会导致重复预订，返回 true 。否则，返回 false 并且不要将该日程安排添加到日历中。

MAX_INT = 10 ** 9
from sortedcontainers import SortedDict


class MyCalendar:

    def __init__(self):
        # self.st = SegmentTree()

        # 暴力
        # self.block = []

        # 有序字典
        # self.block = SortedDict()

        # 方法3
        # 将start和end都放在一个list中，那么start一定在偶数位置，而end在奇数的位置
        self.slot = []

    def book(self, start: int, end: int) -> bool:
        # print(SegmentTree.query(self.st.root, start, end ,0,MAX_INT))
        # if SegmentTree.query(self.st.root, start, end-1 ,0,MAX_INT):
        #     return False
        # else:
        #     SegmentTree.update(self.st.root, start, end-1, 0, MAX_INT, 1)
        #     return True

        # 暴力
        # if any(l < end and start < r for l,r in self.block):
        #     return False
        # self.block.append([start, end])
        # return True

        # 有序字典
        # 插入end的位置
        # i = self.block.bisect_left(end)
        # if i == 0 or (self.block.items()[i-1][1] <= start):
        #     self.block[start] = end
        #     return True
        # return False

        i = bisect.bisect_right(self.slot, start)
        # 当start是的位置是奇数说明不合法
        # 当start插入的是偶数位置，但结束时间超过了下一个start开始的时间也不合法
        if i & 1 or (i < len(self.slot) and self.slot[i] < end):
            return False
            # 这句话是在i位置插入列表，而不是一个数
        self.slot[i:i] = [start, end]
        # print(self.slot)
        return True

    # Your MyCalendar object will be instantiated and called as such:


# obj = MyCalendar()
# param_1 = obj.book(start,end)
class Node:
    def __init__(self) -> None:
        # 左右孩子为空
        self.l = self.r = None
        # 由于题目原因不需要求和
        # 只需要知道该区间的是否被包含了 用val存，lazy是懒标记
        self.val = self.lazy = False


class SegmentTree:
    def __init__(self) -> None:
        self.root = Node()

    @staticmethod
    def update(node: Node, start: int, end: int, l: int, r: int, val: bool) -> None:
        # start end代表目标区间的左右指针
        # l r 代表当前区间的左右指针
        # 直接对该节点进行更新，并且更新懒标记，这里懒标记是记录孩子是否存在变化
        if start <= l and r <= end:
            node.val = val
            node.lazy = True
            return
        # 如果当前的l-r并未被start-end包含，换句话说，就是要往下搜了
        # 如果要往下搜，那么就要进行动态开点和懒标记传递了
        # 先往下更新一手
        SegmentTree.pushdown(node)
        mid = (l + r) >> 1
        if start <= mid:
            # 往左更新
            SegmentTree.update(node.l, start, end, l, mid, val)
        if end > mid:
            # 往右更新
            SegmentTree.update(node.r, start, end, mid + 1, r, val)
        # 进行pushup，也就是说这时候懒标记只会出现在当前的叶子节点上
        # 在递归的同时往上更新，防止query出错
        SegmentTree.pushup(node)

    @staticmethod
    # 查询的道理和update相同
    def query(node: Node, start: int, end: int, l: int, r: int) -> bool:
        # 如果目标区间包含该区间
        # 直接返回该node是否是被包含的
        if start <= l and r <= end:
            return node.val
        # 把懒标记沉下去
        # 也就是更新被增加/删除的node的子节点
        # 只有查询的时候才进行更新
        SegmentTree.pushdown(node)
        mid, ans = (l + r) >> 1, False
        # ans只有在左右子树都是被包含的情况下才算是被包含
        if start <= mid:
            ans = ans or SegmentTree.query(node.l, start, end, l, mid)
        if end > mid:
            ans = ans or SegmentTree.query(node.r, start, end, mid + 1, r)
        # print(ans)
        return ans

    @staticmethod
    def pushdown(node: Node) -> None:
        # 将懒标记下沉，只有在查询和更新的时候才进行
        # 动态开点：只有下沉才孩子节点
        if not node.l:
            node.l = Node()
        if not node.r:
            node.r = Node()
        # 没有懒标记，不需要下沉
        if not node.lazy:
            return
        # 其左右孩子 是否被包含取决于其父亲节点是否被包含
        # 当父亲被包含，其左右子区间必被包含
        # 当父亲没有被包含，其左右子区间必没有被包含
        node.l.val = node.r.val = node.val
        node.l.lazy = node.r.lazy = True
        # 清除当前节点的lazy，他已经往下传递了
        node.lazy = False

    @staticmethod
    def pushup(node: Node) -> None:
        # 当前区间是否被包含同样取决于左右孩子是否都被包含
        node.val = node.l.val or node.r.val