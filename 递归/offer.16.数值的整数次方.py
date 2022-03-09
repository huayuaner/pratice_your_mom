#实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。

if n == 0:
    return 1
if n < 0:
    n = -n
    x = 1 / x
res = self.myPow(x, n // 2)
res = res ** 2
if n % 2 != 0:
    res = res * x
return res

# 结构更好的，因为直接return了，不存在溢出
# if n == 0:
#     return 1
# elif n < 0:
#     return 1/self.myPow(x, -n)
# elif n & 1:
#     return x * self.myPow(x, n - 1)
# else:
#     return self.myPow(x*x, n // 2)
