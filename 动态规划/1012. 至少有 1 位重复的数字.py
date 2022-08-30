# 给定正整数 n，返回在 [1, n] 范围内具有 至少 1 位 重复数字的正整数的个数。
#
#  
#
# 示例 1：
#
# 输入：n = 20
# 输出：1
# 解释：具有至少 1 位重复数字的正数（<= 20）只有 11 。
# 示例 2：
#
# 输入：n = 100
# 输出：10
# 解释：具有至少 1 位重复数字的正数（<= 100）有 11，22，33，44，55，66，77，88，99 和 100 。
# 示例 3：
#
# 输入：n = 1000
# 输出：262
import functools
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)
        length = len(s)
        @functools.lru_cache(None)
        def f(i:int, mask:int, is_Limited:bool, is_Num:bool)->int:
            if i == length:
                return int(is_Num)
            if not is_Num:
                cnt = f(i+1, mask, False, False)
            else:
                cnt = 0
            up = int(s[i]) if is_Limited else 9
            for d in range(1-int(is_Num), up+1):
                if mask & (1<<d) == 0:
                    cnt += f(i+1, mask|(1<<d), is_Limited and d==up, True)
            return cnt

        return n-f(0,0,True, False)