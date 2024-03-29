# 有 N 种物品和一个容量是 V 的背包。
#
# 第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。
#
# 求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
# 输出最大价值。
#
# 输入格式
# 第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。
#
# 接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的体积、价值和数量。
#
# 输出格式
# 输出一个整数，表示最大价值。
#
# 数据范围
# 0<N≤1000
# 0<V≤2000
# 0<vi,wi,si≤2000

'''
多重背包问题 -> 0 1 背包问题
把s份拆成一个一个，就变成了01背包问题有重复物品

但是对于这个数据量会超时


使用二进制的方法求解
具体方法为：
假如这个物品可以选10次，那么就可以打包成 选1次 2^0， 选2次 2^1，选4次 2^2，选3次 （10 - 2^0 - 2^1 - 2^2）
这样 1-10都可以被表示 ，1就是选一次，2选两次... 5是选两次加三次，6是1+2+3，7是1+2+4 ,8是1+3+4，9是2+3+4，10是1+2+3+4
这样从这样就变成了把s份拆成一个个 -> 把s份拆成 log s 份
再对这log s 份进行01背包即可

'''

n, vols = map(int, input().split())

dp = [0] * (vols + 1)
for _ in range(n):
    tmp = []
    v, w, cnt = map(int, input().split())
    k = 1
    while k <= cnt:
        cnt -= k
        tmp.append([v * k, w * k])
        k *= 2

    if cnt > 0:
        tmp.append([v * cnt, w * cnt])
    # print(tmp)
    for t in tmp:
        for j in range(vols, t[0] - 1, -1):
            dp[j] = max(dp[j], dp[j - t[0]] + t[1])
    # print(dp)
print(dp[-1])

