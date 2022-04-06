# 一些正数能被表示成一个或者多个连续质数的和。那一个数会有多少种这样的表示方式呢？比如说数字41能有3种表示方式：
# 2+3+5+7+11+13，11+13+17，和41；数字3只有本身这一种表示方式；而20没有这样的表示方式。写一个程序生成给定数字的表示方式数量吧。数字大小范围从2到10，000。

def check(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num%i==0:return False
    return True
def arr_zhi(num):
    ans = []
    for i in range(2, num+1):
        if check(i):
            ans.append(i)
    return ans
def windows(arr,num):
    if not arr:
        return 0
    if len(arr)<2:
        if arr[0]!=num:
            return 0
        else:
            return 1
    ans = 0
    l,r = 0, 1
    n = len(arr)
    tmp = sum(arr[l:r+1])
    while r<n and l<r:
        if tmp < num:
            r += 1
            tmp += arr[r]
        elif tmp>num:
            tmp -= arr[l]
            l += 1
        else:
            ans += 1
            tmp -= arr[l]
            l += 1
            r += 1
            tmp += arr[r]
    ans += (1 if arr[-1] == num else 0)
    return ans
n = int(input())
arr = arr_zhi(n)
print(windows(arr, n))