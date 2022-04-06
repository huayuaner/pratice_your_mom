# 某次漫展，已知有n个打卡点，每个打卡点的活动需要 m_i 分钟完成，完成后获得奖励点 r_i，已经打卡过的点不能再去。
#
# 需要在规定 m 分钟内完成，尽可能多的收获奖励点，求获得最多的奖励点数。

# dfs
n, t = list(map(int, input().split()))
ans = 0


def dfs(time, score, matix, num):
    # nonlocal ans
    if time > t or num > len(matrix):
        return
    global ans
    ans = max(ans, score)
    for i in range(num, len(matix)):
        time += matix[i][0]
        score += matix[i][1]
        dfs(time, score, matix, i + 1)
        time -= matix[i][0]
        score -= matix[i][1]


if n == 0:
    print(0)
else:
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    dfs(0, 0, matrix, 0)
    print(ans)
