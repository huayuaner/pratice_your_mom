# 小强今天体检，其中有一个环节是测视力
# 小强看到的视力表是一张N*N的表格，但是由于小强视力太差，他无法看清表格中的符号。
# 不过热爱数学的他给自己出了这样一个问题：假设现在有a个向上的符号，b个向下的符号，c个向左的符号，d个向右的符号，
# 把这些符号填到视力表中，总共有多少种可能的情况呢？

from math import factorial

n, a, b, c, d = map(int, input().split())
print(factorial(n * n) // factorial(a) // factorial(b) // factorial(c) // factorial(d) % 998244353)
