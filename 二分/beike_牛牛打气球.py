# 有n个气球，每个气球都有一个坚韧度，牛牛有一把全屏武器，
# 可以使每一个气球的坚韧度都下降b（坚韧度不会为负数），特别的：每次释放武器的时候，
# 牛牛可以选择一个气球，使得这个气球多承受a点伤害。
#
# 牛牛想知道，最少释放几次武器，可以使得所有气球的坚韧度都变成0呢？

# 二分
import math
n, a, b = map(int, input().split())
ball = list(map(int, input().split()))
# 函数用来确认这个次数能不能打完气球
def check(time):
    # math.ceil用来取得大于等于x的整数
    # 计算ball中每个值去掉范围攻击需要的a的次数
    # 如果需要的次数大于攻击的次数 则返回False
    # 否则返回True
    a_time = sum([math.ceil(max(0, ba-time*b)/a) for ba in ball])
    if a_time <= time:
        return True
    else:
        return False
# 二分 其中 右指针取max(ball)//b+1 因为这个次数一定能把所有气球消除
l, r = 1, max(ball)//b + 1
while l<r:
    m = l + (r-l)//2
    if check(m):
        r = m
    else:
        l = m+1
print(l)