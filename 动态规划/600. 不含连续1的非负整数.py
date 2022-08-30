# 给定一个正整数 n ，返回范围在 [0, n] 都非负整数中，其二进制表示不包含 连续的 1 的个数。
#
#  
#
# 示例 1:
#
# 输入: n = 5
# 输出: 5
# 解释:
# 下面是带有相应二进制表示的非负整数<= 5：
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# 其中，只有整数3违反规则（有两个连续的1），其他5个满足规则。
# 示例 2:
#
# 输入: n = 1
# 输出: 2
# 示例 3:
#
# 输入: n = 2
# 输出: 3
class Solution:
    def findIntegers(self, n: int) -> int:
        s = str(bin(n)[2:])
        length = len(s)
        @functools.lru_cache(None)
        def f(i:int, mask:int, is_Limited:bool, is_Num:bool)->int:
            if i == length:
                return 1 # int(is_Num) 0也是数字中的一个
            if not is_Num:
                cnt = f(i+1, mask, False, False)
            else:
                cnt = 0
            up = int(s[i]) if is_Limited else 1
            for d in range(1-int(is_Num), up+1):
                if not d or not mask:
                    cnt += f(i+1, d, is_Limited and d==up, True)
            return cnt
        # 加的这个1 是 0
        return f(0,0,True, False)