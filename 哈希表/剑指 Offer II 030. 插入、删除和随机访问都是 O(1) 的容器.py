# 设计一个支持在平均 时间复杂度
# O(1) 下，执行以下操作的数据结构：
#
# insert(val)：当元素
# val
# 不存在时返回
# true ，并向集合中插入该项，否则返回
# false 。
# remove(val)：当元素
# val
# 存在时返回
# true ，并从集合中移除该项，否则返回
# false 。
# getRandom：随机返回现有集合中的一项。每个元素应该有 相同的概率 被返回。
#  

import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.hash = set()
        # self.length = 0
        self.dic = dict()
        self.nums = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        # if val not in self.hash:
        #     self.hash.add(val)
        #     # self.length += 1
        #     return True
        # return False
        if val in self.dic:
            return False
        self.nums.append(val)
        self.dic[val] = len(self.nums)
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # if val in self.hash:
        #     self.hash.remove(val)
        #     # self.length -= 1
        #     return True
        # return False
        if val not in self.dic:
            return False
        idx = self.dic[val]
        self.nums[idx-1] = self.nums[-1]
        self.dic[self.nums[idx-1]] = idx
        self.nums.pop()
        del self.dic[val]
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # res = None
        # for i,num in enumerate(self.hash):
        #     if random.uniform(0,i+1) <= 1:
        #         res = num
        # return res
        return choice(self.nums)




# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()