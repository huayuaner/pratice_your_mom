# 实现一个 MyCalendar 类来存放你的日程安排。如果要添加的时间内不会导致三重预订时，则可以存储这个新的日程安排。
#
# MyCalendar 有一个 book(int start, int end)方法。它意味着在 start 到 end 时间内增加一个日程安排，注意，这里的时间是半开区间，即 [start, end), 实数 x 的范围为，  start <= x < end。
#
# 当三个日程安排有一些时间上的交叉时（例如三个日程安排都在同一时间内），就会产生三重预订。
#
# 每次调用 MyCalendar.book方法时，如果可以将日程安排成功添加到日历中而不会导致三重预订，返回 true。否则，返回 false 并且不要将该日程安排添加到日历中。
#
# 请按照以下步骤调用MyCalendar 类: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
#
MAX_INT = 10 ** 9


class Node:
    def __init__(self) -> None:
        #
        self.l = self.r = None
        # self.lazy = False
        self.lazy = 0
        self.val = 0


class Segmentree:
    def __init__(self) -> None:
        self.root = Node()

    @staticmethod
    def update(node: Node, start: int, end: int, l: int, r: int):
        if start <= l and end >= r:
            node.val += 1
            node.lazy += 1
            return
            # 动态开点
        Segmentree.pushdown(node)
        mid = (l + r) >> 1
        if start <= mid:
            Segmentree.update(node.l, start, end, l, mid)
        if end > mid:
            Segmentree.update(node.r, start, end, mid + 1, r)

        Segmentree.pushup(node)

    @staticmethod
    def query(node: Node, start: int, end: int, l: int, r: int):
        if start <= l and end >= r:
            return not node.val >= 2
        Segmentree.pushdown(node)
        mid = (l + r) >> 1
        ans = True
        if start <= mid:
            ans = ans and Segmentree.query(node.l, start, end, l, mid)
        if end > mid:
            ans = ans and Segmentree.query(node.r, start, end, mid + 1, r)
        return ans

    @staticmethod
    def pushdown(node):
        if not node.l:
            node.l = Node()
        if not node.r:
            node.r = Node()
        if not node.lazy:
            return
        node.r.val += node.lazy
        node.l.val += node.lazy
        node.l.lazy += node.lazy
        node.r.lazy += node.lazy
        node.lazy = 0
        return

    @staticmethod
    def pushup(node):
        node.val = max(node.l.val, node.r.val)


class MyCalendarTwo:

    def __init__(self):
        self.st = Segmentree()

    def book(self, start: int, end: int) -> bool:
        if Segmentree.query(self.st.root, start, end - 1, 0, MAX_INT):
            Segmentree.update(self.st.root, start, end - 1, 0, MAX_INT)
            return True
        return False

    # Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)