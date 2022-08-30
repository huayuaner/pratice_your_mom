# 如果一个正整数每一个数位都是 互不相同 的，我们称它是 特殊整数 。
#
# 给你一个 正 整数 n ，请你返回区间 [1, n] 之间特殊整数的数目。
#
#  
#
# 示例 1：
#
# 输入：n = 20
# 输出：19
# 解释：1 到 20 之间所有整数除了 11 以外都是特殊整数。所以总共有 19 个特殊整数。
# 示例 2：
#
# 输入：n = 5
# 输出：5
# 解释：1 到 5 所有整数都是特殊整数。
# 示例 3：
#
# 输入：n = 135
# 输出：110
# 解释：从 1 到 135 总共有 110 个整数是特殊整数。
# 不特殊的部分数字为：22 ，114 和 131 。
import functools
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        n = len(s)
        @functools.lru_cache(None)
        # i 表示当前位数
        # mask表示出现过数字的集合
        # is_Limited表示数字选取是否受到限制 比如 123，第一位选了1第二位选了2，第三位只能在 0-3中选择
        # is_Num表示现在是否是有效数字，比如 123  我遍历出 010，本是合理，会被判断为重复，这时的is_Num会在第二位出现1判断其有效，避免了这种情况的出现
        # 如果使用memo记录，那么只用记录i和mask，并且是在 is_Limited == False and  is_Num的情况下
        # 因为 is_Limited不存在重复计算，is_Num == False 也不存在重复计算
        def f(i:int, mask:int, is_Limited:bool, is_Num:bool)->int:
            # 遍历到末尾了
            if i==n:
                return int(is_Num)
            # ans = 0
            # 如果不是数字
            # 说明当前位数可以不填
            if not is_Num:
                ans = f(i+1, mask, False,is_Num)
            else:
                ans = 0
            # 可以填的数字的上界
            up = int(s[i]) if is_Limited else 9
            # 枚举要填的数字
            # 如果不是数字就从1开始，是数字就可以从0开始
            for d in range(1-int(is_Num), up+1):
                # 如果当前数字没有出现
                # mask作用是当作集合
                if (1<<d)&mask == 0:
                    # 更新mask
                    # 更新is_Limited
                    ans += f(i+1, (1<<d)|mask, is_Limited and d==up, True)
            return ans
        return f(0, 0, True, False)