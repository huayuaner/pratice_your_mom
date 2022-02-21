列表 arr 由在范围 [1, n] 中的所有整数组成，并按严格递增排序。请你对 arr 应用下述算法：

从左到右，删除第一个数字，然后每隔一个数字删除一个，直到到达列表末尾。
重复上面的步骤，但这次是从右到左。也就是，删除最右侧的数字，然后剩下的数字每隔一个删除一个。
不断重复这两步，从左到右和从右到左交替进行，直到只剩下一个数字。
给你整数 n ，返回 arr 最后剩下的数字。

 

示例 1：

输入：n = 9
输出：6
解释：
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [2, 4, 6, 8]
arr = [2, 6]
arr = [6]
示例 2：

输入：n = 1
输出：1

class Solution:
    def lastRemaining(self, n: int) -> int:
        # 表示从左向右还是从右向左
        left = True
        # 步长
        step = 1
        # 答案
        head = 1
        while n > 1:
            # 只有从左往右或者从右往左并且n%2==1时head会变
            if left or n%2==1:
                head += step
            left = not left
            step <<= 1
            n >>= 1
        return head