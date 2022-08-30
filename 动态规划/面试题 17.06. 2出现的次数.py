# 编写一个方法，计算从 0 到 n (含 n) 中数字 2 出现的次数。
#
# 示例:
#
# 输入: 25
# 输出: 9
# 解释: (2, 12, 20, 21, 22, 23, 24, 25)(注意 22 应该算作两次)
#
class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        s = str(n)
        length = len(s)
        @functools.lru_cache(None)
        def f(i:int, cnt_1:int, is_Limited:bool, is_Num:bool)->int:
            if i == length:
                return cnt_1
            if not is_Num:
                cnt = f(i+1, cnt_1, False, False)
            else:
                cnt = 0
            up = int(s[i]) if is_Limited else 9
            for d in range(1-int(is_Num), up+1):
                # if mask & (1<<d) == 0:
                cnt += f(i+1, cnt_1 + (d == 2), is_Limited and d==up, True)
            return cnt

        return f(0,0,True, False)