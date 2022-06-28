# 给你两个整数 num 和 k ，考虑具有以下属性的正整数多重集：
#
# 每个整数个位数字都是 k 。
# 所有整数之和是 num 。
# 返回该多重集的最小大小，如果不存在这样的多重集，返回 -1 。
#
# 注意：
#
# 多重集与集合类似，但多重集可以包含多个同一整数，空多重集的和为 0 。
# 个位数字 是数字最右边的数位。
#  
#
# 示例 1：
#
# 输入：num = 58, k = 9
# 输出：2
# 解释：
# 多重集 [9,49] 满足题目条件，和为 58 且每个整数的个位数字是 9 。
# 另一个满足条件的多重集是 [19,39] 。
# 可以证明 2 是满足题目条件的多重集的最小长度。
# 示例 2：
#
# 输入：num = 37, k = 2
# 输出：-1
# 解释：个位数字为 2 的整数无法相加得到 37 。
# 示例 3：
#
# 输入：num = 0, k = 7
# 输出：0
# 解释：空多重集的和为 0 。
#
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        """
        观察1：答案最小是1，最大是num
        观察2：如何知道该答案合法
        数学推导：
        组成num的每一个元素x可以看成 x = n*10 + k
        有n个元素 得到  10*(n_1+n_2+...+n_n) + n*k = num
        就有 (num - n*k)%10 == 0
        上述式子说明 num 和 n*k 对10同余
        再有 n = 11 和 n = 1 的时候 有  11*k%10 = 1*k%10
        所以只用遍历到10即可
        """
        if num == 0:
            return 0
        for i in range(1, 11):

            # print(num)
            if num - i * k < 0: break
            if (num - i * k) % 10 == 0:
                return i
        return -1