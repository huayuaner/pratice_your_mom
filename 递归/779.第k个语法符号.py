# 在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。
#
# 给定行数 N 和序数 K，返回第 N 行中第 K个字符。（K从1开始）
#
# 输入: N = 1, K = 1
# 输出: 0
#
# 输入: N = 2, K = 1
# 输出: 0
#
# 输入: N = 2, K = 2
# 输出: 1
#
# 输入: N = 4, K = 5
# 输出: 1
#
# 解释:
# 第一行: 0
# 第二行: 01
# 第三行: 0110
# 第四行: 01101001

def kthGrammar(self, n: int, k: int) -> int:
    if n == 1:
        return 0
    else:
        if k <= 2 ** (n - 2):
            return self.kthGrammar(n - 1, k)
        else:
            return self.kthGrammar(n - 1, k - 2 ** (n - 2)) ^ 1