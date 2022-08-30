# 给定一个在 0 到 9 之间的整数 d，和两个正整数 low 和 high 分别作为上下界。返回 d 在 low 和 high 之间的整数中出现的次数，包括边界 low 和 high。
#
#  
#
# 示例 1：
#
# 输入：d = 1, low = 1, high = 13
# 输出：6
# 解释：
# 数字 d=1 在 1,10,11,12,13 中出现 6 次。注意 d=1 在数字 11 中出现两次。
# 示例 2：
#
# 输入：d = 3, low = 100, high = 250
# 输出：35
# 解释：
# 数字 d=3 在 103,113,123,130,131,...,238,239,243 出现 35 次。
class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        def helper(high):
            s = str(high)
            length = len(s)
            @functools.lru_cache(None)
            def f(i:int, cnt_d:int, is_Limited:bool, is_Num:bool)->int:
                if i == length:
                    return cnt_d# int(is_Num)
                if not is_Num:
                    cnt = f(i+1, cnt_d, False, False)
                else:
                    cnt = 0
                up = int(s[i]) if is_Limited else 9
                for digit in range(1-int(is_Num), up+1):
                    # if mask & (1<<d) == 0:
                    cnt += f(i+1, cnt_d+(digit==d), is_Limited and digit==up, True)
                return cnt
            return f(0,0,True, False)

        return helper(high) - helper(low-1)# f(0,0,True, False)