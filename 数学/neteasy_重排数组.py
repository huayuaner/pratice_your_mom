# 5
# 小易有一个长度为N的正整数数列A = {A[1], A[2], A[3]..., A[N]}。
# 牛博士给小易出了一个难题:
# 对数列A进行重新排列,使数列A满足所有的A[i] * A[i + 1](1 ≤ i ≤ N - 1)都是4的倍数。
# 小易现在需要判断一个数列是否可以重排之后满足牛博士的要求。

# 思路
# 记录4的倍数，2的倍数，1的倍数的个数
# n个4的倍数的数字可以处理 n+1个非4倍数的数字
# 2的倍数可以内部消化偶数个
# 1的倍数只能和4搭配
# 所以只要4的倍数 + 1 大于等于 （1的倍数 + 2的倍数%2即可）
from collections import Counter
n = int(input())
for _ in range(n):
    lens = int(input())
    nums = list(map(int, input().split()))
    dic = Counter()
    for num in nums:
        if num%4==0:
            dic[4] += 1
        elif num%2 == 0:
            dic[2] += 1
        else:
            dic[0] += 1
    if dic[2]%2+dic[0] > dic[4]+1:
        print('No')
    else:
        print('Yes')
