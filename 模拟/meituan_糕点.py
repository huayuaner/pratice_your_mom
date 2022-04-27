# 小团的蛋糕铺长期霸占着美团APP中“蛋糕奶茶”栏目的首位，因此总会吸引各路食客前来探店。
#
# 小团一天最多可以烤n个蛋糕，每个蛋糕有一个正整数的重量。
#
# 早上，糕点铺已经做好了m个蛋糕。
#
# 现在，有一个顾客要来买两个蛋糕，他希望买这一天糕点铺烤好的最重的和最轻的蛋糕，并且希望这两个蛋糕的重量恰好为a和b。剩余的n-m个蛋糕可以现烤，请问小团能否满足他的要求？
while 1:
    try:
        n,m,a,b = list(map(int, input().split()))
        # a为大b为小
        a,b = max(a,b), min(a,b)
        cakes = list(map(int, input().split()))
        # 当前最大蛋糕和最小蛋糕
        max_cake, min_cake = max(cakes), min(cakes)
        # 如果当前最大蛋糕和最小蛋糕不在a,b范围内，直接 拒绝
        if max_cake <= a and min_cake >= b:
            # 如果两端不等，需要有2个以上多余的位置做端点蛋糕
            if max_cake < a and min_cake > b and n-m>=2:
                print('YES')
            # 一端相同，需要有1个以上多余位置做
            elif (max_cake == a and min_cake>b) or (min_cake == b and max_cake<a) and n-m>=1:
                print('YES')
            # 两端相同则不需要多于位置
            elif max_cake == a and min_cake == b:
                print('YES')
            # 其他情况均不能
            else:
                print('NO')
        else :
            print('NO')
    except:
        break