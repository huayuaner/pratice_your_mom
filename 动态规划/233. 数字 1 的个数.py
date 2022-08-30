# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

class Solution:
    def countDigitOne(self, n: int) -> int:
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
                cnt += f(i+1, cnt_1 + (d == 1), is_Limited and d==up, True)
            return cnt

        return f(0,0,True, False)