# Range模块是跟踪数字范围的模块。设计一个数据结构来跟踪表示为 半开区间 的范围并查询它们。
#
# 半开区间 [left, right) 表示所有 left <= x < right 的实数 x 。
#
# 实现 RangeModule 类:
#
# RangeModule() 初始化数据结构的对象。
# void addRange(int left, int right) 添加 半开区间 [left, right)，跟踪该区间中的每个实数。添加与当前跟踪的数字部分重叠的区间时，应当添加在区间 [left, right) 中尚未跟踪的任何数字到该区间中。
# boolean queryRange(int left, int right) 只有在当前正在跟踪区间 [left, right) 中的每一个实数时，才返回 true ，否则返回 false 。
# void removeRange(int left, int right) 停止跟踪 半开区间 [left, right) 中当前正在跟踪的每个实数。
MAX_RANGE = int(1e9+7)
class RangeModule:

    def __init__(self):
        self.st = SegmentTree()

    def addRange(self, left: int, right: int) -> None:
        SegmentTree.update(self.st.root, left, right-1, 1, MAX_RANGE, True)


    def queryRange(self, left: int, right: int) -> bool:
        return SegmentTree.query(self.st.root, left, right-1, 1, MAX_RANGE)


    def removeRange(self, left: int, right: int) -> None:
        SegmentTree.update(self.st.root, left, right-1, 1, MAX_RANGE, False)

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
    def update(node:Node, start:int, end:int, l:int, r:int, val:bool) -> None:
        # start end代表目标区间的左右指针
        # l r 代表当前区间的左右指针
        # 直接对该节点进行更新，并且更新懒标记，这里懒标记是记录孩子是否存在变化
        if start<=l and r<=end:
            node.val = val
            node.lazy = True
            return
        # 如果当前的l-r并未被start-end包含，换句话说，就是要往下搜了
        # 如果要往下搜，那么就要进行动态开点和懒标记传递了
        # 先往下更新一手
        SegmentTree.pushdown(node)
        mid = (l+r)>>1
        if start <= mid:
            # 往左更新
            SegmentTree.update(node.l, start, end,l, mid,val)
        if end > mid:
            # 往右更新
            SegmentTree.update(node.r, start, end, mid+1, r,val)
        # 进行pushup，也就是说这时候懒标记只会出现在当前的叶子节点上
        # 在递归的同时往上更新，防止query出错
        SegmentTree.pushup(node)
    @staticmethod
    # 查询的道理和update相同
    def query(node:Node, start:int, end:int, l:int, r:int) -> bool:
        # 如果目标区间包含该区间
        # 直接返回该node是否是被包含的
        if start<=l and r<=end:
            return node.val
        # 把懒标记沉下去
        # 也就是更新被增加/删除的node的子节点
        # 只有查询的时候才进行更新
        SegmentTree.pushdown(node)
        mid, ans = (l+r)>>1, True
        # ans只有在左右子树都是被包含的情况下才算是被包含
        if start <= mid:
            ans = ans and SegmentTree.query(node.l, start, end, l, mid)
        if end > mid:
            ans = ans and SegmentTree.query(node.r, start, end, mid+1, r)
        # print(ans)
        return ans
    @staticmethod
    def pushdown(node:Node)->None:
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
    def pushup(node:Node)->None:
        # 当前区间是否被包含同样取决于左右孩子是否都被包含
        node.val = node.l.val and node.r.val




# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)