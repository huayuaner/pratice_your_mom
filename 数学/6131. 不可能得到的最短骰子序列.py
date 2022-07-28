# 给你一个长度为 n 的整数数组 rolls 和一个整数 k 。你扔一个 k 面的骰子 n 次，骰子的每个面分别是 1 到 k ，其中第 i 次扔得到的数字是 rolls[i] 。
#
# 请你返回 无法 从 rolls 中得到的 最短 骰子子序列的长度。
#
# 扔一个 k 面的骰子 len 次得到的是一个长度为 len 的 骰子子序列 。
#
# 注意 ，子序列只需要保持在原数组中的顺序，不需要连续。
#
class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        ans = 1
        mark = [0]*(k+1)
        rest = k
        for roll in rolls:
            if mark[roll]<ans:
                mark[roll] = ans
                rest -= 1
                if rest == 0:
                    ans += 1
                    rest = k
        return ans