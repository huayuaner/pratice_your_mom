# 给定一个整数 n 和一个 无重复 黑名单整数数组 blacklist 。设计一种算法，从 [0, n - 1] 范围内的任意整数中选取一个 未加入 黑名单 blacklist 的整数。任何在上述范围内且不在黑名单 blacklist 中的整数都应该有 同等的可能性 被返回。
#
# 优化你的算法，使它最小化调用语言 内置 随机函数的次数。
#
# 实现 Solution 类:
#
# Solution(int n, int[] blacklist) 初始化整数 n 和被加入黑名单 blacklist 的整数
# int pick() 返回一个范围为 [0, n - 1] 且不在黑名单 blacklist 中的随机整数
#  
#
import random
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        # 将 [0,n-m) 的黑名单的数映射到 [n-m,n)中白名单的数
        # 随机选择[0,n-m)中的数，如果是黑名单中的，就转成映射的[n-m,n)的数；如果不在黑名单，返回自己即可
        m = len(blacklist)
        self.boundry = w = n-m
        # 记录[n-m,n)中的黑名单
        black = {val for val in blacklist if val>=w}
        # 将 [0,n-m)的黑名单的数映射到[n-m,0)
        self.b2w = dict()
        for b in blacklist:
            if b<self.boundry:
                while w in black:
                    w += 1
                self.b2w[b] = w
                w += 1




    def pick(self) -> int:
        x = random.randrange(self.boundry)
        return self.b2w.get(x, x)




# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()