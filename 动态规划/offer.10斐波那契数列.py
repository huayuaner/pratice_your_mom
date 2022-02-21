# 输入写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：
#
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
# 斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
#
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
#
#  
#
# 示例 1：
#
# 输入：n = 2
# 输出：1
# 示例 2：
#
# 输入：n = 5
# 输出：5

# @functools.lru_cache(None)
        # def Fibonacci(n):
        #     if n == 0:
        #         return 0
        #     if n== 1:
        #         return 1
        #     return (Fibonacci(n-1)+Fibonacci(n-2))%(pow(10,9)+7)
        # return Fibonacci(n)%(pow(10,9)+7)

        #上一个fibo的优化，每次返回当前的值与上一次的值
        # def good_fibo(n):
        #     if n<=1:
        #         return (n,0)
        #     else:
        #         a, b = good_fibo(n-1)
        #     return (a+b, a)
        # return good_fibo(n)[0]%(pow(10,9)+7)

        # 动态规划
        # a, b = 0, 1
        # for _ in range(n):
        #     a, b = b, a + b
        # return a % 1000000007

