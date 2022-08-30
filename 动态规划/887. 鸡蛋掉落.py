# 给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。
#
# 已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。
#
# 每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <= n）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。
#
# 请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？
#
#  
# 示例 1：
#
# 输入：k = 1, n = 2
# 输出：2
# 解释：
# 鸡蛋从 1 楼掉落。如果它碎了，肯定能得出 f = 0 。
# 否则，鸡蛋从 2 楼掉落。如果它碎了，肯定能得出 f = 1 。
# 如果它没碎，那么肯定能得出 f = 2 。
# 因此，在最坏的情况下我们需要移动 2 次以确定 f 是多少。
# 示例 2：
#
# 输入：k = 2, n = 6
# 输出：3
# 示例 3：
#
# 输入：k = 3, n = 14
# 输出：4
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[float('inf') for _ in range(n + 1)] for _ in range(k)]
        # 0层楼的时候只用0次操作
        # dp[i][j]表示i+1个鸡蛋和j层楼
        # 当 0 层楼 ,几个鸡蛋都是0
        # 当1层楼，几个鸡蛋都是1
        # for i in range(k):
        #     dp[i][0] = 0
        #     dp[i][1] = 1
        # # 当 1 个鸡蛋，几层楼都是j
        # for j in range(n+1):
        #     dp[0][j] = j

        # # 当有两个鸡蛋且有j层楼
        # # 第一选择从第k层楼丢下 碎：dp[0][k-1] + 1  没碎: dp[1][j-k]+1 取两者小值
        # for i in range(1,k):
        #     for j in range(1,n+1):
        #         # 使用x遍历 1-j的情况
        #         # 可以简单得到 dp[i - 1][left-1]会随着x增大而增大（非递减）， 而dp[i][j-left])会随着x增大而减小（非递增） -> 满足二分条件
        #         # 我们要找的是两条函数较大值的最小值，也就是两条函数的交点处
        #         # 使用二分
        #         left,right = 1, j
        #         while left<right:

        #             mid = left + (right-left)//2
        #             if dp[i-1][mid-1] < dp[i][j-mid]:
        #                 left = mid + 1
        #             else:
        #                 right = mid
        #         dp[i][j] = max(dp[i - 1][left-1], dp[i][j-left]) + 1
        # return dp[-1][-1]

        # 新思路动态规划
        # dp[i][j] 表示 i个鸡蛋 丢j次 最多能检测几层楼
        dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
        # 一个鸡蛋丢一次最多1层楼
        # for j in range(n+1):
        #     dp[0][j] = j
        dp[1][1] = 1
        for i in range(1, k + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1] + 1
                if i == k and dp[i][j] >= n:
                    # print(dp)
                    return j
        # return n