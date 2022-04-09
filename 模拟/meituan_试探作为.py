# 小美和小团所在公司的食堂有N张餐桌，从左到右摆成一排，每张餐桌有2张餐椅供至多2人用餐，公司职员排队进入食堂用餐。小美发现职员用餐的一个规律并告诉小团：当男职员进入食堂时，他会优先选择已经坐有1人的餐桌用餐，只有当每张餐桌要么空着要么坐满2人时，他才会考虑空着的餐桌；
#
# 当女职员进入食堂时，她会优先选择未坐人的餐桌用餐，只有当每张餐桌都坐有至少1人时，她才会考虑已经坐有1人的餐桌；
#
# 无论男女，当有多张餐桌供职员选择时，他会选择最靠左的餐桌用餐。现在食堂内已有若干人在用餐，另外M个人正排队进入食堂，小团会根据小美告诉他的规律预测排队的每个人分别会坐哪张餐桌。


from sys import stdin
from collections import defaultdict
import heapq as hq
N = int(input())
for _ in range(N):
    seats_num = int(input())
    seats =  [int(seat) for seat in list(input())]
    # 使用堆获取最左的位置
    hq1 = []
    hq0 = []
    for idx,s in enumerate(seats):
        if s == 2: continue
        elif s == 1:
            hq.heappush(hq1, idx)
        elif s == 0:
            hq.heappush(hq0, idx)
    # print(seats)
    num = int(input())
    person = list(input())
    for p in person:
        if p == 'M':
            if hq1:
                print(hq.heappop(hq1)+1)
            else:
                i = hq.heappop(hq0)
                hq.heappush(hq1, i)
                print(i+1)
        else:
            if hq0:
                i = hq.heappop(hq0)
                hq.heappush(hq1, i)
                print(i+1)
            else:
                print(hq.heappop(hq1)+1)