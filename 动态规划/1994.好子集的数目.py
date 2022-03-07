# 给你一个整数数组 nums 。如果 nums 的一个子集中，所有元素的乘积可以表示为一个或多个 互不相同的质数 的乘积，那么我们称它为 好子集 。
#
# 比方说，如果 nums = [1, 2, 3, 4] ：
# [2, 3] ，[1, 2, 3] 和 [1, 3] 是 好 子集，乘积分别为 6 = 2*3 ，6 = 2*3 和 3 = 3 。
# [1, 4] 和 [4] 不是 好 子集，因为乘积分别为 4 = 2*2 和 4 = 2*2 。
# 请你返回 nums 中不同的 好 子集的数目对 109 + 7 取余 的结果。
#
# nums 中的 子集 是通过删除 nums 中一些（可能一个都不删除，也可能全部都删除）元素后剩余元素组成的数组。如果两个子集删除的下标不同，那么它们被视为不同的子集。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,2,3,4]
# 输出：6
# 解释：好子集为：
# - [1,2]：乘积为 2 ，可以表示为质数 2 的乘积。
# - [1,2,3]：乘积为 6 ，可以表示为互不相同的质数 2 和 3 的乘积。
# - [1,3]：乘积为 3 ，可以表示为质数 3 的乘积。
# - [2]：乘积为 2 ，可以表示为质数 2 的乘积。
# - [2,3]：乘积为 6 ，可以表示为互不相同的质数 2 和 3 的乘积。
# - [3]：乘积为 3 ，可以表示为质数 3 的乘积。
# 示例 2：
#
# 输入：nums = [4,2,3,15]
# 输出：5
# 解释：好子集为：
# - [2]：乘积为 2 ，可以表示为质数 2 的乘积。
# - [2,3]：乘积为 6 ，可以表示为互不相同质数 2 和 3 的乘积。
# - [2,15]：乘积为 30 ，可以表示为互不相同质数 2，3 和 5 的乘积。
# - [3]：乘积为 3 ，可以表示为质数 3 的乘积。
# - [15]：乘积为 15 ，可以表示为互不相同质数 3 和 5 的乘积。

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        # 状态压缩动态规划
        # 30以内的所有质数
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        mod = 10 ** 9 + 7

        freq = Counter(nums)
        # 2^10 次方
        f = [0] * (1 << len(primes))
        # 所有的1都有出现不出现两种情况，所以是2^freq
        f[0] = pow(2, freq[1], mod)
        for i, occ in freq.items():

            if i == 1:
                continue

            # 检查 i 的每个质因数是否均不超过 1 个
            subset, x = 0, i
            check = True
            # i一定是1个或多个质数的乘积的结果
            # subset是x包含的质因数
            # 试除法
            for j, prime in enumerate(primes):
                if x % (prime * prime) == 0:
                    # 这个i不能被加入到好子集当中
                    check = False
                    break
                if x % prime == 0:
                    subset |= (1 << j)

            if not check:
                continue
            # 动态规划
            # 从后往前是避免[mask^subset]被改变
            for mask in range((1 << len(primes)) - 1, 0, -1):
                # 当前mask出现了的质因数包含了subset中的质因数
                # 我们需要判断mask中选择了数字i的情况
                # 如i=14 14 = 2 * 7 意味着此时mask表示的集合中有2和7
                # 对应到数学表示就是：A和B的交集是B
                # 代码表示 就是: (a & b)=b
                # 这里的mask&subset == subset
                if (mask & subset) == subset:
                    # 这里使用了滚动数组来减少空间量: f[mask]表示修改前的[mask]位置的值（也就是f[i-1][mask]，i-1代表2:i-1的质因数），还有修改前不包括subset出现的质因数（因为每个质因数只能出现1次）*当前i出现的次数
                    # 当mask == subset的时候，就会用上 f[0]的值，也就是f[0]的次数也参与了计算
                    f[mask] = (f[mask] + f[mask ^ subset] * occ) % mod

        ans = sum(f[1:]) % mod
        return ans
    #dfs
    # PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    # FORBID = [p * p for p in PRIMES[:3]]
    # MOD = int(1e9 + 7)
    # cnts = Counter(nums)
    # # 弹出不合法的值(两个相同质因数的乘积及倍数)
    # for k in list(cnts.keys()):
    #     for f in FORBID:
    #         if not k % f:
    #             cnts.pop(k)
    # # key_primes[k] 为k包含的质因数
    # key_primes = defaultdict(set)
    # for k in cnts:
    #     for p in PRIMES:
    #         if not k % p:
    #             key_primes[k].add(p)
    #         elif k < p:
    #             break
    # # 记录 1的次数，同上一个方法
    # ones = pow(2, cnts[1], MOD)
    #
    # @lru_cache(None)
    # # ps存放已经遍历过的质因数
    # def dfs(idx, ps):
    #     # base case 遍历完成或质因数已经被选完了
    #     if idx > 30 or len(ps) == len(PRIMES):
    #         # 不可能所有质数都没被选的空集
    #         return (len(ps) > 0) * ones
    #     st, ans = set(ps), 0
    #     # idx存在在原数组中且质因子尚未被选
    #     if idx in cnts and not key_primes[idx] & st:
    #         # ans +选择了当前质因数的出现次数*之后遍历次数
    #         ans += cnts[idx] % MOD * dfs(idx + 1, tuple(st | key_primes[idx])) % MOD
    #     # 叠加不选idx的答案数
    #     return (ans + dfs(idx + 1, ps)) % MOD
    #
    # return dfs(2, tuple())

