# 有 N 种物品和一个容量是 V 的背包。
#
# 第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。
#
# 求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
# 输出最大价值。
#
# 输入格式
# 第一行两个整数，N，V (0<N≤1000, 0<V≤20000)，用空格隔开，分别表示物品种数和背包容积。
#
# 接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的体积、价值和数量。
#
# 输出格式
# 输出一个整数，表示最大价值。
#
# 数据范围
# 0<N≤1000
# 0<V≤20000
# 0<vi,wi,si≤20000


from collections import deque

n, vols = map(int, input().split())
dp = [0] * (vols + 1)
for _ in range(n):
    v, w, s = map(int, input().split())
    # 余数为c的类
    for c in range(v):
        pq = deque()
        times = (vols - c) // v
        # 余数为c能放times个
        for k in range(times + 1):
            cur = dp[k * v + c] - k * w
            # 单调队列队头已经不合法了
            # 弹出
            if pq and pq[0][0] == k - s - 1:
                pq.popleft()
            # 弹出单调队列中小于cur的
            while pq and pq[-1][1] < cur:
                pq.pop()
            # 存入标号+当前值的组合
            pq.append([k, cur])
            # 更新dp
            dp[k * v + c] = pq[0][1] + k * w
            # print(dp,k)
        # queue = []
        # hh, tt = 0, -1
        # times = (vols-c) // v
        # for k in range(times+1):
        #     curr = dp[k*v+c] - k*w
        #     if hh <= tt and queue[hh][0] == k-s-1:
        #         hh += 1
        #     while hh <= tt and queue[-1][1] < curr:
        #         queue.pop()
        #         tt -= 1
        #     queue.append([k, curr])
        #     tt += 1
        #     dp[k*v+c] = queue[hh][1] + k*w
        #     print(queue[hh:tt+1])

print(dp[-1])

