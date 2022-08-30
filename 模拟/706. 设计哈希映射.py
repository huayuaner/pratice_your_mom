# 不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
#
# 实现 MyHashMap 类：
#
# MyHashMap() 用空映射初始化对象
# void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
# int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
# void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。
class MyHashMap:

    def __init__(self):
        # 最简单
        # self.arr = [-1]*(10**6 + 1)

        # 分桶
        # self.map = [[-1]*1000 for _ in range(1001)]

        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def put(self, key: int, value: int) -> None:
        # self.arr[key] = value

        # row, col = key//1000, key%1000
        # self.map[row][col] = value

        hashkey = self.hash(key)
        for item in self.table[hashkey]:
            if item[0] == key:
                item[1] = value
                break
        else:
            self.table[hashkey].append([key, value])

    def get(self, key: int) -> int:
        hashkey = self.hash(key)
        for item in self.table[hashkey]:
            if item[0] == key:
                return item[1]
        return -1
        # return self.arr[key]
        # row, col = key//1000, key%1000
        # return self.map[row][col]

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        for i, item in enumerate(self.table[hashkey]):
            if item[0] == key:
                # print(self.table[hashkey])
                self.table[hashkey].pop(i)
                # print(self.table[hashkey])
                return
                # row, col = key//1000, key%1000
        # self.map[row][col] = -1
        # self.arr[key] = -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)