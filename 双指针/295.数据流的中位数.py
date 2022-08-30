# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
#
# 例如，
#
# [2,3,4] 的中位数是 3
#
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
#
# 设计一个支持以下两种操作的数据结构：
#
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。
# 示例：
#
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2
# 进阶:
#
# 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
# 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
# import bisect
class MedianFinder:

    def __init__(self):

    # self.order = []

    # self.Max = []
    # self.Min = []

    def addNum(self, num: int) -> None:

    # bisect.insort(self.order, num)

    # if not self.Min or -self.Min[0]>num:
    #     heappush(self.Min, -num)
    #     if len(self.Min) - 1 >len(self.Max):
    #         heappush(self.Max, -heappop(self.Min))
    # else:
    #     heappush(self.Max, num)
    #     if len(self.Min) < len(self.Max):
    #         heappush(self.Min, -heappop(self.Max))

    def findMedian(self) -> float:
# n = len(self.order)
# if n == 0: return None
# if n % 2 == 0:
#     mid1, mid2 = n//2-1, n//2
#     return (self.order[mid1]+self.order[mid2])/2
# else:
#     return self.order[n//2]

# if len(self.Max)!= len(self.Min):
#     return -self.Min[0]
# else:
#     return (-self.Min[0]+self.Max[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()