# 设计一个数字容器系统，可以实现以下功能：
#
# 在系统中给定下标处 插入 或者 替换 一个数字。
# 返回 系统中给定数字的最小下标。
# 请你实现一个 NumberContainers 类：
#
# NumberContainers() 初始化数字容器系统。
# void change(int index, int number) 在下标 index 处填入 number 。如果该下标 index 处已经有数字了，那么用 number 替换该数字。
# int find(int number) 返回给定数字 number 在系统中的最小下标。如果系统中没有 number ，那么返回 -1 。
#  

from sortedcontainers import SortedSet
from collections import defaultdict
import heapq
class NumberContainers:

    def __init__(self):
        # self.index2num = dict()
        # self.num2index = defaultdict(SortedSet)

        self.idx2num = dict()
        self.num2idx = defaultdict(list)


    def change(self, index: int, number: int) -> None:
        # if index in self.index2num:
        #     self.num2index[self.index2num[index]].remove(index)
        # self.index2num[index] = number
        # self.num2index[number].add(index)

        # 懒删除
        self.idx2num[index] = number
        heapq.heappush(self.num2idx[number], index)


    def find(self, number: int) -> int:
        # return self.num2index[number][0] if self.num2index[number] else -1

        heap = self.num2idx[number]
        while heap and self.idx2num[heap[0]] != number:
            heapq.heappop(heap)
        return heap[0] if heap else -1



# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)