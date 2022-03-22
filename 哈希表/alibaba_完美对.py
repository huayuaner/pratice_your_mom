# 有个N物品，每个物品有个K属性，对应属性相加的和全部相等则称为完美对
#
# 进阶：时间复杂度N log N，空间复杂度 N

# a1+b1=a2+b2 => a1-a2 = -(b1-b2)
#前一项减去后一项转化为字符串作为键
# 出现次数作为值
# 接受输入
n, k = list(map(int, input().split()))
HashMap = dict()
ans = 0
for _ in range(n):
    a = list(map(int, input().split()))
    b = [a[i-1]-a[i] for i in range(1, k)]
    #  a的键
    s1 = ''.join([str(t) for t in b])
    # 与a构成完美串的串
    s2 = ''.join([str(-t) for t in b])
    # 加上匹配上的数量
    if s2 in HashMap:
        ans += HashMap[s2]
    # 增加a字符串的出现次数
    if s1 in HashMap:
        HashMap[s1] += 1
    else:
        HashMap[s1] = 1
print(ans)