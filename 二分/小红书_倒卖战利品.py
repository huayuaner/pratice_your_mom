# 在游戏中，击败魔物后，薯队长获得了N件宝物，接下来得把这些宝物卖给宝物回收员来赚点小钱。这个回收员有个坏毛病，每次卖给他一件宝 物后，之后他就看不上比这件宝物差的宝物了。
# 在这个世界中，衡量宝物的好坏有两个维度，稀有度X和实用度H，回收员在回收一个宝物A 后，下一个宝物的
# 稀有度和实用度都不能低于等于宝物A。那么薯队长如何制定售卖顺序，才能卖给回收员宝物总个数最多。

# 排序，对另一个属性找最长递增子串
n = int(input())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))
nums.sort()
d= []
for num in nums:
    if not d or num[1]>d[-1]:
        d.append(num[1])
    else:
        l, r = 0, len(d)-1
        loc = r
        while l<=r:
            m = l+ (r-l)//2
            if d[m] >= num[1]:
                r = m-1
                loc = m
            else:
                l = m+1
        d[loc] = num[1]
print(len(d))