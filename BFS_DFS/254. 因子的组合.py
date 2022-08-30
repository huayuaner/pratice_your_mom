# 整数可以被看作是其因子的乘积。
#
# 例如：
#
# 8 = 2 x 2 x 2;
#   = 2 x 4.
# 请实现一个函数，该函数接收一个整数 n 并返回该整数所有的因子组合。
#
# 注意：
#
# 你可以假定 n 为永远为正数。
# 因子必须大于 1 并且小于 n。
class Solution:
    # def __init__(self):
    #     self.ans = []
    def getFactors(self, n: int) -> List[List[int]]:
        def dfs(n,l):
            ans = []
            for i in range(l, int(math.sqrt(n))+1):
                if n%i == 0:
                    ans.append([n//i,i])
                    # 这里使用 n//i,i 作为参数，避免了重复
                    # 比如 -> 12  i == 2 会分成  [6,2], i==3 会分成 [4, 3]
                    # 如果从2 开始  6 和 4 又会分成  [2,3] 和 [2,2]
                    # 发生重复
                    # 换句话说 如果一个 i == 3并且从2开始遍历的例子一定会出现在 i==2之后的例子里 、
                    # 非常巧妙的设计

                    # 因子n//i 能否从i开始被拆分
                    # n//i是一直在变小的，这点不会出现重复
                    for sub in dfs(n//i, i):
                        ans.append(sub+[i])
            return ans
        return dfs(n,2)
