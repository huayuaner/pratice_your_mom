# 牛牛要参加一场程序猿世界杯，一共有2^n名选手参加比赛，选手们依次编号从1到2^n，比赛采用单淘汰制，即第一轮(1,2),(3,4)...进行比赛，第一轮的决胜者再与相连的选手进行比赛，每轮都会淘汰一半的选手，进行之后能决出冠军。
# 牛牛的编号为，但是牛牛知道了各个选手与其他选手比赛时的胜率。牛牛想知道他能夺冠的概率是多少呢，牛牛给你各个选手之间若进行比赛时的胜率，请你告诉牛牛他夺冠可能的概率是多少呢

from collections import defaultdict
n, m = map(int, input().split())
matrix = []
for _ in range(2**n):
    matrix.append([int(x)/100 for x in input().split()])
# print(matrix)
# 参赛选手编号
com = [i for i in range(1, 2**n+1)]
# 返回com中选手对应的胜率
def merge(com):
    # base case
    # 只有一个的情况
    if len(com) == 1:
        # 返回选手编号 及其 对应胜率
        return {com[0]:1}
    # 从中间分开
    mid = len(com)//2
    left = merge(com[:mid])
    right = merge(com[mid:])
    # 如果m在左半边
    if m in left:
        # 在左半边中 m 对应的胜率
        p = left[m]
        win = 0
        # m必须胜
        # p * 对应的v的胜率(就是v从right中胜出的概率) * p对上v的胜率
        for c,w in right.items():
            # m 胜， v 胜， 两者 对上 ，m胜
            win += p*w*matrix[m-1][c-1]
        return {m:win}
    # 右边同左边
    elif m in right:
        p = right[m]
        win = 0
        for c,w in left.items():
            # m 胜， v 胜， 两者 对上 ，m胜
            win += p*w*matrix[m-1][c-1]
        return {m:win}
    # 这俩部分都不包含 m
    # 要把这俩部分所有选手及其胜率都记录下来
    else:
        dic = defaultdict(int)
        for c1,w1 in left.items():
            for c2, w2 in right.items():
                dic[c1] += w1*w2*matrix[c1-1][c2-1]
                dic[c2] += w1*w2*matrix[c2-1][c1-1]
        return dic
print(float("%.10f"%merge(com)[m]))